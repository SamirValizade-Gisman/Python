import urllib.request

url1="https://upload.wikimedia.org/wikipedia/commons/3/36/Hopetoun_falls.jpg"
url2="https://scx2.b-cdn.net/gfx/news/2019/2-nature.jpg"
url3="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDjlBAvSLFtx_DxTS6Wq5aBVVJo7BHBJ4dXg&usqp=CAU"
#Sekillerin url unvanini sira ile kopyaliyiriq
urlist=[url1,url2,url3]
numb=1
#for dongusu ucun bir reqem teyin edirik ki her defe bunu yazsin
for url in urlist:
    urllib.request.urlretrieve(url,"Sekil"+str(numb)+".jpg")
    numb+=1
    #For dongusunde her novbeti ucun 1 vahid artirib basdiyir

#Gisman
