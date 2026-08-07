from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class BaseCrawler(ABC):
    """
    Abstract base class for all crawler implementations.
    """

    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def fetch_page(self) -> str:
        pass

    def get_soup(self) -> BeautifulSoup:
        html = self.fetch_page()
        return BeautifulSoup(html, "lxml")