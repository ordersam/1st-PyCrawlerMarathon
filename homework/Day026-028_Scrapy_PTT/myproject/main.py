import scrapy
# 建立爬蟲流程
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    ]
	# 取得全局設定setting.py
    process = CrawlerProcess(get_project_settings())
	# 載入PTTCrawler爬蟲(可指定初始化變數)，可多個爬蟲載入(分開寫)
    process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')
	# 執行爬蟲
    process.start()

if __name__ == '__main__':
    main()
