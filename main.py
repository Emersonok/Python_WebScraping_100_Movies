from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
top_movies = response.text



soup = BeautifulSoup(top_movies, "html.parser")
# print(soup.prettify())
movies = soup.find_all(name="h3", class_="title")

# all_movies = []
# for movie in movies:
#     a_movie = movie.getText()
#     all_movies.append(a_movie)

all_movies = [movie.getText() for movie in movies]
best_movies = all_movies[::-1]

with open ("top_100_movies.txt", "w") as file:
    for movie in best_movies:
        file.write(f"{movie}\n")
    
    

    



            

            