# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StockNewsPipeline:
    def open_spider(self, spider):
        # Open the CSV file for writing when the spider is opened
        self.file = open('/home/ec2-user/KOINDB/news_data/news_url.csv', 'w', encoding='utf-8')
        self.content = open('/home/ec2-user/KOINDB/news_data/news_content.csv', 'w', encoding='utf-8')
        # Create a DataFrame to store the items
        self.df_img = pd.DataFrame(columns=['source_name','news_url','img_url'])
        self.df_news = pd.DataFrame(columns=['news_url', 'news_content'])

    def process_item(self, item, spider):
        # Append the item to the DataFrame
        # print(item)
        data = [{'source_name': item['source_name'],'news_url':item['news_url'],
                                  'img_url':item['img_url']}]
        df_img_item = pd.DataFrame(data)
        self.df_img = pd.concat([self.df_img,df_img_item],ignore_index=True)

        news_data = [{'news_url':item['news_url'],'news_content':item['news_content']}]
        df_news_item = pd.DataFrame(news_data)
        self.df_news = pd.concat([self.df_news,df_news_item],ignore_index=True)

        return item

    def close_spider(self, spider):
        # Save the DataFrame to the CSV file when the spider is closed
        path = '/home/ec2-user/KOINDB/news_data/general_market_news_sample.csv'
        # path = "../dataset/general_market_news_sample.csv"
        df_original = pd.read_csv(path)
        df_img_output = df_original.merge(self.df_img,on=['source_name','news_url'],how='left')

        df_img_output.to_csv(self.file, index=False, encoding='utf-8')
        self.file.close()
        self.df_news.to_csv(self.content, index=False, encoding='utf-8')



