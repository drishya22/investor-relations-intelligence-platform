from app.crawler.requests_crawler import RequestsCrawler


class CrawlerFactory:

    @staticmethod
    def get_crawler(url: str):

        return RequestsCrawler(url)