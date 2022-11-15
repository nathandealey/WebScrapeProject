from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.investing.com/crypto/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

# The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)
table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    td = row.findAll("td")
    name = (td[2].text.strip())
    symbol = (td[3].text.strip())
    cp = (td[4].text)
    dc = (td[8].text.strip())
    cp2 = float(td[4].text.replace(",",""))
    dc2 = float(td[8].text.replace("+","").replace("%","")) / 100
    changedinprice = round((cp2+(cp2 * dc2)),4)

    print("---------------------------------------")
    print(f"Crypto Currency: {name} ")
    print(f"Symbol: {symbol}")
    print()
    print(f"Current Price: ${cp}")
    print(f"24-Hour Percent Change in Price: {dc}")
    print(f"Daily Adjusted Price: ${changedinprice}")
    print("---------------------------------------")
    print()
    print()

#for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+15134509904"

myCellPhone = "+16822017628"

for row in table_rows[1:6]:
    td = row.findAll("td")
    name = (td[2].text.strip())
    cp2 = float(td[4].text.replace(",",""))
    if name == "Bitcoin" and cp2 < 40000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="Bitcoin is below $40,000")

    if name == "Ethereum" and cp2 < 3000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="Ethereum is below $3,000")
