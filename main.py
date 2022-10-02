# program - uzytkownik wybiera folder, szyfruje wszystkie zdj i udostepnia klucz, pozwala rowniez na encode
from functions_file import *
import tkinter as tk

klucz = losuj_klucz(1024)
#zaszyfruj("C:\\Users\\alanm\\Desktop\\katalog\\imageEncode\\test.png", klucz)
#odszyfruj("C:\\Users\\alanm\\Desktop\\katalog\\imageEncode\\zakodowany.png", klucz)

window = tk.Tk()

#title
title_frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
title_frame.pack()

title = tk.Label(text="Behold, images encoding and decoding", master=title_frame)
title.pack()
#title

#przestrzen na szyfrowanie
enc_frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
enc_frame.pack(side=tk.LEFT)

enc_entry = tk.Entry(master=enc_frame, width=50)
enc_entry.pack(side=tk.LEFT)

enc_button_dirloc = tk.Button(text="Lokalizacja pliku", master=enc_frame, command=lambda: alert(enc_entry))
enc_button_dirloc.pack()

enc_button_enc = tk.Button(text="Zaszyfruj", master=enc_frame, command=lambda: szyfruj(enc_entry.get(), klucz))
enc_button_enc.pack()
enc_label = tk.Label(text="Tutaj daj plik do zaszyfrowania", master=enc_frame, relief=tk.GROOVE, borderwidth=5)
enc_label.pack()
#szyfrowanie


#przestrzen na deszyfrowanie
dec_frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
dec_frame.pack()

dec_entry = tk.Entry(master=dec_frame, width=50)
dec_entry.pack(side=tk.RIGHT)

dec_button_dirloc = tk.Button(text="Lokalizacja pliku", master=dec_frame, command=lambda: alert(dec_entry))
dec_button_dirloc.pack()

dec_button_dec = tk.Button(text="Odszyfruj", master=dec_frame, command=lambda: szyfruj(dec_entry.get(), klucz))
dec_button_dec.pack()

dec_label = tk.Label(text="Tutaj daj plik do odszyfrowania", master=dec_frame)
dec_label.pack()
#deszyfrowanie

window.mainloop()