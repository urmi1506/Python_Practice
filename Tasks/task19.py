# Draw  A Game Board
size = int (input("Enter Size of Board :"))
for i in range(2 * size + 1):
    if i % 2 == 0 :
        print(" ---" * size )
    else :
        print (" |  " * (size + 1))