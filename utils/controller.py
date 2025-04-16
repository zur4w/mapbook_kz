def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów.')

def add_user(users_data:list)->None:
    new_name = input('Podaj imię: ')
    new_location = input('Podaj miejsce: ')
    new_posts = input('Podaj liczbę postów: ')
    users_data.append( {'name': new_name,'location': new_location,'posts': new_posts})

def remove_user(users_data:list[dict]) -> None:
    user_name=input("Podaj imię znajomego do usunięcia: ")
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)
