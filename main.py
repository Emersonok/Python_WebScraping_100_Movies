from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")
movies = soup.find_all(name="h3", class_="title")

all_movies = []
for movie in movies:
    a_movie = movie.getText()
    all_movies.append(a_movie)
    
print(all_movies)

movies = []
cont = 1
for i in all_movies:
    tamanho = len(all_movies) - cont
    movies.append(all_movies[tamanho])
    cont += 1
    
print(movies)
    



            

            