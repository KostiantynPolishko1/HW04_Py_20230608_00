import math

diagonalC = float(input("\nenter size of diagonal: "))

if diagonalC == 0:
    print("ERROR!")
else:
    sizeA = int(math.sqrt(((diagonalC**2)/2)))
    if sizeA < 2:
        print("\n\tERROR! SQUARE SIDE = {}.\n\tENTER BIGGER SIZE OF DIAGONAL".format(sizeA))
    else:
        print("square side = {}\n".format(sizeA))

        for i in range(0, sizeA):
            ind = 0

            #TOP
            if i < sizeA / 2:

                if i == 0:
                    #top first hor. line
                    for j in range(0, sizeA):
                        print("*  ", end='')
                    print()
                else:
                    # normal diagonal
                    ind3 = 0
                    for j in range(0, i):
                        if j == 0:
                            print("*  ", end='')
                            ind += 1
                        else:
                            print("   ", end='')
                            ind += 1
                            ind3 += 1
                    print("*  ", end='')
                    ind += 1
                    ind2 = ind
                    # opposite diagonal
                    for j in range(0, sizeA - ind - i - 1):
                        print("   ", end='')
                        ind2 += 1
                    if sizeA % 2 != 0:
                        if i < sizeA / 2 - 1:
                            print("*  ", end='')
                            n = ind2
                            for k in range(n, sizeA-1):
                                if k == sizeA-2:
                                    print("*")
                                else:
                                    print("   ", end='')
                        else:
                            for k in range(n, sizeA):
                                if k == sizeA-1:
                                    print("*", end='')
                                else:
                                    print("   ", end='')
                    else:
                        print("*  ", end='')
                        for n1 in range(0, ind3):
                            print("   ", end='')
                        print("*")

            #BOTTOM
            if i >= sizeA / 2:

                if i == sizeA-1:
                    #bottom last hor. line
                    if sizeA % 2 != 0:
                        print()
                    for j in range(0, sizeA):
                        print("*  ", end='')
                    print()
                else:
                    ind4 = 0
                    if sizeA % 2 != 0:
                        print()
                    for j in range(0, sizeA - 1 - i):
                        if j == 0:
                            print("*  ", end='')
                            ind += 1
                        else:
                            print("   ", end='')
                            ind += 1
                            ind4 += 1
                    print("*  ", end='')
                    ind += 1
                    for j in range(0, i - ind):
                        print("   ", end='')
                    if sizeA % 2 != 0:
                        print("*  ", end='')
                        for n in range(0, ind4):
                            print("   ", end='')
                        print("*  ", end='')
                    else:
                        print("*  ", end='')
                        for n2 in range(0, ind4):
                            print("   ", end='')
                        print("*")
