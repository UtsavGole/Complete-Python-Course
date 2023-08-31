user_prompt=input("Enter 'a' to add 's' to show 'f' search and  'q' to  quite: ")
movies=[]

def add_movies():
    movie_name=input("Enter movie name: ")
    movie_director=input("Enter movie Director: ")
    release_date=input("Enter release date: ")

    movies.append(
        {
        "name":movie_name,
        "director":movie_director,
        "release_date":release_date
        }
    )
    #storing_movies(movies)
    

def listing_movies():
    print('!! Details of movie  !!\n')
    for movie in movies:
        m_name=movie['name']
        m_director=movie['director']
        m_release_date=movie['release_date']

        
        row=f'Movie Name: {m_name}\nRelease Date: {m_release_date}\nMovie Director: {m_director}\n'
        print(row)

def searching_movies():
    find_movie=input("Enter the name of a movie you want to search: ")
    for movie in movies:
        if find_movie in movie['name']:
            f_name=movie['name']
            f_director=movie['director']
            f_release_date=movie['release_date']
            print("!! Searched Movie Details !!\n")
            row=f'Movie Name: {f_name}\nRelease Date: {f_release_date}\nMovie Director: {f_director}\n'
            print(row)

user_menu={
    'a':add_movies,
    's':listing_movies,
    'f':searching_movies
} 

def menu(user_prompt):
    while user_prompt!='q':
        
        if user_prompt in user_menu:
            selected_function=user_menu[user_prompt]
            selected_function()
        else:
            print("Wrong Command!!")
            
        user_prompt=input("Enter 'a' to add 's' to show 'f' search and  'q' to  quite: ")

menu(user_prompt)
print("\n!! Programme is completed !!\n")
    

