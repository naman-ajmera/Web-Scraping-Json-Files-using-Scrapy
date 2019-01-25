# -*- coding: utf-8 -*-
from scrapy import Spider
import json

class TweetSpider(Spider):
    name = 'tweet'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2016.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)

        for tweet in jsonresponse:
            yield{
                    'id_str' : tweet['id_str'],
                    'favorite_count' : tweet['favorite_count'],
                    'is_retweet' : tweet['is_retweet'],
                    'text': tweet['text'],
                    'created_at' : tweet['created_at'],
                    'retweet_count' : tweet['retweet_count']               
                }           
