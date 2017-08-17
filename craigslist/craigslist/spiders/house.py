# -*- coding: utf-8 -*-
import scrapy


class HouseSpider(scrapy.Spider):
    name = "houses"
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://losangeles.craigslist.org/search/hhh']

    def parse(self, response):

    	houses = response.xpath('//p[@class="result-info"]')
    	for house in houses:
    		title = house.xpath('a/text()').extract_first()
    		price = house.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first()
    		location = house.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
    		relative_url = house.xpath('a/@href').extract_first()
    		absolut_url = response.urljoin(relative_url)
    		print(title)
    		yield{'URL': absolut_url, 'Title': title, 'Location': location, 'Price': price }

