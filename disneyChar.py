import requests

def line():
    print("______________________________________________________")

def again():
    print("Again, choose an option")

def films():
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

    global commum_midia
    global midia_type
    global midia_c1
    global midia_c2

    commum_midia = commum_films
    midia_type = "films"
    midia_c1 = film_list_c1
    midia_c2 = film_list_c2
    lists_print()

def shorts():
    short_list_c1 = []
    short_list_c2 = []
    commum_short = []
    for page_c1 in range(page_counter_c1):
        shorts_c1 = data_c1[page_c1]["shortFilms"]
        if not shorts_c1:
            pass
        else:
            short_list_c1 = short_list_c1 + shorts_c1

    for page_c2 in range(page_counter_c2):
        shorts_c2 = data_c2[page_c2]["shortFilms"]
        if not shorts_c2:
            pass
        else:
            short_list_c2 = short_list_c2 + shorts_c2 

    for short in short_list_c1:
        if short in short_list_c2:
             commum_short.append(short)
        pass

    global commum_midia
    global midia_type
    global midia_c1
    global midia_c2

    commum_midia = commum_short
    midia_type = "Short Films"
    midia_c1 = short_list_c1
    midia_c2 = short_list_c2
    lists_print()

def tv():
    tv_list_c1 = []
    tv_list_c2 = []
    commum_tv = []
    for page_c1 in range(page_counter_c1):
        tv_c1 = data_c1[page_c1]["tvShows"]
        if not tv_c1:
            pass
        else:
            tv_list_c1 = tv_list_c1 + tv_c1

    for page_c2 in range(page_counter_c2):
        tv_c2 = data_c2[page_c2]["tvShows"]
        if not tv_c2:
            pass
        else:
            tv_list_c2 = tv_list_c2 + tv_c2 

    for tv in tv_list_c1:
        if tv in tv_list_c2:
             commum_tv.append(tv)
        pass
    global commum_midia
    global midia_type
    global midia_c1
    global midia_c2
    commum_midia = commum_tv
    midia_type = "TV Shows"
    midia_c1 = tv_list_c1
    midia_c2 = tv_list_c2
    lists_print()

def games():
    game_list_c1 = []
    game_list_c2 = []
    commum_game = []
    for page_c1 in range(page_counter_c1):
        game_c1 = data_c1[page_c1]["gameShows"]
        if not game_c1:
            pass
        else:
            game_list_c1 = game_list_c1 + game_c1

    for page_c2 in range(page_counter_c2):
        game_c2 = data_c2[page_c2]["gameShows"]
        if not game_c2:
            pass
        else:
            game_list_c2 = game_list_c2 + game_c2 

    for game in game_list_c1:
        if game in game_list_c2:
             commum_game.append(game)
        pass
    global commum_midia
    global midia_type
    global midia_c1
    global midia_c2
    commum_midia = commum_game
    midia_type = "games"
    midia_c1 = game_list_c1
    midia_c2 = game_list_c2
    lists_print()

def parks():
    park_list_c1 = []
    park_list_c2 = []
    commum_park = []
    for page_c1 in range(page_counter_c1):
        park_c1 = data_c1[page_c1]["parkAttractions"]
        if not park_c1:
            pass
        else:
            park_list_c1 = park_list_c1 + park_c1

    for page_c2 in range(page_counter_c2):
        park_c2 = data_c2[page_c2]["parkShows"]
        if not park_c2:
            pass
        else:
            park_list_c2 = park_list_c2 + park_c2 

    for park in park_list_c1:
        if park in park_list_c2:
             commum_park.append(park)
        pass
    global commum_midia
    global midia_type
    global midia_c1
    global midia_c2
    commum_midia = commum_park
    midia_type = "Park Attractions"
    midia_c1 = park_list_c1
    midia_c2 = park_list_c2
    lists_print()

def lists_print():
    if len(commum_midia) > 0:
        print(f"Yeah, {char1} and {char2} have appeared in commum {midia_type}, such as:\n")
        counter =0
        for midia in commum_midia:
            counter += 1
            print(f"{counter}-{midia},\n")
    else:
        print(f"Ops... {char1} and {char2} haven't appeared in commum {midia_type}")
    
    line = "\n____________________________________________\n"
    print(f"{line}and, that's the {midia_type} list of them:\n")
    print(f"{char1}:\n{midia_c1}\n{line}{char2}:\n{midia_c2}")
    print("Again, choose an option")


char1 = input("Character 1: ")
get_char1 = requests.get(f'https://api.disneyapi.dev/character?name={char1}')
data_c1 = get_char1.json()["data"]
page_counter_c1 = get_char1.json()["info"]["count"]

char2 = input("Character 2: ")
get_char2 = requests.get(f'https://api.disneyapi.dev/character?name={char2}')
data_c2 = get_char2.json()["data"]
page_counter_c2 = get_char2.json()["info"]["count"]


print("To find commum midia they appear\nCHOSE AN OPTION BELLOW:")
option = 0
while option != "6":
    line()
    print("1- Films\n2- Short Films\n3- TV Shows\n4- Games\n5- Park Attractions\n6 - Close Program")
    line()
    option = input("Chose: ")
    if (option == "1"):
        films()
    elif (option == "2"):
        shorts()
    elif option == "3":
        tv()
    elif option == "4":
        games()
    elif option == "5":
        parks()
    elif option == "6":
        break
    else:
        print("Wrong option, please type a valid value to contiue\nOption 6 close the program")