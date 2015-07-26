import sys
from urllib2 import urlopen, URLError
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
response = requests.get('http://www.merrjep.com/list.aspx?municipality=124')

soup = BeautifulSoup(response.text, "html.parser")
orat = soup.select('th')
table_body = soup.select('.listing_thumbs')

rows = soup.find('.listing_thumbs')

def main():
    table = soup.find("table",{"class": "listing_thumbs"})
    for row in table.findAll("tr"):
        cell = row.select("a")

        if len(cell) > 0:
            responsi = requests.get('http://www.merrjep.com/' + cell[0].get('href'))
            soupi = BeautifulSoup(responsi.text, "html.parser")
            description = soupi.select('.auctionDescriptionContent')
            print "Pershkrimi:" + description[0].getText()

            contact_name = soupi.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_ContactNameLabel")
            print contact_name.getText()

            phone = soupi.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_ContactTelephoneLabel")
            print phone.getText()

            titulli = soupi.find('span', id="ctl00_ContentPlaceHolder1_TopHeadlineLabel")
            print titulli.getText()

            qmimi = soupi.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_AdPriceLabel")
            if qmimi != None:
                print qmimi.getText()
            print "________________________________________________"

if __name__ == "__main__":
    main()