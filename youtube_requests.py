import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

video_titles = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-rich-grid-media")
creators = soup.find_all("a", class_="yt-simple-endpoint style-scope yt-formatted-string")

for title, creator in zip(video_titles, creators):
    print(f"{title.text.strip()} - {creator.text.strip()}")