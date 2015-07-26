import sys
from urllib2 import urlopen, URLError
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
response = requests.get('http://www.merrjep.com/list.aspx?municipality=124')

soup = BeautifulSoup(response.text, "html.parser")

def main():
    listing_results_table = soup.find("table",{"class": "listing_thumbs"})
    for row in listing_results_table.findAll("tr"):
        cell = row.select("a")

        if len(cell) > 0:
            single_link_result = requests.get('http://www.merrjep.com/' + cell[0].get('href'))
            single_link_parsed = BeautifulSoup(single_link_result.text, "html.parser")
            description = single_link_parsed.select('.auctionDescriptionContent')[0].getText()

            contact_name = single_link_parsed.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_ContactNameLabel").getText()


            phone = single_link_parsed.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_ContactTelephoneLabel").getText()


            tittle = single_link_parsed.find('span', id="ctl00_ContentPlaceHolder1_TopHeadlineLabel").getText()

            price = ""
            try:
                price = single_link_parsed.find('span', id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel1_AdPriceLabel").getText()
            except:
                price = ""

            large_image = ""

            image_results_table = single_link_parsed.select(".thumb_image")

            #print image_results_table

            result = {
                "contact_name": contact_name,
                "phone": phone,
                "titulli": tittle,
                "description": description,
                "qmimi": price,
                "imazhi": []
            }
            for image_url in image_results_table:
                result['imazhi'].append(image_url['src'])
            print result

            print "________________________________________________"

if __name__ == "__main__":
    main()