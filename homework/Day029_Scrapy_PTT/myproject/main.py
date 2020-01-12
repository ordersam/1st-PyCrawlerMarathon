import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
	# target_board = ['Gossiping', 'Stock']
	target_board = ['Gossiping']
	process = CrawlerProcess(get_project_settings())
	for board in target_board:
		process.crawl('PTTCrawler', board=board)
	process.start()     # 只可呼叫一次 stop_after_crawl=False

if __name__ == '__main__':
	main()
