from tkinter import *

import tkintermapview

root = Tk()
root.title("Mapbook_KŻ")
root.geometry("1024x768")


#RAMKI
ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0)


#RAMKA LISTA OBIEKTOW
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly=Button(ramka_lista_obiektow, text="Pokaż szczegóły")
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text="Edytuj obiekt")
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt=Button(ramka_lista_obiektow, text="Usuń obiekt")
button_usun_obiekt.grid(row=2, column=2)


#RAMKA FORMULARZ
label_formularz=Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name= Label(ramka_formularz, text="Imię: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(ramka_formularz, text="Naziwsko: ")
label_surname.grid(row=2, column=0, sticky=W)
label_posts= Label(ramka_formularz, text="Liczba postów: ")
label_posts.grid(row=3, column=0, sticky=W)
label_location= Label(ramka_formularz, text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)

entry_name= Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname= Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_posts= Entry(ramka_formularz)
entry_posts.grid(row=3, column=1)
entry_location= Entry(ramka_formularz)
entry_location.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text="Dodaj")
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)



#RAMKA SZCZEGOLY OBIEKTOW
label_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Szczegóły użytkownika: ")
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_name_szczegoly_obiektow= Label(ramka_szczegoly_obiektow, text="Imię: ")
label_name_szczegoly_obiektow.grid(row=1, column=0, sticky=W)

label_name_szczegoly_obiektow_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_name_szczegoly_obiektow_wartosc.grid(row=1, column=1, sticky=W)

label_surname_szczegoly_obiektow= Label(ramka_szczegoly_obiektow, text="Nazwisko: ")
label_surname_szczegoly_obiektow.grid(row=1, column=2, sticky=W)

label_surname_szczegoly_obiektow_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_surname_szczegoly_obiektow_wartosc.grid(row=1, column=3, sticky=W)


label_posts_szczegoly_obiektow= Label(ramka_szczegoly_obiektow, text="Posty: ")
label_posts_szczegoly_obiektow.grid(row=1, column=4, sticky=W)

label_posts_szczegoly_obiektow_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_posts_szczegoly_obiektow_wartosc.grid(row=1, column=5, sticky=W)

label_location_szczegoly_obiektow= Label(ramka_szczegoly_obiektow, text="Miejscowość: ")
label_location_szczegoly_obiektow.grid(row=1, column=6, sticky=W)

label_location_szczegoly_obiektow_wartosc= Label(ramka_szczegoly_obiektow, text="....")
label_location_szczegoly_obiektow_wartosc.grid(row=1, column=7, sticky=W)


#RAMKA MAPA
map_vidget= tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=400)
map_vidget.set_position(52.23, 21)
map_vidget.set_zoom(5)
map_vidget.grid(row=0, column=0, columnspan=3)












root.mainloop()