from bs4 import BeautifulSoup
import requests


# link = https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/

def download(url):
    """
    Reads data from a URL and returns data as string

    :param url:
    :return:
    """
    return requests.get(url).text


if __name__ == "__main__":
    football_url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/"
    scoring_data = download(football_url)

    soup = BeautifulSoup(scoring_data, features="lxml")
    touchdown_data = soup.find_all('div', class_="Page-colMain")

    print(touchdown_data)
