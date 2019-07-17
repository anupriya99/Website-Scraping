from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReq(my_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")

containers = page_soup.findAll("div", {"class" : "bhgxx2 col-12-12"})
print(len(containers))
print(soup.prettify(containers[0]))

'''


container = containers[0]
price = container.findAll()
'''