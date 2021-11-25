def geomtery(teref):
    if len(teref)==3:
        a=teref[0]
        b=teref[1]
        c=teref[2]

        if (a+b)>c and (a+c)>b and (b+c)>a:
            if (a==b) and (a==c) and (b==c):
                print("Bərabər tərəfli üçbucaq")
            elif (a==b) and (a==c):
                print("Bərabəryanlı üçbucaq")
            else:
                print("Müxtəlif yanlı üçbucaq")
        
        else:
            print("Üçbucaq təyin olunmur")



    elif len(teref)==4:
        a=teref[0]
        b=teref[1]
        c=teref[2]
        d=teref[3]
        if a==b==c==d:
            print("Kvadrat")
        elif (a==b) and (c==d):
            print("Duzbucaqli")
        else:
            print("Çoxbucaqlı")


while (True):
    Tereflerin_sayi=int(input("Tereflerin sayini daxil edin: "))
    if (Tereflerin_sayi == 3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geomtery([a,b,c])

    elif (Tereflerin_sayi == 4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geomtery([a,b,c,d])
    
    else:
        print("Zəhmət olmasa təkrar daxil edin")
    
else:
    print("Hər hansı bir fiqur deyil")

#Gisman


