from tkinter import *
import zaidimas

# tkinter lango parametrai
langas = Tk()
langas.geometry("800x450")
langas.title('Kryžiukai-nuliukai')


# paleisti žaidimui ir nunulinti parametrus po paskutinio paleidimo
def zaisti():
    zaidimas.occupied = {"blue": [], "white": []}
    zaidimas.validinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    zaidimas.rounds = 1
    zaidimas.main()

# žaidimo taisyklių aprašymas
label1 = Label(langas, text="\nŽaidimas žaidžiamas dviese.\n"
                            "\n Vienas žaidėjas sau pasiima mėlynos, o kitas – baltos spalvos apskritimą.\n "
                            "\n Mėlynasis pradės pirmas.\n "
                            "\n Pirmasis žaidėjas deda savo ženklą į norimą langelį. Antrasis padeda savo ženklą į norimą laisvą langelį ir t.t. pakaitomis.\n"
                            "\n Žaidimo tikslas – surinkti tris vienodus ženklus vienoje linijoje (horizontaliai, vertikaliai arba įstrižai).\n"
                            "\n Laimi tas, kuris pirmasis surenka liniją iš savo figūrų.\n"
                            "\n Jeigu nei vienam žaidėjui to nepavyksta padaryti, o visi langeliai jau užimti, tuomet skelbiamos lygiosios ir žaidžiama nauja partija.\n "
                            "\n Smagaus žaidimo!\n")

# mygtuko parametrai
button1 = Button(langas, text="Pradėti naują žaidimą ->", command=zaisti)
button1.bind("<Button-1>", zaisti)

label1.grid(row=1, column=0)
button1.grid(row=5, columnspan=2)


langas.mainloop()