from typing import List, Tuple, Dict
import csv


def extract_co2emission_top_five(filename: str) -> Dict[int, float]:
    """Extract the total co2 emission extracted by the top five co2 emitting countries from
    1979 to 2015.

    According to https://www.ucsusa.org/resources/each-countrys-share-co2-emissions, the top five countries
    with the leading emission of co2 in 2018 were China, United States, India, Russian Federation and Japan.

    The return value is a dictionary, where each key-value pair corrsponds to:
        - Key: Year
        - Value: The total co2 emission of China, United States, India, Russian Federation and Japan for that year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        data = [row for row in reader]

    final_dict = {}

    total_china = {}
    total_us = {}
    total_india = {}
    total_russia = {}
    total_japan = {}

    for i in range(1979, 2016):
        for line in data:
            if line[1] == 'China' and line[2] == str(i):
                china_emission = float(line[3])
                total_china[i] = china_emission
            elif line[1] == 'United States' and line[2] == str(i):
                us_emission = float(line[3])
                total_us[i] = us_emission
            elif line[1] == 'India' and line[2] == str(i):
                india_emission = float(line[3])
                total_india[i] = india_emission
            elif line[1] == 'Russia' and line[2] == str(i):
                russia_emission = float(line[3])
                total_russia[i] = russia_emission
            elif line[1] == 'Japan' and line[2] == str(i):
                japan_emission = float(line[3])
                total_japan[i] = japan_emission

    for i in range(1979, 2016):
        final_dict[i] = total_china[i] + total_us[i] + total_india[i] + total_russia[i] + total_japan[i]

    return final_dict


def extract_temperatures(filename: str) -> Dict[int, float]:
    """Extract the average global temperatures from each year in the range 1979 to 2015.

    The return value is a dictionary, where each key-value pair corrsponds to:
        - Key: Year
        - Value: Average Land Temperature for the corresponding year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        data = [row for row in reader]

    full_dict = {}
    months_counted = {}

    for line in data:
        full_dict[int(line[0][:4])] = 0
        months_counted[int(line[0][:4])] = 0

    for line in data:
        if line[1] != '':
            full_dict[int(line[0][:4])] += float(line[1])
            months_counted[int(line[0][:4])] += 1

    final_dict = {x: full_dict[x]/months_counted[x] for x in range(1979, 2016)}

    return final_dict


def extract_sea_ice(filename: str) -> Dict[int, float]:
    """Extract the sea-ice index from each year in the range 1979 to 2015.

    The return value is a dictionary, where each key-value pair corrsponds to:
        - Key: Year
        - Value: Sea-Ice index for the corresponding year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        data = [row for row in reader]

    final_dict = {}

    for line in data:
        final_dict[int(line[0])] = float(line[4])

    return final_dict


def make_x_y_lists(data: Dict[int, float]) -> Tuple[list, list]:
    """Turn dict of data into two lists, one containing all the keys and one
     containing all values

    Returns a tuple containing a list of all x values and a list of all y values.

    Preconditions:
        - data must be in dict format as outputted by extract_xxx functions
    """
    x = [key for key in data]
    y = [data[key] for key in data]

    return (x, y)


def extract_list_map(filename: str, year: int) -> List[List]:
    """Extract the list of values needed for the Choropleth map.

    The return value is a list of lists. Each inner-list contains two strings and a float:
    - First string: The code of the country
    - Second string: The country name
    - Float value: CO2 emission

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        data = [row for row in reader]

    final_list = []

    for line in data:
        inner_list = []
        if line[2] == str(year) and line[0] != '':
            inner_list.append(line[0])
            inner_list.append(line[1])
            inner_list.append(float(line[3]))
            final_list.append(inner_list)

    return final_list
