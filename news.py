import requests
from bs4 import BeautifulSoup
import sys

urlIndex = int(sys.argv[1])

urls = ["https://news.ycombinator.com",
        "https://www.tomshardware.com",
        "https://www.howtogeek.com"
       ]

URL = urls[urlIndex-1]



page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")


def HackerNews(parsedPage):
    print("")
    print("    The Latest News of Hacker News    ")
    print("")
    table = parsedPage.find("table",id="hnmain")
      
    titleLink = table.find_all("a", class_="titlelink")
      
    for link in titleLink:
        print()
        print("")
        print(" Title: ",link.text)
        print(" Link:  ",link["href"])
        print("#")
          
def HardwareNews(parsedPage):
    print()
    print("    The Latest News abou Hardware    ")    
    print()
    content = parsedPage.find("div",id="content")
    
    titleLink = content.find_all("a", class_="article-link")

    for link in titleLink:
        print()
        print("")
        print(" Title: ", link["aria-label"])
        print(" Link: ", link["href"])
        print()

def HowToGeek(parsedPage):

    print("    The Latest News of How to Geek    ")

    main = parsedPage.find("main",id="main")

    articles = main.find_all("article", class_="post")
    for article in articles:
        aTag = article.find("a")
        href = aTag["href"]
        header = article.find("header")
        headerText = header["aria-label"]
        print()
        print(" Title: ", headerText)
        print(" Link: ", href)
        print()
   


def main():
     

    try:

        if int(urlIndex-1) == 0:
            HackerNews(soup)        

        elif int(urlIndex-1) == 1:
            HardwareNews(soup)
    
        elif int(urlIndex-1) == 2:
            HowToGeek(soup)

        else:
            print("Invalid Input")
    except KeyError as err:
        print('Error:','',err)

    


if __name__ == '__main__':
    main()



  
