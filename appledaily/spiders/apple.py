import scrapy
import bs4

class AppledailySpider(scrapy.Spider):
    name = 'apple'
    allowed_domains = ['www.appledaily.com.hk']
    start_urls = ['https://hk.appledaily.com/archive/20210619/']

    # def parse(self, response):
    #     soup = bs4.BeautifulSoup(response.text, 'lxml')
    #     titles = soup.find_all('a', {'class': 'archive-story'})
    #     for title in titles:
    #         print(title.text)

    def parse(self, response):
        for href in response.css('.archive-story a a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)