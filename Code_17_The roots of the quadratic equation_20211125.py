def koktap(a,b,c):
    delta=(b*b-4*a*c)
    if (delta<0):
        print("Misalın kökləri həqiqi deyil!")
        return

    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)

    return(round(x1,2),round(x2,2))

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print("""Tənliyində boşluqları daxil edərik
{}x^2+{}x+{} kökləri tapın""".format(a,b,c))

Result=koktap(a,b,c)
print(Result)

#Gisman