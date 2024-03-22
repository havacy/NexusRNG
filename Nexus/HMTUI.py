import customtkinter
import pygame 
import time
import numpy as np
from PIL import Image

def Buttonpressed():
    
    Rolls = [
        "Common",
        "Bleeding",
        "Uncommon",
        "Good",
        "Natural",
        "Rare",
        "Divinus",
        "Diaboli",
        "Crystallized",
        "Rage",
        "Glacier",
        "Permafrost",
        "Wind",
        "Stormal",
        "Ruby",
        "Gilded",
        "Jackpot",
        "Precious",
        "Magnetic",
        "Sidereum",
        ":Flushed:",
        "Undead",
        "Aquatic",
        "Nautilus",
        "Exotic",
        "BOUNDED",
        "Celestial",
        "Arcane",
        "Gravitational",
        "Virtual",
        "Poseidon",
        "Hades",
        "HYPER-VOLT",
        "STARSCOURGE",
        "Chromatic",
        "Matrix",
        "Impeached",
        "Comet",
        "Galaxy",
        "Lunar",
        "Solar",
        "Undefined",
        "Archangel",
        "Abyssal Hunter"
    ]
    Roll_probabilities =  [
   500000000,2225000,112500000,100000000,62500000,31250000,19531250,11718750,6103515,7812500,2441410,1220703,
    762940,378420,567430,195315,305180,144960,72480,35360,57480,27650,14210,7090,4550,2730,2130,1060,530,330,260,210,110,110,120,
   100, 60,50,50,20,20,10,10,1
    ]
    Outof = sum(Roll_probabilities)

    #print(Outof)

    rr = np.random.choice(Rolls, p=[prob/Outof for prob in Roll_probabilities])

    Got.configure(text=rr)


base = customtkinter.CTk()
base.title("Nexus RNG")
base.geometry("700x400")


customtkinter.set_widget_scaling(1.0)  # widget dimensions and text sizepy
customtkinter.set_window_scaling(1.0)  # window geometry dimensions
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")




#Rolling Button
global Roll
Roll = customtkinter.CTkButton(base, text="Roll", command=Buttonpressed, font=('Elephant',50))
Roll.grid(row=1, column=0, padx=0, pady=0,)
Roll.configure(height=100, width=300,)
base.grid_columnconfigure(0, weight=1)

#Rolling results
global Got
Got = customtkinter.CTkLabel(base, text="Rolled", fg_color="transparent", font=('Impact',30))
Got.grid(row=0, column=0, padx=0, pady=100)
Got.configure(height=50, width=200)
Got.configure()

pygame.mixer.init()
pygame.mixer.music.load('Sounds\Skibidi.wav"')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=10, start=0, fade_ms=10000)


base.mainloop()
