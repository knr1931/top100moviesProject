from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')

movies = soup.find_all(name='h3', class_='title')

movies_file_name = "movies.txt"

with open(movies_file_name, 'w', encoding='utf-8') as file:
    for movie in movies[-1::-1]:
        file.write(f"{movie.getText()}\n")
