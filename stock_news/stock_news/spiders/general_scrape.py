import time

import pandas as pd
import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse
from stock_news.items import StockNewsItem
from stock_news.public_func import mapping
from scrapy.crawler import CrawlerProcess
# from tqdm.auto import tqdm
from tqdm import tqdm

class GeneralScrapeSpider(scrapy.Spider):
    name = "general_scrape"
    allowed_domains = ["#"]

    def __init__(self, path='/home/ec2-user/KOINDB/news_data/general_market_news_sample.csv', name=None, **kwargs):

        super().__init__(name=None, **kwargs)
        self.path = path

    def start_requests(self):
        # Read the CSV file and filter URLs based on the 'source_name'
        if self.path is not None:
            df = pd.read_csv(self.path)
            # progress_bar = tqdm(range(df.shape[0]))
            start = time.time()
            print(f'------------We are scraping {df.source_name.nunique()} websites------------')
            cnt = 0
            for source in tqdm(df.source_name.unique()):
                try:
                    mapping(source)
                    start_urls = df[df['source_name'] == source]['news_url'].tolist()
                    for url in start_urls:
                        yield scrapy.Request(url, callback=self.parse, meta={'source_name': source})
                        # progress_bar.update(1)
                except ValueError:
                    continue
                # print(source)
                cnt += 1
                print(f'------------This is the website {cnt} that we scrape------------')
            end = time.time()
            print(f'It takes {round(end - start, 0)} seconds to scrape {cnt} website')

    def parse(self, response: HtmlResponse, **kwargs):
        if response.status==200:
            sel = Selector(response)
            t = StockNewsItem()
            source_name = response.meta['source_name']
            paths, img_path = mapping(source_name)
            if isinstance(paths, list):
                for path in paths:
                    paragraphs = " ".join(sel.xpath(path).extract()).strip().replace('\\', '')
                    if len(paragraphs) == 0:
                        continue
                    else:
                        break
            else:
                paragraphs = " ".join(sel.xpath(paths).extract()).strip().replace('\\', '')

            if img_path.__len__() > 0 and isinstance(img_path, list) == True:
                cnt = 0
                while cnt <= len(img_path) - 1:
                    current_path = img_path[cnt]
                    img_url = sel.xpath(current_path).extract()

                    try:
                        img_url = img_url[0]
                        if response.meta['source_name']=="aljazeera":
                            img_url = "https://www.aljazeera.com/" + img_url
                        break
                    except:
                        cnt += 1
                    if cnt == len(img_path):
                        img_url = ''

            t['source_name'] = response.meta['source_name']
            t['news_url'] = response.url
            t['news_content'] = paragraphs
            t['img_url'] = img_url
            yield t

        else:
            print(response.status,response.url)

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    }
)

if __name__ == "__main__":
    process.crawl(GeneralScrapeSpider)
    process.start()  # the script will block here until the crawling is finished