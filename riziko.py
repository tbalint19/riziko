import random

jatek = "y"
while jatek == "y" :

    jatek = input("Mehet a szimuláció?(y/n):")
    if jatek == "y" :

        tamadokszama = int(input("Támadó egységek száma?"))
        vedokszama = int(input("Védő egységek száma?"))

        dobas1 = random.randint(1,6)
        dobas2 = random.randint(1,6)
        dobas3 = random.randint(1,6)
        dobas4 = random.randint(1,6)
        dobas5 = random.randint(1,6)

        print( )


        if tamadokszama >3:
            tamadodobasok = [dobas1, dobas2, dobas3]
            tamadodobasok.sort()
            tamadodobasok.reverse()
            print("A támadó dobásai:", tamadodobasok[0], tamadodobasok[1], tamadodobasok[2])

        if tamadokszama == 3:
            tamadodobasok = [dobas1, dobas2]
            tamadodobasok.sort()
            tamadodobasok.reverse()
            print("A támadó dobásai:", tamadodobasok[0], tamadodobasok[1])

        if tamadokszama == 2:
            tamadodobasok = [dobas1,]
            tamadodobasok.sort()
            tamadodobasok.reverse()
            print("A támadó dobásai:", tamadodobasok[0])

        if tamadokszama == 1:
            print("Egy egységgel nem támadhatsz!")
            tamadodobasok = []




        if vedokszama >1 :
            vedodobasok = [dobas4, dobas5]
            vedodobasok.sort()
            vedodobasok.reverse()
            if len(tamadodobasok) > 0 :

                print("A védő dobásai:", vedodobasok[0], vedodobasok[1])

        if vedokszama == 1 :
            vedodobasok = [dobas4]
            vedodobasok.sort()
            vedodobasok.reverse()
            if len(tamadodobasok) > 0 :

                print("A védő dobásai:", vedodobasok[0])

        print( )


        vesztesegA = 0
        vesztesegV = 0

        while len(vedodobasok) > 0  and len(tamadodobasok) > 0 :

            osszehasonlitandoA = max(tamadodobasok)
            osszehasonlitandoV = max(vedodobasok)

            if osszehasonlitandoA > osszehasonlitandoV :
                vesztesegV = vesztesegV + 1

            else :
                vesztesegA = vesztesegA + 1

            vedodobasok.remove(max(vedodobasok))
            tamadodobasok.remove(max(tamadodobasok))


        print("A támadó veszteségei:", vesztesegA, "--------> Megmaradó támadók száma:", tamadokszama - vesztesegA)
        print("A védő veszteségei:  ", vesztesegV, "--------> Megmaradó védők száma:  ", vedokszama - vesztesegV)

        print( )
        print( )
        print("--------------------------------------------")

    else :
        print("--------------------------------------------")
        exit()
