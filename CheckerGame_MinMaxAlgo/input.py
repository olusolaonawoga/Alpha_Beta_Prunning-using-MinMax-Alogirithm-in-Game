
#Function to receive selection of piece to be moved by the Human Player and checks if piece is has legitimate moves or not
def input_choose_piece(position, available_pieces=None):
    while True:
        if available_pieces:
            print(
                "Forced captures are enabled! You can only choose the highlighted figures.")

        coord = input(
            "Enter the coordinates of the piece you want to move(For example, 52 without space\nOR Enter Q or q to exit the game:")
        try:
            if coord.lower() == "Q":
                return None
            coordinate = (int(coord) // 10), (int(coord) % 10)
            field = position.get_table()[coordinate[0]][coordinate[1]]
            if available_pieces:
                if coordinate in available_pieces:
                    if position.get_white_to_move() and field.lower() == "x":
                        next_moves = position.find_valid_moves_for_piece(
                            coordinate)
                        if len(next_moves) != 0:
                            return coordinate
                        else:
                            print("Chosen piece has no available moves!")
                            continue
                    elif not position.get_white_to_move() and field.lower() == "o":
                        return coordinate
                    else:
                        print("Selection is not valid! Try again.")
            else:
                if position.get_white_to_move() and field.lower() == "x":
                    next_moves = position.find_valid_moves_for_piece(
                        coordinate)
                    if len(next_moves) != 0:
                        return coordinate
                    else:
                        print("Chosen piece has no available moves!")
                        continue
                elif not position.get_white_to_move() and field.lower() == "o":
                    return coordinate
                else:
                    print("Selection is not valid! Try again.")
        except:
            print("Invalid coordinate entered! Please try again.")



#Function to check if moves entered by the Human Player is valid
def input_choose_field(valid_moves):
    while True:
        coord = input(
            "Enter the coordinates of the piece predicted (For example, 52 without space: ")
        try:
            if coord.lower() == "x":
                return None
            coordinate = (int(coord) // 10), (int(coord) % 10)
            if coordinate not in valid_moves:
                print("Selection is not valid! Try again.")
            else:
                return coordinate
        except:
            print("Invalid coordinate! Try again.")

#Function to enable forced captures
def input_forced_moves():
    while True:
        forced = input(
            "Do you want to enable forced captures? <yes|no>:")
        try:
            if forced.lower() == "yes":
                return True
            if forced.lower() == "no":
                return False
            print("Invalid choice! Try again.")

        except:
            print("Invalid input! Try again!")