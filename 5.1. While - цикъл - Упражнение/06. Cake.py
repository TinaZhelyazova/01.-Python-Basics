length = int(input())
width = int(input())
pieces= input()
pieces_counter = 0
number_of_pieces = length * width

while True:
    if pieces == "STOP":

        print(f"{number_of_pieces} pieces are left.")
        break
    elif int(pieces) >= number_of_pieces or pieces ==0:
        pieces_needed = abs(number_of_pieces - int(pieces))
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break
    number_of_pieces -= int(pieces)
    pieces_counter += int(pieces)


    pieces = input()

