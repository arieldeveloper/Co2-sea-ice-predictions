import csv
import requests

# Extracting csv dataset from this url
url = 'https://raw.githubusercontent.com/arieldeveloper/CSC110-Final/main/datasets/owid-co2-data.csv?token=ASB6CZ6QOER7EN3GIBO5CBS73KHZW'
response = requests.get(url)

with open('co2_emission_dataset.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))

# According to https://www.ucsusa.org/resources/each-countrys-share-co2-emissions, these were the top five countries
# with the leading emission of co2 in 2018: China, United States, India, Russian Federation, Japan
