#We define how many days each month has
january = march = may = july = august = october = december = 31
april = june = september = november = 30
february = 28
#Cubic meter price of natural gas including taxes
Kubmetr_qiymeti= 0.12
#How much natural gas did the user consume per month?
Ayliq_serfiyyet=input("Aylıq təbii qaz istehlakınızı kubmetrlə daxil edin: ")
#The user wants to know which month's invoice?
dovr=input("""Hansı ayın fakturasını hesablamaq istəyirsiniz?
(Zəhmət olmasa, ayın adını kiçik hərflə və ingilis dilində daxil edin)\n""")
#Return the data from the input() function above.
#transforming it into a Python understandable format
Ay=eval(dovr)
#User's daily natural gas consumption
gunlukserfiyyet=int(Ayliq_serfiyyet)/Ay
#Bill total
Faktura=int(Kubmetr_qiymeti*gunlukserfiyyet*Ay)
print("Günlük sərfiyyatınız: \t",gunlukserfiyyet,"m3\n","təqribi faktura miqadarı: \t",Faktura,"azn", sep="")

#GISMAN_second_code