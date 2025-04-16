from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, update_user


def main():
    print(f'Witaj {users[0]['name']}')


while True:
    print('===========MENU===========')
    print('0 - Zakończ pracę programu.')
    print('1 - Pokaż, co u moich znajomych.')
    print('2 - Dodaj znajomego.')
    print("3 - Usuń znajomego")
    print("4 - Edytuj dane znajomego.")
    print('==========================')
    choice: str = input('Wybierz opcje menu: ')
    if choice == '0': break
    if choice == '1': get_user_info(users[1:])
    if choice == '2': add_user(users)
    if choice == '3': remove_user(users)
    if choice == '4': update_user(users)

if __name__ == '__main__':
    main()
