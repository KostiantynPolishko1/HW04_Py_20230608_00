import math

diagonalC = float(input("\nenter size of diagonal: "))

if diagonalC == 0:
    print("ERROR!")
else:
    sizeA = int(math.sqrt(((diagonalC**2)/2)))
    if sizeA < 2:
        print("\n\tERROR! SQUARE SIDE = {}.\n\tENTER BIGGER SIZE OF DIAGONAL".format(sizeA))
    else:
        print("square side = {}".format(sizeA))

        for i in range(0, sizeA):
            if i == 0:
                for j in range(0, sizeA):
                    print("*  ", end='')
                print()
            elif i == sizeA-1:
                for j in range(0, sizeA):
                    print("*  ", end='')
            else:
                print("*  ", end='')
                for j in range(0, sizeA-2):
                    print("   ", end='')
                print("* ")
