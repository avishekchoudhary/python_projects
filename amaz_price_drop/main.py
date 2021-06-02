import requests
from bs4 import BeautifulSoup
import smtplib


uri = 'https://www.amazon.in/Crucial-DDR4-Laptop-Memory-CT8G4SFRA266/dp/B08C56KXQJ/ref=sr_1_1?dchild=1&keywords=laptop+ram&qid=1618840833&sr=8-1'
header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.9'
}

response = requests.get(url=uri,headers=header)
response.raise_for_status()


soup = BeautifulSoup(response.text,'lxml')

present_price = soup.find(name='span',id='priceblock_ourprice').getText()

present_price = present_price.split("₹")[1]

present_price = present_price.split(",")#splitted over comma because u cant convert that type of str to int/float
present_price = present_price[0]+present_price[1]
print(present_price)


target_price = 4000

if float(present_price) <= target_price:
    with smtplib.SMTP('smtp.mail.yahoo.com',port=587) as connection:
        connection.starttls()
        connection.login(user='#', password='#')
        connection.sendmail(
            from_addr='#',
            to_addrs='#',
            msg=f'subject:Price Drop  \n\nHey, here the price you wanted so grab the deal ASAP.....'
        )

