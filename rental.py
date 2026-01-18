import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter Url : ")
page =requests.get(url)

def main(page) :
    src = page.content
    soup = BeautifulSoup(src , "lxml")
    cars_details=[]

    # AllData=soup.find_all('div',{'class':'SM_b848800a'})

    # print(AllData)
    # cars = soup.find_all('a',{'class' :'SM_df109d05'})
    # cars=soup.find_all('div',{'class':'SM_92786005 SM_aa35055d SM_312c83af'}).text.strip()
    # print(cars)

    # def get_cars_info(AllData):
    #
    #     cars=soup.find_all('a')
    #     print(cars[8])
    # get_cars_info(AllData)

    car_name=[name.text for name in soup.find_all('div',class_='SM_92786005')]
    print(car_name)
    car_rate=[rate.text for rate in soup.find_all('div',class_='SM_3e7a1efe SM_a81e959c')]
    print(car_rate)
    company=[image for image in soup.find_all('img',class_='SM_c6895d69 SM_50b2c943 SM_f80890e0 SM_7706a20c')]
    print(company)


main(page)