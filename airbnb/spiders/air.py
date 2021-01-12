import scrapy
import pandas as pd

class airSpider(scrapy.Spider):
    name = "airbnb"

    def start_requests(self):
        df = pd.read_csv("/home/ashish/Downloads/airbnb_online.csv")
        for i in range(df.shape[0]):
            yield scrapy.Request(url=df.iloc[i,0], callback=self.parse)

    def parse(self,response):
       title = response.css('h1::text').extract()
       ratings = response.css('._6ijom0::text').extract_first()
       number = response.css('._krjbj::text').extract_first()
       location = response.css('._y5ztp3::text').extract()
       content = response.css('._g9yb1m ._16e70jgn div ._1gw6tte div span ._1y6fhhr span::text').extract()
       content = ' '.join(content)
       since = response.css('._1fg5h8r::text').extract_first()
       reviews = response.css('._pog3hg::text').extract()
       comment = response.css('._1gw6tte ._zcn96s ._4i7tcd div ._1byskwn ._5702fc7 section span ._1y6fhhr span::text').extract()
       comment = ' '.join(comment)
       scraped_info={
       'Title':title[0],
       'Rating':ratings,
       'No of reviews':number,
       'location':location[0],
       'Part of':location[1],
       'What you will do':content,
       'Host': title[1],
       'Since':since,
       'reviews':reviews[0],
       'verification':reviews[1],
       'comment': comment,
       'url':response.url,
       }
       yield scraped_info
