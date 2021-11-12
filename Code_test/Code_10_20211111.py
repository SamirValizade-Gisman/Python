x = int(input("Qiymətiniz: "))

if x > 100 or x < 0:
    print("Belə bir nəticə yoxdur")

elif x >= 90 and x <= 100:
    print("A aldın.")

elif x >= 80 and x <= 89:
    print("B aldın.")

elif x >= 70 and x <= 79:
    print("C aldın.")

elif x >= 60 and x <= 69:
    print("D aldın.")

elif x >= 0 and x <= 59:
    print("F aldın.")