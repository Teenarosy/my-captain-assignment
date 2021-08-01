# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:32:43 2021

@author: Admin
"""

#project:Web scraper using Beautifulsoup4 and requests
import requests
from bs4 import Beautifulsoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore//?page="
page_num_MAX = 3
scrapped_info_list = []

for page_num in range(1,page_num_MAX):  
    req = requests.get(oyo_url + str(page_num))
    content = req.content

    soup = Beautifulsoup(content,"html.parser")

    all_hotels = soup.find_all("div",{"class":"hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_dict["address"]  = hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]  = hotel.find("span",{"class":"listingPrice__finalPrice"}).text

        try:
            hotel_dict["rating"] = hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            pass

            parent_amenities_element = hotel.find("div",{"class":"amenityWrapper"})

            ameninities_list = []
            for amenity in parent_amenities_element.find_all("div",{"class":"amenityWapper_amenity"}):
                ameninities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

            hotel_dict["amenities"] = ', '.join(ameninities_list[:-1])

            scrapped_info_list.append(hotel_dict)

            #print(hotel_name, hotel_address, hotel__price, hotel_rating, ameninities_list)

dataFrame = pandas.dataFrame(scrapped_info_list) 
dataFrame.to_csv("Oyo.csv")