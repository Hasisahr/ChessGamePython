import tkinter as tk
import subprocess

def pokreni_zmijica():
    subprocess.run(["python", "zmijica.py"])

def pokreni_sah_1v1():
   subprocess.run(["python", "jedanNaJedan.py"])

def pokreni_sah_comp():
    subprocess.run(["python", "mainAI.py"])

def pokreni_krizic_kruzic():
    subprocess.run(["python", "ticTacToe.py"])

glavni_prozor = tk.Tk()
glavni_prozor.geometry("700x700")
glavni_prozor.configure(bg="light gray")
glavni_prozor.title("Igraonica")

naslov = tk.Label(glavni_prozor, text="Dobrodošli!\nOdaberite igru!", height=5, font=("Times", 27, "bold"), bg= "light gray", fg="dark slate gray")
naslov.pack(pady=5)


zmijica_gumb = tk.Button(glavni_prozor, text="Zmijica", command=pokreni_zmijica, width=30, height=3, font=("Times", 15, "bold"), bg= "dark slate gray", fg="white")
zmijica_gumb.pack(pady=10)

krizic_gumb = tk.Button(glavni_prozor, text="Križić-kružić", command=pokreni_krizic_kruzic, width=30, height=3, font=("Times", 15, "bold"), bg= "dark slate gray", fg="white")
krizic_gumb.pack(pady=10)

sah1v1_gumb = tk.Button(glavni_prozor, text="Šah 1 vs 1", command=pokreni_sah_1v1, width=30, height=3, font=("Times", 15, "bold"), bg= "dark slate gray", fg="white")
sah1v1_gumb.pack(pady=10)

sah_comp_gumb = tk.Button(glavni_prozor, text="Šah protiv kompjutora", command=pokreni_sah_comp, width=30, height=3, font=("Times", 15, "bold"), bg= "dark slate gray", fg="white")
sah_comp_gumb.pack(pady=10)


glavni_prozor.mainloop()
