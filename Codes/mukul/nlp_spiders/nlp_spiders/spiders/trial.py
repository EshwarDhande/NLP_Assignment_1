from scrapy.spiders import SitemapSpider
from pathlib import Path
from bs4 import BeautifulSoup, Comment
from hashlib import sha512


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def read_links():
    with open('/home/marathi_nlp/mukul/nlp_spiders/nlp_spiders/spiders/links.txt', 'r') as links_file:
        return links_file.readlines()

class MySpider(SitemapSpider):
    name = "nlp_spider"
    sitemap_urls = read_links()

    def parse(self, response):
        page = sha512(response.css("title::text")[0].get().encode('utf-8')).digest().hex()
        folder = response.url.split("/")[2]
        filename = f"/home/marathi_nlp/mukul/data/{folder}/{page}.txt"
        Path(f"/home/marathi_nlp/mukul/data/{folder}").mkdir(exist_ok=True)
        Path(filename).write_text(text_from_html(response.body), encoding='utf-8')
