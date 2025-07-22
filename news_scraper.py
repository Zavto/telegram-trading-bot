
import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://cointelegraph.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.select("h2")[:3]
    return "\n".join([h.get_text(strip=True) for h in headlines])
