class bcolors:

    GREEN = ''
    RED = ''
    CYAN = ''
    BLACK = ''
    WHITE = ''
    BG_BLUE = ''
    BG_WHITE = ''
    BG_PINK = ''
    END = ''


#Function that prints the checkers board with the active state of the pieces
def print_table(table, selected=None, valid_moves=None):
    for i in range(len(table)):
        if i == 0:
            print("    0    1    2    3    4    5    6    7")
            print("  __________________________________________")
        for j in range(len(table[i])):
            if j == 0:
                print(i, end=" |")
            if table[i][j] == "x" or table[i][j] == "X":
                if selected and ((i, j) in selected or (i, j) == selected):
                    print(bcolors.BG_BLUE + bcolors.BLACK + " " +
                          str(table[i][j]) + " " + bcolors.END, end="  ")
                else:
                    print(bcolors.GREEN + " " +
                          str(table[i][j]) + " " + bcolors.END, end="  ")
            elif table[i][j] == "o" or table[i][j] == "O":
                if selected and ((i, j) in selected or (i, j) == selected):
                    print(bcolors.BG_BLUE + bcolors.BLACK + " " +
                          str(table[i][j]) + " " + bcolors.END, end="  ")
                else:
                    print(bcolors.RED + " " +
                          str(table[i][j]) + " " + bcolors.END, end="  ")

            elif valid_moves and (i, j) in valid_moves:
                print(bcolors.BG_WHITE + bcolors.BLACK + str(i) +
                      " " + str(j) + bcolors.END, end="  ")
            else:
                if selected and ((i, j) in selected or (i, j) == selected):
                    print(bcolors.BG_PINK + bcolors.BLACK + " " +
                          str(table[i][j]) + " " + bcolors.END, end="  ")
                else:
                    print(" " + str(table[i][j]) + " ", end="  ")
        print("| " + str(i))
    print("  ------------------------------------------")
    print("    0    1    2    3    4    5    6    7")