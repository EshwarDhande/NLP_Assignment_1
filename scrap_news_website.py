import requests
from bs4 import BeautifulSoup
base='https://marathi.ndtv.com/'
i=requests.get(base)
s=BeautifulSoup(i.text,"html.parser")

links=s.find_all("a")
urls= [link.get('href') for link in links]
repetition=[]
for url in urls :
    print('main')
    print(url)
    try:
        # if url[8:10]=='mr':
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            info= soup.find_all("a")
            urlsl= [link.get('href') for link in info]
            # repetition=[]
            for url_ in urlsl:
             print(url_)
             if url_[0:12]=='https://mara' and (url_ not in repetition):
                try:
                    response = requests.get(url_)
                    soup = BeautifulSoup(response.text, "html.parser")
                    info= soup.find_all("h1")
                    infop= soup.find_all("p")
                    with open("/home/llmmarathi/Pendse/15/ndtv5.txt", "a") as file:
                                for h in info:
                                        file.write(h.text.strip() + "\n")
                                for h in infop:
                                        file.write(h.text.strip() + "\n")


                    print("Data has been successfully written "+url_)
                    repetition.append(url_)
             
                except:
                 print('Skeep')
             else:
                print('Skeep due to repetition')

    except:
        print('Skeep')
