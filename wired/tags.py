import requests
from bs4 import BeautifulSoup

def scrape_links_with_https(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        links = []
        for a in a_tags:
            text = a.get_text()
            if text.startswith('https'):
                links.append(text)
        return links
def download_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content

def save_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(content))


def main():
    url = 'https://www.wired.com/sitemap/?month=6&week=4&year=2023'
    links_with_https = scrape_links_with_https(url)
    for i, link in enumerate(links_with_https):
        html_content = download_html(link)
        if html_content:
            filename = f'page{i+1}.html'
            save_html(html_content, filename)
            print(f'Successfully downloaded {filename}')

    if links_with_https:
        for i, link in enumerate(links_with_https):
             pass
            #print(f'Link {i+1}: {link}')


if __name__ == '__main__':
    main()

