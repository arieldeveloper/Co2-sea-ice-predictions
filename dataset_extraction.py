import csv
import requests

# Extracting csv dataset from this url
url = 'https://raw.githubusercontent.com/arieldeveloper/CSC110-Final/main/datasets/owid-co2-data.csv?token=ASB6CZ6QOER7EN3GIBO5CBS73KHZW'
response = requests.get(url)

url_content = response.content
csv_file = open('co2_emission_dataset.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

url = 'https://raw.githubusercontent.com/arieldeveloper/CSC110-Final/main/datasets/GlobalTemperatures.csv?token=ASB6COVWUJSSHAUIRB27S7C73PZGY'
response = requests.get(url)

url_content = response.content
csv_file = open('global_temp_dataset.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

url = 'https://raw.githubusercontent.com/arieldeveloper/CSC110-Final/main/datasets/sea_ice.csv?token=ASB6COS2NYLTHQRCIXSCWNS73PZKQ'
response = requests.get(url)

url_content = response.content
csv_file = open('sea_ice_index_dataset.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# According to https://www.ucsusa.org/resources/each-countrys-share-co2-emissions, these were the top five countries
# with the leading emission of co2 in 2018: China, United States, India, Russian Federation, Japan
