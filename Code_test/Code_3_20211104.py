import docx
import os
erize="""
                                     Tarix: {}


Azerbaycan Respublikasi
{} Universiteti
{} fakultesi dekanliğina


Fakultenizin {} qrup {} nömreli telebesiyem. elavede
qeyd olunan problemim esasinda {} tedris ili {}.
Yari rubunde tedrisimin dondurulmasini isteyiriem.
Bildirerek sizden xahis edirem.
       
           İmza:

Ad                   :{}
Soyad                :{}
Sexsiyyet Vesiqesi   :{}
Unvan                :{}
Telefon              :{}
Elektron poct        :{}
"""


Date                           =input("Tarix: ")
University                     =input("Universitetin adi: ")
Faculty                        =input("Fakulte adi: ")
Department                     =input("İxtisasin adi: " )
Student_numb                   =input("Telebenin nömresi: ")
Education_year                 =input("Tedril ili: ")
Term                           =input("Rub: ")
Name                           =input("Ad: ")
Surname                        =input("Soyad: ")
ID_cards                       =input("sexsiyyet vesiqesi: ")
Adress                         =input("unvan: ")
Phone                          =input("Telefon nömresi: ")
Email                          =input("Elektron poct unvani: ")
 
print(erize.format( Date,University,Faculty,Department,Student_numb,Education_year,Term,Name,Surname,ID_cards,Adress,Phone,Email))
doc=docx.Document()
parag=doc.add_paragraph(erize)
doc.save("Ərizə.docx")
os.system("start Ərizə.docx")

#GISMAN_third_code