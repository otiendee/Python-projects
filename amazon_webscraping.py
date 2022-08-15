import gmail as gmail
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


url = 'https://www.amazon.com/BISSELL-SpotClean-Portable-Cleaner-2458/dp/B07D46SQ63/ref=sr_1_3?keywords=bissell+spotclean+pet+pro&qid=1660503680&sprefix=bissels%2Caps%2C2700&sr=8-3'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
           "Accept-Language":"en-US,en;q=0.5"
           }
page = requests.get(url, headers=headers)

page_items = page.text

soup = BeautifulSoup(page_items, "lxml")

prices = soup.find(class_= "a-offscreen")
for p in prices:
    price_string = p.getText()
#print(price_string)

price_string_with_no_dollar = price_string.split("$")[1]
price_float = float(price_string_with_no_dollar)
print(price_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

buying_price = 190
my_email = 'xxx@yahoo.com'
password = 'xxx'
if price_float < buying_price:
    message = f"{title} is now {price_string}"

    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='xxx@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )