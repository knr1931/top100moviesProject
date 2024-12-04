from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
MOVIES_FILE_PATH = "movies.txt"

response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')

movies = soup.find_all(name='h3', class_='title')

with open(MOVIES_FILE_PATH, 'w', encoding='utf-8') as file:
    for movie in movies[-1::-1]:
        file.write(f"{movie.getText()}\n")
