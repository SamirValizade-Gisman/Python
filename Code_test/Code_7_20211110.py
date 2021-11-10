İstifadeci_adi=input("İstifadəçinin adı: ")
Parol=input("parol: ")
Cemi_uzunluq=len(İstifadeci_adi)+len(Parol)
mesaj="İstifadəçi adı və parolunuzun cəmi {} işarədən ibarətdir"
print(mesaj.format(Cemi_uzunluq))
if Cemi_uzunluq > 40:
    print("İstifadəçi adı və uzunluğunun ",
    "uzunluğu 40 işarədən artıq olmamalıdır!!!")
else:
    print(İstifadeci_adi+",","Sistemə xoş gəldiniz!",)

#GISMAN_seventh_code