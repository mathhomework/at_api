# -*- coding: utf-8 -*-

# Scrapy settings for at_scrape_exercise project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

BOT_NAME = 'at_scrape_exercise'

SPIDER_MODULES = ['at_scrape_exercise.spiders']
NEWSPIDER_MODULE = 'at_scrape_exercise.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'at_scrape_exercise (+http://www.yourdomain.com)'
os.environ['DJANGO_SETTINGS_MODULE'] = 'adventure_time.settings'