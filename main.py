users:list=[
    {'name':'Kamil','location':'Lipce Reymontowskie','posts':100},
    {'name':'Wiktoria','location':'Chełm','posts':6},
    {'name':'Bartosz','location':'Maliniec','posts':110},
    {'name':'Łukasz','location':'Wrocław','posts':80},

]


print(f'Witaj {users[0]['name']}')

for user in users:
    print(f'Twój znajomy {user['name']} z {user['location']} opublikował {user['posts']} postów.')

