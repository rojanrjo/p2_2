import random

def pas_use():
    use= input("use: ")
    pas = input("pas: ")

    if not pas.isdigit():
        exit()

    return use, int(pas)


def gue(use):
    gues1 = random.randint(1, 100)
    hads = 5
    bord = 0
    bakht = 0

    print(f"{use} ")


    for  hads in range( hads):
        gues2 = input( { hads + 1})


        if  gues2  <   gues1:
            print("bozorgeee")
            bakht += 1
        elif  gues2  >   gues1:
            print("kocholoeeee")
            bakht += 1
        else:
            print("okiii")
            bord += 1
            break

    return bord, bakht


