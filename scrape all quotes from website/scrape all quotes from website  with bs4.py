import requests
from bs4 import BeautifulSoup


## url of site which we scrape
url = "https://parade.com/937586/parade/life-quotes/"


## request the url to get data from that website and check status code
page = requests.get(url)
#print(page.status_code)


## call BeautifulSoup and store in soup variable
soup = BeautifulSoup(page.text,"html.parser")

#print(soup)

quote = soup.find(class_= "page_content")

#print(quote)

p_class = soup.find_all("p")
#print(p_class)
#print(len(p_class))
#print(p_class[8])

## slice from 8:161
main_p = p_class[8:161]
#print(main_p)

for i in main_p:
    print(i.text,end="\n\n")


#### Done ####
