import random
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def alert(entry):
    tk.Tk().withdraw()
    folder_path = filedialog.askopenfilename()

    entry.insert(0, folder_path)

def losuj_klucz(ile):
    klucz = ""
    for x in range(ile):
        klucz += str(random.randint(0, 1))
    return klucz

def roz_klucz(klucz, w, h):
    d_klucz = ""
    for x in range(int((w*h*24)/len(klucz))+1):
        d_klucz += klucz
    return d_klucz

def operacja_xor(bit_i,bit_k):
    if bit_i == bit_k:
        return '1'
    else:
        return '0'


def szyfruj(sciezka, key):
    image = Image.open(sciezka)
    width, height = image.size
    mapa_pikseli = image.load()
    glowny_klucz = roz_klucz(key, width, height)
    position = 0

    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            color = bin(r)[2:].zfill(8) + bin(g)[2:].zfill(8) + bin(b)[2:].zfill(8)

            klucz24 = glowny_klucz[position:position + 24]
            position += 24

            new_color = ""
            for k in range(24):
                new_color += operacja_xor(color[k], klucz24[k])

            mapa_pikseli[i, j] = (int(new_color[0:8], 2), int(new_color[8:16], 2), int(new_color[16:24], 2))

    image.show()
    image.save(sciezka)