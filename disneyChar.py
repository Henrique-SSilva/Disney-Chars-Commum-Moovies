import requests

char1 = input("Character 1: ")
get_char1 = requests.get(f'https://api.disneyapi.dev/character?name={char1}')
data_c1 = get_char1.json()["data"]
page_counter_c1 = get_char1.json()["info"]["count"]

char2 = input("Character 2: ")
get_char2 = requests.get(f'https://api.disneyapi.dev/character?name={char2}')
data_c2 = get_char2.json()["data"]
page_counter_c2 = get_char2.json()["info"]["count"]

film_list_c1 = []
film_list_c2 = []
commum_films = []

for page_c1 in range(page_counter_c1):
    films_c1 = data_c1[page_c1]["films"]
    if not films_c1:
        pass
    else:
        film_list_c1 = film_list_c1 + films_c1

for page_c2 in range(page_counter_c2):
    films_c2 = data_c2[page_c2]["films"]
    if not films_c2:
        pass
    else:
        film_list_c2 = film_list_c2 + films_c2 

for film in film_list_c1:
    if film in film_list_c2:
         commum_films.append(film)
    pass

if len(commum_films) > 0:
    print(f"Yeah, they've appeared in commum films, such as: {commum_films}")
else:
    print(f"Ops... they've not appeared in commum films")

line = "\n____________________________________________\n"
print(f"{line}and, that's the film list of them:\n{char1}: {film_list_c1}{line}{char2}: {film_list_c2}")


