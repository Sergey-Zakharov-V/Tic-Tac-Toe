player1 = input("Первый игрок, чем вы будете играть? (0:X): ")
player2 = ""
field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
steps = 0
if player1.upper() == "X":
    player2 = "0"
else:
    player1 = "X"
    player2 = "0"
print(player1, player2)


def win():
    if(field[0] == field[1] == field[2] == player1 or
            field[3] == field[4] == field[5] == player1 or
            field[6] == field[7] == field[8] == player1 or
            field[0] == field[4] == field[8] == player1 or
            field[2] == field[4] == field[6] == player1 or
            field[0] == field[3] == field[6] == player1 or
            field[1] == field[4] == field[7] == player1 or
            field[2] == field[5] == field[8] == player1):
        draw_field()
        print("Игрок {} выйграл".format(player1))
        return False
    elif(   field[0] == field[1] == field[2] == player2 or
            field[3] == field[4] == field[5] == player2 or
            field[6] == field[7] == field[8] == player2 or
            field[0] == field[4] == field[8] == player2 or
            field[2] == field[4] == field[6] == player2 or
            field[0] == field[3] == field[6] == player2 or
            field[1] == field[4] == field[7] == player2 or
            field[2] == field[5] == field[8] == player2):
        draw_field()
        print("Игрок {} выйграл".format(player2))
        return False
    else:
        return True


def walk(player, string_):
    string_ = int(string_) - 1
    if field[string_] == " ":
        field[string_] = player


def draw_field():
    print("\n" * 100 +
          "| {} | {} | {} |\n".format(field[6], field[7], field[8]) +
          "-------------\n" +
          "| {} | {} | {} |\n".format(field[3], field[4], field[5]) +
          "-------------\n" +
          "| {} | {} | {} |\n".format(field[0], field[1], field[2]))


while win():
    draw_field()
    if " " not in field:
        break

    if steps % 2 == 0:
        walk(player1, input("Игрок {}, куда ходим?: ".format(player1)))
        steps += 1
    else:
        walk(player2, input("Игрок {}, куда ходим?: ".format(player2)))
        steps += 1
