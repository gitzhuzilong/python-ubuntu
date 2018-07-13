# python自带包放第一
# 第三方放第二
# 自己写的方第三
from django.conf.urls import url

from Api.rest import *

# 新建session对象
# session_obj = SessionRest()
# 新建user对象
# user_obj = UserRest()

# api_urls = [
#     url('session', session_obj.enter),
#     url('user', user_obj.enter)
# ]

api = Register()
#登陆
api.regist(SessionRest('session'))
#用户创建
api.regist(UserRest('user'))
#验证码
api.regist(RegistCode())
#客户问卷增删查
api.regist(CustomerQuestionnaire('customer_questionnaire'))
#客户问题增删查
api.regist(CustomerQuestion('customer_question'))
#问卷提交审核、发布
api.regist(QuestionnaireState('questionnaire_state'))
#用户对问卷查看、参与
api.regist(QuestionnaireJoin('user_questionnaire'))
#管理员对问卷查看
api.regist(AdminQuestionnaire('admin_questionnaire'))
#管理员审核问卷
api.regist(AdminQuestionnaireComment('questionnaire_comment'))
#用户参与问卷、查看参与信息
api.regist(Participation())
#用户选择答案
api.regist(UserInfoAnswer('answer'))
#用户查看答案
api.regist(UserAnswer('user_answer'))
#用户提交答案
api.regist(UserParticipationState('user_participation_state'))
#用户查看积分
api.regist(UserPointHistory('user_point_history'))



class A(object):
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(B, C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B, C):
    pass