# Python Reading and Writing into a file example
#
# Week 11-12, Files, Miika Nissi
import os

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

        
def read_file(file):
    with open(file, "r") as filestream:
        for line in filestream:
            cur_line = line.split(",")
            countries_list.append( Country(str(cur_line[0]), int(cur_line[1])) )

def write_file(file):
    f = open(file, "w")
    for country in countries_list:
        f.write(str(country.name) + ", " + str(country.population)+"\n")
    f.close()

countries_list = []
current_path = os.path.dirname(__file__)
country_file = os.path.join(current_path, "countries.txt")

read_file(country_file)
for country in countries_list:
    print("Country: " + str(country.name) + ", " + "Population: " + str(country.population))

countries_list.append( Country("Finland", 5540720))

write_file(country_file)
