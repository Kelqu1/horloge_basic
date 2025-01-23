from datetime import datetime
import tkinter as tk
import os

def actu_heure():
    heure_brute = datetime.now()
    heure_formaté = heure_brute.strftime("%H:%M:%S")
    resultat_label.config(text=heure_formaté)
    horloge.after(1000, actu_heure)  # Mettre à jour l'heure toutes les 1000 ms (1 seconde)

repertoire_du_projet= os.path.dirname(os.path.abspath(__file__))
logo_jeu_path=os.path.join(repertoire_du_projet, "resources/horloge.ico")

horloge = tk.Tk()
horloge.title("horloge")
horloge.iconbitmap(logo_jeu_path)
horloge.geometry("200x100")
horloge.config(bg="lightgrey")

resultat_label = tk.Label(horloge, text="", width=20, height=4, font=("Helvetica", 16), background="lightgrey")
resultat_label.pack(side="top", anchor="n", padx=10, pady=10)

actu_heure()  # Appeler une première fois pour afficher l'heure immédiatement

horloge.mainloop()
