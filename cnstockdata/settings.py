# -*- coding: utf-8 -*-

# Scrapy settings for cnstockdata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cnstockdata'

SPIDER_MODULES = ['cnstockdata.spiders']
NEWSPIDER_MODULE = 'cnstockdata.spiders'
FEED_FORMAT = 'csv'

ITEM_PIPELINES = {
    'cnstockdata.pipelines.FinancialDataPipelie' : 300,
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnstockdata (+http://www.yourdomain.com)'
