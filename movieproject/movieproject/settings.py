# -*- coding: utf-8 -*-

# Scrapy settings for movieproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'movieproject'

SPIDER_MODULES = ['movieproject.spiders']
NEWSPIDER_MODULE = 'movieproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
user_agent_list = ["Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
                   "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
                   "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
                   "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                   "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
                   "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                   "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
                   "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
                   "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
ua = random.choice(user_agent_list)
USER_AGENT = ua

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

REDIS_HOST = '172.20.10.2'
REDIS_PORT = 6379
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
