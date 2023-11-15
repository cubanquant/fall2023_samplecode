import requests
from bs4 import BeautifulSoup
import urllib.request

def download_url(url):
    """
    Reads from a URL and returns the HTML as string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def scrape_page(url):
    """
    Scrape a Wikipedia page

    :param url:
    :return:
    """
    page = download_url(url)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page, features='lxml')
    # Pull the table
    result_table = soup.find_all('table', class_="sortable plainrowheaders wikitable")

    rows = result_table[0].find_all("tr")
    headers = rows[0].find_all("th")
    winner_header = headers[1].text.strip()
    score_header = headers[2].text.strip()
    loser_header = headers[3].text.strip()
    venue_header = headers[4].text.strip()
    print(f"{winner_header:<15} - {score_header:<15} - {loser_header:<15} - {venue_header:<15}")
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        winner = cells[0].text.strip()
        score = cells[1].text.strip()
        loser = cells[2].text.strip()
        venue = cells[3].text.strip()
        print(f"{winner:<15} - {score:<15} - {loser:<15} - {venue:<15}")


if __name__ == "__main__":
    """Main entry point"""
    URL = 'https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals'
    scrape_page(URL)
