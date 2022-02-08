#########################################
# groupe Licence Mathématiques-Informatique 
# Hugo TIERES
# Nour BCHIBCHI
# Aomar TEBIB
# https://github.com/uvsq22103076/projet_tas_de_sable_equipe7.git
#########################################

import tkinter as tk

terrain= tk.Tk()
terrain.title("tas de sable")
canvas = tk.Canvas(terrain, bg="black", height=600 , width=600, borderwidth=0 )
canvas.grid(row=0, column=0)


terrain.mainloop()

L=[1,2,3]