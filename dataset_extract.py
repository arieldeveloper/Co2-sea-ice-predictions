"""CSC110 Fall Final project: Extracting values from dataset

DESCRIPTION:
===============================

This Python module contains the program and tests described in Part 3.
You can run this file as given to see the pytest report given in the handout.
Your task is to fix all errors in this file so that each test passes
(see assignment handout for details).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of instructors and TAs
from CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) Ariel Chouminov, Oliver Laranjeira, Ram Chawla and Umayrah Chonee.
"""
# import statements
from typing import List, Tuple, Dict
import csv


def extract_co2emission_top_five(filename: str) -> Dict[int, float]:
    """Extract the total co2 emission extracted by the top five co2 emitting countries from
    1979 to 2015.

    According to https://www.ucsusa.org/resources/each-countrys-share-co2-emissions,
    the top five countries with the leading emission of co2 in 2018 were China,
    United States, India, Russian Federation and Japan.

    The return value is a dictionary, where each key-value pair corresponds to:
        - Key: Year
        - Value: The total co2 emission of China, United States, India, Russian Federation
         and Japan for that year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.

    """
    # Accumulator
    final_dict = {}

    for i in range(1979, 2016):
        final_dict[i] = 0

    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        for line in reader:
            for i in range(1979, 2016):
                if line[1] == 'China' and line[2] == str(i):
                    final_dict[i] += float(line[3])
                elif line[1] == 'United States' and line[2] == str(i):
                    final_dict[i] += float(line[3])
                elif line[1] == 'India' and line[2] == str(i):
                    final_dict[i] += float(line[3])
                elif line[1] == 'Russia' and line[2] == str(i):
                    final_dict[i] += float(line[3])
                elif line[1] == 'Japan' and line[2] == str(i):
                    final_dict[i] += float(line[3])

    return final_dict


def extract_temperatures(filename: str) -> Dict[int, float]:
    """Extract the average global temperatures from each year in the range 1979 to 2015.

    The return value is a dictionary, where each key-value pair corresponds to:
        - Key: Year
        - Value: Average Land Temperature for the corresponding year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    # accumulators
    full_dict = {}
    months_counted = {}

    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)

        for line in reader:
            full_dict[int(line[0][:4])] = 0
            months_counted[int(line[0][:4])] = 0

    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)

        for line in reader:
            if line[1] != '':
                full_dict[int(line[0][:4])] += float(line[1])
                months_counted[int(line[0][:4])] += 1

    final_dict = {x: full_dict[x] / months_counted[x] for x in range(1979, 2016)}

    return final_dict


def extract_sea_ice(filename: str) -> Dict[int, float]:
    """Extract the sea-ice index from each year in the range 1979 to 2015.

    The return value is a dictionary, where each key-value pair corresponds to:
        - Key: Year
        - Value: Sea-Ice index for the corresponding year

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    # Accumulator
    final_dict = {}

    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)

        for line in reader:
            if int(line[0]) < 2016:
                final_dict[int(line[0])] = float(line[4])

    return final_dict


def extract_list_map(filename: str, year: int) -> List[List]:
    """Extract the list of values needed for the Choropleth map.

    The return value is a list of lists. Each inner-list contains two strings and a float:
    - First string: The code of the country
    - Second string: The country name
    - Float value: CO2 emission for given year

    Preconditions:
        - filename refers to a CSV file in the exact format of the co2-data.csv file.
        - 2018 >= year >= 1979
    """
    # accumulator
    final_list = []

    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)

        for line in reader:
            # accumulator
            inner_list = []
            if line[2] == str(year) and line[0] != '':
                inner_list.append(line[0])
                inner_list.append(line[1])
                inner_list.append(float(line[3]))
                final_list.append(inner_list)

    return final_list


def make_x_y_lists(data: Dict[int, float]) -> Tuple[list, list]:
    """Turn dict of data into two lists, one containing all the keys and one
     containing all values

    Returns a tuple containing a list of all x values and a list of all y values.

    Preconditions:
        - data must be in dict format as outputted by extract_xxx functions

    >>> make_x_y_lists({2000: 10.5, 2001: 11.0, 2002: 11.5, 2003: 12.0})
    ([2000, 2001, 2002, 2003], [10.5, 11.0, 11.5, 12.0])

    """
    # Accumulators
    x_values = []
    y_values = []
    for key in data:
        x_values.append(key)
        y_values.append(data[key])

    return (x_values, y_values)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['csv', 'typing.List', 'typing.Dict', 'typing.Tuple'],
        'allowed-io': ['extract_co2emission_top_five', 'extract_temperatures',
                       'extract_sea_ice', 'extract_list_map'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
