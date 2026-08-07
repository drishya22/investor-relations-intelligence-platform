import requests

from app.crawler.base import BaseCrawler


class RequestsCrawler(BaseCrawler):

    def fetch_page(self) -> str:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            ),
            "Accept": "text/html",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.get(
            self.url,
            headers=headers,
            timeout=20,
        )

        response.raise_for_status()

        return response.text