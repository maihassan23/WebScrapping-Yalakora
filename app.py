import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.rentalcars.com/search-results?affiliateCode=google&coordinates=&doDay=22&doHour=10&doMinute=0&doMonth=1&doYear=2026&driversAge=30&dropCoordinates=&dropFtsType=iata&dropLocation=CAI&dropLocationIata=&dropLocationName=Cairo%20International%20Airport&ftsType=iata&gad_source=1&gclid=EAIaIQobChMI0tX89ofGhAMVoJpQBh2PPQAXEAAYAyAAEgLV8vD_BwE&label=generic%3AmdzScgnf4KMGkANFVZv*thvg%3AtyS%3Acr507740556694%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-21068310%3Alp1005390%3Ali%3Adec%3Adm%3Aws&location=CAI&locationIata=&locationName=Cairo%20International%20Airport&preflang=us&puDay=15&puHour=10&puMinute=0&puMonth=1&puYear=2026&filterCriteria_sortBy=PRICE&filterCriteria_sortAscending=true"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the relevant data
cars = soup.find_all('div', class_='car-listing')

for car in cars:
    try:
        name = car.find('h2', class_='car-name').text.strip()
        price = car.find('span', class_='price').text.strip()
        company = car.find('div', class_='supplier-name').text.strip()
        
        print(f"Car Name: {name}, Price: {price}, Company: {company}")
    except AttributeError:
        continue

response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

print(response.text)