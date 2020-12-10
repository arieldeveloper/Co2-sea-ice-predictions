import plotly.graph_objects as go
from typing import List, Tuple
import csv


def extract_co2emission_top_five(filename: str) -> List[Tuple[int, float]]:
    """Extract the total co2 emission extracted by the top five co2 emitting countries from
    1979 to 2015.

    According to https://www.ucsusa.org/resources/each-countrys-share-co2-emissions, the top five countries
    with the leading emission of co2 in 2018 were China, United States, India, Russian Federation and Japan.

    The return value is a list of tuples, where each tuple corrsponds to:
        - First element: The year
        - Second element: The total co2 emission of China, United States, India, Russian Federation and Japan.

    Preconditions:
        - filename refers to a CSV file in the format specified in the written report.
    """
    breakpoint()
    with open(filename) as file:
        reader = csv.reader(file)
        # skip header row
        next(reader)
        data = [row for row in reader]

    final_list = []

    total_china = []
    for i in range(0, 37):
        for line in data:
            if line[0] == 'CHN' and line[2] == str(i + 1979):
                china_emission = float(line[3])
                total_china.append(china_emission)

    total_us = []
    for i in range(1979, 2016):
        for line in data:
            if line[1] == 'United States' and line[2] == str(i):
                us_emission = float(line[3])
                total_us.append(us_emission)

    total_india = []
    for i in range(1979, 2016):
        for line in data:
            if line[1] == 'India' and line[2] == str(i):
                india_emission = float(line[3])
                total_india.append(india_emission)

    total_russia = []
    for i in range(1979, 2016):
        for line in data:
            if line[1] == 'Russia' and line[2] == str(i):
                russia_emission = float(line[3])
                total_russia.append(russia_emission)

    total_japan = []
    for i in range(1979, 2016):
        for line in data:
            if line[1] == 'Japan' and line[2] == str(i):
                japan_emission = float(line[3])
                total_japan.append(japan_emission)

    for i in range(0, 37):
        final_list.append((i + 1979, total_china[i] + total_us[i] + total_india[i] + total_russia[i]
                           + total_japan[i]))

    return final_list
