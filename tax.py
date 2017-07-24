#Tax Bracket of People with Income

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen
import datetime

#Parses as HTML

def web_parse():
    #Wikipedia Tax Page
    page_url = 'https://en.wikipedia.org/wiki/Income_tax_in_the_United_States'

    #Request from Wiki
    wikiClient = uOpen(page_url)
    page_html = wikiClient.read()
    wikiClient.close()

    #Parses the page
    page_soup = soup(page_html, "html.parser")

    year = datetime.datetime.now().year
    year_id = "Marginal_tax_rates_for_" + str(year)
    header = page_soup.find("span", {"id" : year_id }).parent
    #Find the table for the current year
    table = header.next_sibling.next_sibling

    print(header)

#Organizes the data into list for tax bracket
def tax_bracket():
    for row in table.findAll("tr")
    cells = row.findAll("td")
    if len(cells) == 7:
        10% = cells[1].find(text=True)
        15% = cells[2].find(text=True)
        25% = cells[3].find(text=True)
        28% = cells[4].find(text=True)
        33% = cells[5].find(text=True)
        35% = cells[6].find(text=True)
        39.6% = cells[7].find(text=True)

if __name__ == '__main__':
    #Prints the last element of the list
    web_parse()
    print('This works!')
