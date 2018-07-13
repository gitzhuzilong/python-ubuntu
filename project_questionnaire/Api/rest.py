import random
import json
from datetime import datetime
import time
from tempfile import TemporaryFile
import base64

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
import qrcode

from Api.utils import *
from questionnaire.models import *
from Api.decorators import *
# 定义Rest类，根据客户端请求方法来执行相应请求函数


class Rest(object):
    def __init__(self, name=None):
        # 如果传入了名字就以传入的名字作为路由，没有就以类的名字的小写作为路由
        # self.__class__是指当前类，.__name__是指当前类的名字
        self.name = name or self.__class__.__name__.lower()
    # 定义一个方法，用于绑定到url

    @csrf_exempt
    def enter(self, request, *args, **kwargs):
        # 取出客户端请求方法
        method = request.method
        # 根据请求方法执行相应的处理函数
        if method == 'GET':
            # 获取资源
            return self.get(request, *args, **kwargs)
        elif method == 'POST':
            # 更新资源
            return self.post(request, *args, **kwargs)
        elif method == 'PUT':
            # 添加资源
            return self.put(request, *args, **kwargs)
        elif method == 'DELETE':
            # 删除资源
            return self.delete(request, *args, **kwargs)
        else:
            # 不支持其他方法
            return method_not_allowed()
    # 定义请求返回内容，在utils.py中封装函数统一格式，方便在后面的子类重写

    def get(self, request, *args, **kwargs):
        return method_not_allowed()

    def post(self, request, *args, **kwargs):
        return method_not_allowed()

    def put(self, request, *args, **kwargs):
        return method_not_allowed()

    def delete(self, request, *args, **kwargs):
        return method_not_allowed()
    # 获取题目信息

    def get_questions(self, obj):
        questions = []
        try:
            questionset = Question.objects.filter(questionnaire=obj)
            if questionset:
                for question in questionset:
                    dt = dict()
                    dt['id'] = question.id
                    dt['title'] = question.title
                    dt['category'] = question.category
                    dt['item'] = [model_to_dict(
                        i) for i in QuestionItem.objects.filter(question=question)]
                    questions.append(dt)
        except Exception as e:
            return json_response({'msg': '参数错误'})
        return questions
    # 获取单个问卷信息

    def get_questionnaire(self, obj):
        questionnairecomments = QuestionnaireComment.objects.filter(
            questionnaire=obj)
        dt = dict()
        dt['id'] = obj.id
        dt['title'] = obj.title
        dt['quantity'] = obj.quantity
        dt['free_count'] = obj.free_count
        # %H:%M:%S
        dt['deadline'] = obj.deadline.strftime('%Y-%m-%d')
        dt['create_date'] = obj.create_date.strftime('%Y-%m-%d')
        dt['state'] = obj.state
        dt['customer'] = {'id': obj.customer_id,
                          'name': obj.customer.name}
        questions = self.get_questions(obj)
        dt['questions'] = questions
        dt['comments'] = [{'id': questionnairecomment.id, 'create_date': questionnairecomment.create_date.strftime(
            '%Y-%m-%d'), 'comment': questionnairecomment.comment} for questionnairecomment in questionnairecomments]
        return dt
    # 获取问卷

    def get_questionnaires(self, questionnaire_data, user):
        page = int(questionnaire_data.get('page', 1))
        limit = int(questionnaire_data.get('limit', 10))
        with_detail = questionnaire_data.get('with_detail', False)
        questionnaire_id = questionnaire_data.get('id', '')
        print('hello')
		if hasattr(user, 'customer'):
            user = user.customer
            state = questionnaire_data.get('status', [0])
            questionnaires = Questionnaire.objects.filter(
                customer=user, state__in=state)
        elif hasattr(user, 'userinfo'):
            user = user.userinfo
            state = questionnaire_data.get('status', [4])
            now_time = time.strftime('%Y-%m-%d')
            answers = Answer.objects.filter(userinfo=user)
            joinde_questionaires = [
                answer.questionnaire_id for answer in answers]
            questionnaires = Questionnaire.objects.exclude(id__in=joinde_questionaires).filter(
                free_count__gt=0, deadline__gt=now_time, state__in=state)
        else:
            state = questionnaire_data.get('status', [1])
            questionnaires = Questionnaire.objects.filter(state__in=state)
        data = dict()
        if questionnaires.count() // limit == 0:
            data['pages'] = questionnaires.count() // limit
        else:
            data['pages'] = questionnaires.count() // limit + 1
        data['count'] = questionnaires.count()
        data['objs'] = []
        if questionnaire_id:
            try:
                obj = questionnaires.get(
                    id=questionnaire_id, state__in=state)
            except Exception as e:
                return json_response({'msg': '参数错误'})
            questions = self.get_questions(obj)
            data['objs'] = [self.get_questionnaire(obj)]
        else:
            try:
                objs = questionnaires[limit*(page-1): limit*page]
            except Exception as e:
                return json_response({'msg': '参数错误'})
            for obj in objs:
                data['objs'].append(self.get_questionnaire(obj))
        if not with_detail:
            for i in data['objs']:
                i.pop('questions')
        return data


class Register(object):
    def __init__(self,):
        self.resources = []

    def regist(self, resource):
        self.resources.append(resource)

    @property
    def urls(self):
        urlpatterns = [
            url(r'^{}$'.format(resource.name), resource.enter)
            # 列表生成式
            for resource in self.resources
        ]
        return urlpatterns


class SessionRest(Rest):
    # 登陆
    def put(self, request, *args, **kwargs):
        data = request.PUT
        username = data.get('username', '')
        password = data.get('password', '')
        # 查询数据库用户表
        user = authenticate(username=username, password=password)
        if user:
            # 保存登陆状态
            login(request, user)
            return json_response({
                "msg": "登陆成功"
            })
        else:
            return params_error({
                "msg": "用户名或密码错误"
            })
    # 退出

    def delete(self, request, *args, **kwargs):
        logout(request)
        return json_response({"msg": "退出成功"})


class UserRest(Rest):
    # 获取用户信息
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            data = dict()
            if hasattr(user, 'customer'):
                customer = user.customer
                data['username'] = customer.name
                data['email'] = customer.email
                data['company'] = customer.company
                data['address'] = customer.address
                data['phone'] = customer.phone
                data['mobile'] = customer.mobile
                data['qq'] = customer.qq
                data['wechat'] = customer.wechat
                data['web'] = customer.web
                data['industry'] = customer.industry
                data['description'] = customer.description
                data['user'] = user.id
                data['category'] = 'customer'
            elif hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                data['username'] = userinfo.name
                data['age'] = userinfo.age
                data['sex'] = userinfo.sex
                data['phone'] = userinfo.phone
                data['email'] = userinfo.email
                data['address'] = userinfo.address
                data['birthday'] = userinfo.birthday
                data['qq'] = userinfo.qq
                data['wechat'] = userinfo.wechat
                data['job'] = userinfo.job
                data['salary'] = userinfo.salary
                data['user'] = user.id
                data['category'] = 'userinfo'
            else:
                return json_response({})
        else:
            return not_authenticated()
        return json_response(data)
    # 更新用户信息

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        if user.is_authenticated:
            if hasattr(user, 'customer'):
                customer = user.customer
                customer.name = data.get('username', '')
                customer.email = data.get('email', '')
                customer.save()

            elif hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                userinfo.name = data.get('username', '')
                userinfo.qq = data.get('qq', '')
                userinfo.save()
            else:
                return json_response({
                    "msg": "更新成功"
                })
        else:
            return not_authenticated()
        return json_response({"msg": "更新成功"})
    # 创建用户信息

    def put(self, request, *args, **kwargs):
        data = request.PUT

        username = data.get('username', '')
        password = data.get('password', '')
        ensure_password = data.get('ensure_password', '')
        regist_code = data.get('regist_code', 0)
        session_regist_code = request.session.get('regist_code', 1)
        email = data.get('email', '')
        company = data.get('company', '')
        address = data.get('address', '')
        phone = data.get('phone', '')
        mobile = data.get('mobile', '')
        qq = data.get('qq', '')
        wechat = data.get('wechat', '')
        web = data.get('web', '')
        industry = data.get('industry', '')
        description = data.get('description', '')
        age = data.get('age')
        sex = data.get('sex', 0)
        birthday = data.get('birthday')
        job = data.get('job', '')
        salary = data.get('salary')

        error = dict()
        if not username:
            error['username'] = '必须提供用户名'
        else:
            if User.objects.filter(username=username).count() > 0:
                error['username'] = '用户名已存在'
        if len(password) < 6:
            error['password'] = '密码长度不可小于6位'
        if password != ensure_password:
            error['ensure_password'] = '密码不匹配'
        if regist_code != session_regist_code:
            error['regist_code'] = '验证码不匹配'
        if error:
            return params_error(error)
        user = User()
        user.username = username
        user.set_password(password)
        user.save()

        category = data.get('category', 'userinfo')
        if category == 'userinfo':
            # 创建普通用户
            user_obj = UserInfo()
            user_obj.name = username
            user_obj.age = age
            if sex == 0:
                sex = True
            else:
                sex = False
            user_obj.sex = sex
            user_obj.phone = phone
            user_obj.email = email
            user_obj.address = address
            user_obj.birthday = birthday
            user_obj.qq = qq
            user_obj.wechat = wechat
            user_obj.job = job
            user_obj.salary = salary
        else:
            # 创建客户
            user_obj = Customer()
            user_obj.name = username
            user_obj.email = email
            user_obj.company = company
            user_obj.address = address
            user_obj.phone = phone
            user_obj.mobile = mobile
            user_obj.qq = qq
            user_obj.wechat = wechat
            user_obj.web = web
            user_obj.industry = industry
            user_obj.description = description
        user_obj.user = user
        user_obj.save()
        return json_response({'id': user.id})


class RegistCode(Rest):
    def get(self, request, *args, **kwargs):
        # 获取6位随机数字
        regist_code = random.randint(100000, 1000000)
        # 保存到session中
        request.session['regist_code'] = regist_code
        # 返回随机数
        return json_response({'regist_code': regist_code})


class CustomerQuestionnaire(Rest):
    # 装饰器判断用户是否登录以及登录用户是否是客户
    @customer_require
    # 创建问卷
    def put(self, request, *args, **kwargs):
        data = request.PUT
        customer = request.user.customer
        questionnaire = Questionnaire()
        questionnaire.title = data.get('title')
        questionnaire.deadline = datetime.strptime(
            data.get('expire_date'), '%Y-%m-%d')
        questionnaire.quantity = data.get('quantity', 1)
        questionnaire.free_count = data.get('quantity', 1)
        questionnaire.customer = customer
        questionnaire.save()
        return json_response({'id': questionnaire.id})

    @customer_require
    # 更新问卷
    def post(self, request, *args, **kwargs):
        data = request.POST
        customer = request.user.customer
        questionnaire_id = data.get('questionnaire_id')
        try:
            questionnaire = Questionnaire.objects.get(
                pk=questionnaire_id, customer=customer, state__in=[0, 1, 2, 3])
        except Exception as e:
            return json_response({'msg': '找不到该问卷或当前问卷不可修改'})
        questionnaire.title = data.get('title')
        questionnaire.deadline = datetime.strptime(
            data.get('expire_date'), '%Y-%m-%d')
        questionnaire.quantity = data.get('quantity', 1)
        questionnaire.free_count = data.get('quantity', 1)
        questionnaire.state = 0
        questionnaire.save()
        return json_response({'msg': '问卷更新成功'})

    @customer_require
    # 删除问卷
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        customer = request.user.customer
        questionnaire_ids = data.get('ids')
        for questionnaire_id in questionnaire_ids:
            try:
                questionnaire = Questionnaire.objects.get(
                    pk=questionnaire_id, customer=customer, state__in=[0, 2, 3])
            except Exception as e:
                return json_response({'msg': '找不到问卷'})
            questionnaire.delete()
        return json_response({'deleted_ids': questionnaire_ids})

    @customer_require
    # 获取问卷
    def get(self, request, *args, **kwargs):
        questionnaire_data = request.GET
        user = request.user
        data = self.get_questionnaires(
            questionnaire_data, user)
        return json_response(data)


class CustomerQuestion(Rest):
    @customer_require
    # 创建题目
    def put(self, request, *args, **kwargs):
        data = request.PUT
        customer = request.user.customer
        title = data.get('title')
        category = data.get('category', 'radio')
        questionnaire_id = data.get('questionnaire_id')
        items = data.get('items')
        question = Question()
        question.title = title
        question.category = category
        try:
            questionnaire = Questionnaire.objects.filter(
                id=questionnaire_id, customer=customer)[0]
        except Exception as e:
            return json_response({'msg': '问卷找不到'})
        question.questionnaire = questionnaire
        question.save()
        for item in items:
            questionitem = QuestionItem()
            questionitem.question = question
            questionitem.content = item
            questionitem.save()
        questionnaire.state = 0
        questionnaire.save()
        return json_response({'id': question.id})

    @customer_require
    # 更新题目
    def post(self, request, *args, **kwargs):
        data = request.POST
        customer = request.user.customer
        title = data.get('title')
        category = data.get('category', 'radio')
        question_id = data.get('question_id')
        items = data.get('items')
        try:
            question = Question.objects.get(
                pk=question_id, questionnaire__customer=customer, Questionnaire__state__in=[0, 1, 2, 3])
        except Exception as e:
            return json_response({'msg': '找不到问题'})
        question.title = title
        question.category = category
        question.save()
        question.questionitem_set.all().delete()
        for item in items:
            questionitem = QuestionItem()
            questionitem.question = question
            questionitem.content = item
            questionitem.save()
        questionnaire = question.questionnaire
        questionnaire.state = 0
        questionnaire.save()
        return json_response({'msg': '题目更新成功'})

    @customer_require
    # 删除题目
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        customer = request.user.customer
        question_ids = data.get('question_ids')
        try:
            questions = Question.objects.filter(
                id__in=question_ids, questionnaire__customer=customer, questionnaire__state__in=[0, 1, 2, 3])
        except Exception as e:
            return json_response({'msg': '找不到要删除的问题'})
        deleted_ids = [question.id for question in questions]
        questionnaire_set = set()
        for question in questions:
            questionnaire_set.add(question.questionnaire)
        for questionnaire in questionnaire_set:
            questionnaire.state = 0
            questionnaire.save()
        questions.delete()
        return json_response({'deleted_ids': deleted_ids})


class QuestionnaireState(Rest):
    @customer_require
    # 客户提交问卷审核或发布
    def post(self, request, *args, **kwargs):
        data = request.POST
        customer = request.user.customer
        questionnaire_id = data.get('questionnaire_id')
        state = data.get('state')
        try:
            questionnaire = Questionnaire.objects.get(
                id=questionnaire_id, customer=customer)
        except Exception as e:
            return json_response({'msg': '找不到该问卷'})
        if state == 1:
            if questionnaire.state in [0, 2]:
                questionnaire.state = 1
                questionnaire.save()
            else:
                return json_response({'msg': '当前问卷未处理可提交审核状态'})
        if state == 4:
            if questionnaire.state == 3:
                questionnaire.state = 4
                questionnaire.save()
            else:
                return json_response({'msg': '当前问卷未处理可提交发布状态'})
        return json_response({'msg': '提交成功'})

class PayMent(Rest):
    def create_qrcode(self, data):
        img = qrcode.make(data)
        tmp = TemporaryFile()
        img.save(tmp)
        tmp.seek(0)
        return base64.b64encode(tmp.read()).decode()
    @customer_require
    #客户充值
    def put(self, request, *args, **kwargs):
        data = request.PUT
        customer = request.user.customer
        amount = int(data.get('amount'))
        if amount <= 0:
            return json_response({'msg': '请输入正确的金额'})
        wallet = Wallet.objects.get(customer=customer)
        wallet.balance += int(amount)
        walletflow = WalletFlow()
        walletflow.amount = amount


class QuestionnaireJoin(Rest):
    @userinfo_require
    # 用户查看问卷
    def get(self, request, *args, **kwargs):
        questionnaire_data = request.GET
        user = request.user
        data = self.get_questionnaires(questionnaire_data, user)
        return json_response(data)


class Participation(Rest):
    @userinfo_require
    # 用户参与问卷
    def put(self, request, *args, **kwargs):
        data = request.PUT
        userinfo = request.user.userinfo
        questionnaire_id = data.get('questionnaire_id')
        print(questionnaire_id)
        answer = Answer()
        now_time = time.strftime('%Y-%m-%d')
        try:
            questionnaire = Questionnaire.objects.get(
                id=questionnaire_id, state=4, deadline__gt=now_time, free_count__gt=0)
        except Exception as e:
            return json_response({'msg': '该问卷已参与或不存在'})
        answer.questionnaire = questionnaire
        answer.userinfo = userinfo
        questionnaire.free_count -= 1
        if questionnaire.free_count < 0:
            return json_response({'msg': '当前问卷参与人数已满'})
        answer.save()
        questionnaire.save()
        return json_response({'msg': '参与成功'})

    @userinfo_require
    # 用户退出参与问卷
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        userinfo = request.user.userinfo
        questionnaire_ids = data.get('questionnaire_ids')
        questionnaires = Questionnaire.objects.filter(id__in=questionnaire_ids)
        answers = Answer.objects.filter(
            questionnaire__in=questionnaires, userinfo=userinfo, is_done=False)
        items = QuestionItem.objects.filter(question__questionnaire__in=questionnaires)
        answeritem = AnswerItem.objects.filter(item__in=items, userinfo=userinfo)
        answeritem.delete()
        for answer in answers:
            answer.delete()
        for questionnaire in questionnaires:
            questionnaire.free_count += 1
            questionnaire.save()
        return json_response({'msg': questionnaire_ids})

    @userinfo_require
    #用户查看参与信息
    def get(self, request, *args, **kwargs):
        questionnaire_data = request.GET
        userinfo = request.user.userinfo
        state = questionnaire_data.get('state', 'true')
        page = questionnaire_data.get('page', 1)
        limit = questionnaire_data.get('limit', 10)
        if state == 'false':
            answers = Answer.objects.filter(userinfo=userinfo, is_done=False)[(int(page)-1)*int(limit): int(page)*int(limit)]
        elif state == 'true':
            answers = Answer.objects.filter(userinfo=userinfo, is_done=True)[(int(page)-1)*int(limit): int(page)*int(limit)]
        else:
            return json_response({'msg': '请输入正确的类型'})
        data = []
        for answer in answers:
            join_dict = dict()
            questionnaire = Questionnaire.objects.get(id=answer.questionnaire_id)
            join_dict['questionnaire'] = {'title': questionnaire.title}
            join_dict['join_date'] = answer.create_date.strftime('%Y-%m-%d')
            join_dict['state'] = answer.is_done
            data.append(join_dict)
        return json_response(data)

class UserInfoAnswer(Rest):
    # 保存答案
    def saveanswers(self, data, request):
        questionnaire_id = data.get('questionnaire_id', 0)
        questionnaire_exist = Questionnaire.objects.filter(
            id=questionnaire_id, state=4, deadline__gt=time.strftime('%Y-%m-%d'))
        if not questionnaire_exist:
            return params_error({
                'questionnaire_id': '问卷不存在或者不可提交答案'
            })
        questionnaire = questionnaire_exist[0]
        has_joined = Answer.objects.filter(
            questionnaire=questionnaire, userinfo=request.user.userinfo, is_done=False)
        if not has_joined:
            return params_error({
                'questionnaire_id': '还没有参与该问卷或者该问卷已完成'
            })
        questions = data.get('questions', [])
        question_ids = [item['question_id'] for item in questions]
        questions_can_answer = Question.objects.filter(
            id__in=question_ids, questionnaire=questionnaire)
        questions_can_answer_ids = [obj.id for obj in questions_can_answer]
        questions_items = QuestionItem.objects.filter(
            question_id__in=questions_can_answer_ids)
        AnswerItem.objects.filter(
            item__in=questions_items, userinfo=request.user.userinfo).delete()
        for question in questions:
            if question['question_id'] in questions_can_answer_ids:
                question_obj = Question.objects.get(id=question['question_id'])
                items = QuestionItem.objects.filter(
                    id__in=question['items'], question=question_obj)
                if items.count() > 1 and question_obj.is_checkbox:
                    for item in items:
                        answer = AnswerItem()
                        answer.item = item
                        answer.question = question_obj
                        answer.userinfo = request.user.userinfo
                        answer.save()
                elif items.count() == 1:
                    answer = AnswerItem()
                    answer.question = question_obj
                    answer.userinfo = request.user.userinfo
                    answer.item = items[0]
                    answer.save()
                else:
                    return json_response({
                        'warning': '参数错误'
                    })
        answer = has_joined[0]
        is_done = data.get('is_done', False)
        answer.is_done = is_done
        answer.save()
        return json_response({'answer': '提交成功'})

    @userinfo_require
    # 用户选择答案
    def put(self, request, *args, **kwargs):
        data = request.PUT
        response = self.saveanswers(data, request)
        return response

    @userinfo_require
    # 用户取消已选择的答案
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        userinfo = request.user.userinfo
        item_ids = data.get('item_ids')
        answeritems = AnswerItem.objects.filter(
            item_id__in=item_ids, userinfo=userinfo)
        for answeritem in answeritems:
            answeritem.delete()
        return json_response({'msg': '删除选择成功'})


class UserParticipationState(Rest):
    @userinfo_require
    # 用户完成答题
    def post(self, request, *args, **kwargs):
        data = request.POST
        userinfo = request.user.userinfo
        questionnaire_id = data.get('questionnaire_id')
        answer = Answer.objects.get(
            questionnaire_id=questionnaire_id, userinfo=userinfo)
        if answer:
            if answer.is_done:
                point = Point.objects.get(userinfo=userinfo)
                try:
                    point = Point.objects.get(userinfo=userinfo)
                except Exception as e:
                    point = Point()
                    point.userinfo = userinfo
                    point.save()
                point.balance += 1
                point.save()
                pointhistory = PointHistory()
                pointhistory.quantity = 1
                pointhistory.reason = '完成问卷'
                pointhistory.direction = True
                pointhistory.point = point
                pointhistory.save()
            else:
                return json_response({'msg': '问卷未完成'})
        else:
            return json_response({'msg': '未参与该问卷'})
        return json_response({'msg': '提交答案成功'})


class UserPointHistory(Rest):
    @userinfo_require
    # 用户查看积分
    def get(self, request, *args, **kwargs):
        point_data = request.GET
        userinfo = request.user.userinfo
        data = dict()        
        point = Point.objects.get(userinfo=userinfo)
        category = point_data.get('category', 'true')
        page = point_data.get('page', 1)
        limit = point_data.get('limit', 10)
        data['balance'] = point.balance
        if category == 'true':
            pointhistories = PointHistory.objects.filter(point=point, direction=True)[(int(page)-1)*int(limit): int(page)*int(limit)]
        elif category == 'false':
            pointhistories = PointHistory.objects.filter(point=point, direction=False)[(int(page)-1)*int(limit): int(page)*int(limit)]
        else:
            return json_response({'msg': '请输入正确的类型'})
        data['hsitories'] = [{'create_date': pointhistory.create_date.strftime('%Y-%m-%d'), 'amount': pointhistory.quantity,
                              'reason': pointhistory.reason} for pointhistory in pointhistories]
        return json_response(data)

class UserAnswer(Rest):
    @userinfo_require
    # 用户查看问卷答案
    def get(self, request, *args, **kwargs):
        answer_data = request.GET
        userinfo = request.user.userinfo
        questionnaire_id = answer_data.get('questionnaire_id')
        user_joined = Answer.objects.filter(
            questionnaire_id=questionnaire_id, userinfo=userinfo)
        if user_joined:
            try:
                questionnaire = Questionnaire.objects.get(id=questionnaire_id)
            except Exception as e:
                return json_response({'msg': '所查询的问卷不存在'})
        else:
            return json_response({'msg': '用户未参与该问卷'})
        data = dict()
        data['questionnaire'] = {'title': questionnaire.title, 'expire_date': questionnaire.deadline.strftime(
            '%Y-%m-%d'), 'customer': questionnaire.customer.name}
        questions = Question.objects.filter(questionnaire=questionnaire)
        data['questions'] = []
        for question in questions:
            question_dict = dict()
            question_dict['title'] = question.title
            question_dict['category'] = question.category
            question_dict['id'] = question.id
            items = QuestionItem.objects.filter(question=question)
            question_dict['item'] = []
            for item in items:
                item_dict = dict()
                item_dict['id'] = item.id
                item_dict['content'] = item.content
                if AnswerItem.objects.filter(item=item):
                    item_dict['is_select'] = 'ture'
                else:
                    item_dict['is_select'] = 'false'
                question_dict['item'].append(item_dict)
            data['questions'].append(question_dict)
        return json_response(data)


class AdminQuestionnaire(Rest):
    @admin_require
    # 管理员查看问卷
    def get(self, request, *args, **kwargs):
        questionnaire_data = request.GET
        user = request.user
        data = self.get_questionnaires(questionnaire_data, user)
        return json_response(data)


class AdminQuestionnaireComment(Rest):
    @admin_require
    # 管理员审核问卷
    def put(self, request, *args, **kwargs):
        data = request.PUT
        questionnaire_id = data.get('questionnaire_id')
        comment = data.get('comment')
        is_agree = data.get('is_agree', True)
        questionnairecomment = QuestionnaireComment()
        try:
            questionnaire = Questionnaire.objects.get(
                id=questionnaire_id, state=1)
        except Exception as e:
            return json_response({'msg': '找不到问卷'})
        questionnairecomment.comment = comment
        if is_agree:
            questionnaire.state = 4
            questionnaire.save()
        else:
            questionnaire.state = 3
            questionnaire.save()
        questionnairecomment.save()
        return json_response({'msg': '审核结果已提交'})
