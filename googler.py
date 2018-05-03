import requests
from bs4 import BeautifulSoup
from random import choice

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

USER_AGENT = random_headers()

class google:
    def __init__(self):
        pass

    def fetch_results(self, search_term, number_results, language_code):
        assert isinstance(search_term, str), 'Search term must be a string'
        assert isinstance(number_results, int), 'Number of results must be an integer'
        self.escaped_search_term = search_term.replace(' ', '+')
     
        self.google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(self.escaped_search_term, number_results, language_code)
        self.response = requests.get(self.google_url, headers=USER_AGENT)
        self.response.raise_for_status()
     
        return search_term, self.response.text

    def parse_results(self, html, keyword):
        self.soup = BeautifulSoup(html, 'html.parser')

        self.found_results = []
        self.rank = 1
        self.result_block = self.soup.find_all('div', attrs={'class': 'g'})
        for self.result in self.result_block:

            self.link = self.result.find('a', href=True)
            self.title = self.result.find('h3', attrs={'class': 'r'})
            self.description = self.result.find('span', attrs={'class': 'st'})
            if self.link and self.title:
                self.link = self.link['href']
                self.title = self.title.get_text()
                if self.description:
                    self.description = self.description.get_text()
                if self.link != '#':
                    self.found_results.append({'keyword': keyword, 'rank': self.rank, 'description': self.description})
                    self.rank += 1
        return self.found_results

    def search_google(self, question):
        self.question   = question  # Question to Google
        #print(self.question)
        self.keyword, self.html = self.fetch_results(self.question, 400, 'en')
        self.results = self.parse_results(self.html, self.keyword)
        return self.results
