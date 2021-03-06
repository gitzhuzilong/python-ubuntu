# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-11 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_point_pointhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0, help_text='余额')),
                ('customer', models.OneToOneField(help_text='客户', on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='WalletFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, help_text='发生金额')),
                ('direction', models.BooleanField(default=True, help_text='方向,增加为True，减少为False')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='发生时间')),
                ('reason', models.CharField(help_text='变动原因', max_length=32)),
                ('done', models.BooleanField(default=False, help_text='是否已完成')),
                ('payment', models.CharField(choices=[('alipay', '支付宝'), ('wechat', '微信')], help_text='支付方式', max_length=32)),
                ('paymentid', models.CharField(help_text='第三方支付id', max_length=128)),
                ('wallet', models.ForeignKey(help_text='钱包', on_delete=django.db.models.deletion.CASCADE, to='questionnaire.wallet')),
            ],
        ),
    ]
