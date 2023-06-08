import math
factor = 2
B = abs(float(input("\nenter size of hor_diagonal: ")))
B = int(B/2)
H = int(B*factor)

if B == 0:
    print("ERROR!")
else:
    #top part
    print("\tver_diagonal = ", H*2)
    print("\thor_diagonal = ", B * 2)
    print("fig. ROMB")
    for i in range(0, H):
        if i % factor == 0:
            if i == 0:
                for j in range(0, (B-int(i/factor))-1):
                    print("  ", end='')
                print("x")
            elif 0 < i < H:
                for j in range(0, (B-int(i/factor))-1):
                    print("  ", end='')
                print("x", end='')

                for j in range(0, i-1):
                    print("  ", end='')
                print("x")
        else:
            print()
    #bottom part
    for i in range(0 + factor, H):
        if i % factor == 0:
            for j in range(0, int(i/factor)):
                print("  ", end='')
            print("x", end='')

            for j in range(0, (2*B-1)-2-i):
                print("  ", end='')
            if i < H-factor:
                print("x", end='')
        if i < H-1:
            print()
