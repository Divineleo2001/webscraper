import os
import requests
from bs4 import BeautifulSoup

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Define the URLs of the weather forecast websites or APIs you want to scrape
sources = [
    'https://openweathermap.org/',
    'https://weather.com/',
    'https://www.accuweather.com/',
    'https://www.wunderground.com/',
    'https://www.weather.gov/',
]

# Loop through each source
for source_url in sources:
    # Send an HTTP GET request to the source URL
    response = requests.get(source_url)
    html_content = response.text

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(html_content, 'html.parser')

        city_info_span = soup.find('span', {'class_': 'city-info'})

        #EXtract the city name from the nest span with the class "city-name"
        city_name_span = city_info_span.find('span', {'class_': 'city-name'})
        city_name = city_name_span.get_text(strip=True)

        temperature_span = city_info_span.span('span',{ "class_":"wu-value"})
        temperature = temperature_span.get_text(strip=True)


        # Extract data from the HTML using Beautiful Soup
        # Your scraping logic goes here for each source

        # Define a filename based on the source URL (you can customize this)
        filename = os.path.join(script_dir, source_url.split('//')[1].replace('/', '_') + '.txt')

        # Save the scraped data to a text file in the script's directory
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

        print(f'Data from {source_url} saved to {filename}')
        print(f'City: {city_name}')
        print(f'Temperature: {temperature}')

    else:
        print(f'Failed to retrieve data from {source_url}. Check the URL and your internet connection.')
