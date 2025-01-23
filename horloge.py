from datetime import datetime
import tkinter as tk
import os
import math

def dessiner_aiguille(canvas, x, y, longueur, angle, largeur):
    radian = math.radians(angle)
    x_fin = x + longueur * math.sin(radian)
    y_fin = y - longueur * math.cos(radian)
    canvas.create_line(x, y, x_fin, y_fin, width=largeur)

def actu_heure():
    heure_brute = datetime.now()
    heures = heure_brute.hour % 12
    minutes = heure_brute.minute
    secondes = heure_brute.second

    canvas.delete("all")

    # Dessiner le cadran
    canvas.create_oval(10, 10, 190, 190, width=2)
    for i in range(12):
        angle = i * 30
        x1 = 100 + 80 * math.sin(math.radians(angle))
        y1 = 100 - 80 * math.cos(math.radians(angle))
        x2 = 100 + 90 * math.sin(math.radians(angle))
        y2 = 100 - 90 * math.cos(math.radians(angle))
        canvas.create_line(x1, y1, x2, y2, width=2)

    # Dessiner les aiguilles
    dessiner_aiguille(canvas, 100, 100, 60, heures * 30 + minutes / 2, 4)  # Heures
    dessiner_aiguille(canvas, 100, 100, 80, minutes * 6, 3)  # Minutes
    dessiner_aiguille(canvas, 100, 100, 90, secondes * 6, 1)  # Secondes

    horloge.after(1000, actu_heure)  # Mettre à jour l'heure toutes les 1000 ms (1 seconde)

repertoire_du_projet = os.path.dirname(os.path.abspath(__file__))
logo_jeu_path = os.path.join(repertoire_du_projet, "resources/horloge.ico")

horloge = tk.Tk()
horloge.title("Horloge")
horloge.iconbitmap(logo_jeu_path)
horloge.geometry("200x200")
horloge.config(bg="lightgrey")

canvas = tk.Canvas(horloge, width=200, height=200, bg="lightgrey")
canvas.pack()

actu_heure()  # Appeler une première fois pour afficher l'heure immédiatement

horloge.mainloop()