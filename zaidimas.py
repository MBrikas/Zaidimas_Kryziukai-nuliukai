def main():
    import turtle as t
    from tkinter import messagebox
    # žaidimo ekrano parametrai
    t.setup(600, 600, 10, 70)
    t.tracer(False)
    t.bgcolor("SkyBlue1")
    t.hideturtle()
    t.title("Kryžiukai-nuliukai")
    # Nusipiešti žaidimo lentos linijoms
    t.pensize(5)
    for i in (-100, 100):
        t.up()
        t.goto(i, -300)
        t.down()
        t.goto(i, 300)
        t.up()
        t.goto(-300, i)
        t.down()
        t.goto(300, i)
        t.up()

    # Funkcija žaidimo laimėtojui nustatyti
    def win_game():
        win = False
        if '1' in occupied[turn] and '2' in occupied[turn] and '3' in occupied[turn]:
            win = True
        if '4' in occupied[turn] and '5' in occupied[turn] and '6' in occupied[turn]:
            win = True
        if '7' in occupied[turn] and '8' in occupied[turn] and '9' in occupied[turn]:
            win = True
        if '1' in occupied[turn] and '4' in occupied[turn] and '7' in occupied[turn]:
            win = True
        if '2' in occupied[turn] and '5' in occupied[turn] and '8' in occupied[turn]:
            win = True
        if '3' in occupied[turn] and '6' in occupied[turn] and '9' in occupied[turn]:
            win = True
        if '1' in occupied[turn] and '5' in occupied[turn] and '9' in occupied[turn]:
            win = True
        if '3' in occupied[turn] and '5' in occupied[turn] and '7' in occupied[turn]:
            win = True
        return win

    # Funkcija nusipiešti apkritimą reikiamame langelyje
    def mark_cell(x, y):
        # Globalūs kintamieji
        global turn, rounds, validinputs

        # Apskaičiuoti langelio numerį pagal x ir y reikšmes
        if -300 < x < 300 and -300 < y < 300:
            col = int((x + 500) // 200)
            row = int((y + 500) // 200)
            # Langelio numerio pavertimas į string
            cellnumber = str(col + (row - 1) * 3)
        else:
            print('spustelėjote už žaidimo lentos ribų')

        # Patikrinti ar veiksmas valid
        if cellnumber in validinputs:
            # Nueiti į reikiamą langelį ir padėti apskritimą
            t.up()
            t.goto(cellcenter[cellnumber])
            t.dot(180, turn)
            t.update()

            # Pridėti ėjimą į occupied list'ą
            occupied[turn].append(cellnumber)
            # Išimti neleistinus ėjimus ateičiai
            validinputs.remove(cellnumber)
            # Patikrinti ar žaidėjas laimėjo
            if win_game() == True:
                # Jei laimėjo užbaigti žaidimą
                validinputs = []
                messagebox.showinfo("End Game", f"Sveikinimai {turn} žaidėjui, Tu laimėjai!")
                t.exitonclick()
            # Jei visi langeliai užimti ir niekas nelaimėjo skelbti lygiąsias
            elif rounds == 9:
                messagebox.showinfo("Tie Game", "Žaidimo pabaiga, lygiosios!")
                t.exitonclick()
            # Raundų skaičiavimui
            rounds += 1
            # Ėjimo eilėi parinkti
            if turn == "blue":
                turn = "white"
            else:
                turn = "blue"

            # Priminti jei ėjimas negalimas
        else:
            messagebox.showerror("Error", "Negalimas ėjimas!")

    # Bind'inti pelės paspaudimą į the mark_cell() funkciją
    t.onscreenclick(mark_cell)
    t.listen()
    t.done()


# Dictionary sumapinti langelių numeriams su koordinatėmis
cellcenter = {'1': (-200, -200), '2': (0, -200), '3': (200, -200),
              '4': (-200, 0), '5': (0, 0), '6': (200, 0),
              '7': (-200, 200), '8': (0, 200), '9': (200, 200)}
# Mėlynas pradeda
turn = "blue"
# Skaičiuoti kiek raundų sužaista
rounds = 1
# Galimų ėjimų listo sukūrimui
validinputs = list(cellcenter.keys())
# Abiejų žaidėjų atliktų ėjimų dictionary
occupied = {"blue": [], "white": []}

if __name__ == "__main__":
    main()