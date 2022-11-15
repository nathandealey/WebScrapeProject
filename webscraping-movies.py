
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title
table_rows = soup.findAll("tr")

print(title.text)
##
##
##
##
'''
#for loop 
for row in table_rows[1:6]:
    td = row.findAll("td")
    movie_rank = (td[0].text)
    movie_name = (td[1].text)
    total_gross = int(td[5].text.replace("$","").replace(",",""))
    distributor = (td[9].text)

    avg_g_theatre = 


    print(movie_rank, "-", movie_name, "grossed: ", total_gross, "distributed by: ", distributor)
'''
#prof B solution

movie_rows = soup.findAll('tr')
for x in range[1:6]:
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    movie_name = td[1].text
    theatre = td[6].text.replace(",","")
    gross = int(td[7].text.replace(",","").replace("$",""))
    dis = td[9].text

    avg = gross / theatre

    print(f"Rank: {rank}")
    print(f"Movie Name: {movie_name}")
    print(f"Total Gross: ${gross:,.2f}")
    print(f"Distributor: {dis}")
    print(f"Average Per Theatre: {avg:,.2f}")
    print()
