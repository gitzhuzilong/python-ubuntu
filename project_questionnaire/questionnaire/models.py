from datetime import date

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    '''
    #客户信息
    '''
    user = models.OneToOneField(User, on_delete=True)
    # 客户名称
    name = models.CharField(max_length=32)
    # 客户邮箱
    email = models.EmailField(null=True, blank=True)
    # 公司名称
    company = models.CharField(max_length=32, null=True, blank=True)
    # 地址
    address = models.CharField(max_length=256, null=True, blank=True)
    # 手机
    phone = models.CharField(max_length=16, null=True, blank=True)
    # 固话
    mobile = models.CharField(max_length=16, null=True, blank=True)
    # QQ
    qq = models.CharField(max_length=16, null=True, blank=True)
    # 微信
    wechat = models.CharField(max_length=16, null=True, blank=True)
    # 网站
    web = models.CharField(max_length=16, null=True, blank=True)
    # 行业
    industry = models.CharField(max_length=32, null=True, blank=True)
    # 公司简介
    description = models.TextField(null=True, blank=True)


class UserInfo(models.Model):
    '''
    #用户
    '''
    user = models.OneToOneField(User, on_delete=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True, blank=True)
    sex = models.BooleanField()
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    birthday = models.DateField(default=date(
        2018, 1, 1), null=True, blank=True)
    qq = models.CharField(max_length=16, null=True, blank=True)
    wechat = models.CharField(max_length=16, null=True, blank=True)
    job = models.CharField(max_length=32, null=True, blank=True)
    salary = models.CharField(max_length=32, null=True, blank=True)


class Questionnaire(models.Model):
    '''
    #问卷
    '''
    customer = models.ForeignKey('Customer', on_delete=True)
    title = models.CharField(default='标题', max_length=64)
    create_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    state = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    free_count = models.IntegerField(default=1)


class Question(models.Model):
    '''
    #题目
    '''
    category_choices = [
        ('radio', '单选'),
        ('select', '多选'),
    ]
    questionnaire = models.ForeignKey('Questionnaire', on_delete=True)
    title = models.CharField(max_length=128)
    index = models.IntegerField(default=0, db_index=True)
    category = models.CharField(
        choices=category_choices, default='radio', max_length=16)


class QuestionItem(models.Model):
    '''
    #题目选项
    '''
    question = models.ForeignKey('Question', on_delete=True)
    content = models.CharField(max_length=32)


class QuestionnaireSuggest(models.Model):
    '''
    #问卷建议
    '''
    userinfo = models.ForeignKey('UserInfo', on_delete=True, null=True)
    questionnaire = models.ForeignKey('Questionnaire', on_delete=True)
    create_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(default='')


class QuestionnaireComment(models.Model):
    '''
    #问卷审核
    '''
    questionnaire = models.ForeignKey('Questionnaire', on_delete=True)
    create_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()


class Answer(models.Model):
    '''
    #参与问卷
    '''
    userinfo = models.ForeignKey('UserInfo', on_delete=True)
    questionnaire = models.ForeignKey('Questionnaire', on_delete=True)
    create_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)


class AnswerItem(models.Model):
    """
    # 回答题目选项
    """
    userinfo = models.ForeignKey('UserInfo', on_delete=True, null=True, help_text="用户信息")
    item = models.ForeignKey('QuestionItem', on_delete=True, help_text="选项")


class Point(models.Model):
    '''
    #用户积分
    '''
    userinfo = models.OneToOneField('UserInfo', on_delete=True, help_text='用户信息')
    balance = models.IntegerField(default=0, help_text='余额')


class PointHistory(models.Model):
    '''
    #积分历史
    '''
    point = models.ForeignKey('Point', on_delete=True, help_text='积分历史')
    create_date = models.DateTimeField(auto_now=True, help_text='发生时间')
    quantity = models.IntegerField(default=0, help_text='数量')
    reason = models.CharField(max_length=32, help_text='变动原因')
    direction = models.BooleanField(default=True, help_text='减少为False，增加为True')


class Wallet(models.Model):
    '''
    #客户钱包
    '''
    customer = models.OneToOneField('Customer', on_delete=True, help_text='客户')
    balance = models.IntegerField(default=0, help_text='余额')


class WalletFlow(models.Model):
    '''
    #钱包流水明细
    '''
    wallet = models.ForeignKey('Wallet', on_delete=True, help_text='钱包')
    amount = models.IntegerField(default=0, help_text='发生金额')
    direction = models.BooleanField(
        default=True, help_text='方向,增加为True，减少为False')
    create_date = models.DateTimeField(auto_now=True, help_text='发生时间')
    reason = models.CharField(max_length=32, help_text='变动原因')
    done = models.BooleanField(default=False, help_text='是否已完成')
    payment = models.CharField(max_length=32, choices=[('alipay', '支付宝'), ('wechat', '微信')], help_text='支付方式')
    paymentid = models.CharField(max_length=128, help_text='第三方支付id')
