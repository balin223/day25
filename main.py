import csv
import pandas
from statistics import mean

#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     temperatures = [int(i) for i in temperatures]
#
# print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temperature = int(monday.temp)
# print(monday_temperature)

# data_dict = {
#     "Family Name": ["Kara", "Bajer", "Zoe"],
#     "age": ["38", "37", "1.5"]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("Lin Family Registry.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon = data['Primary Fur Color'].value_counts()['Cinnamon']
gray = data['Primary Fur Color'].value_counts()['Gray']
black = data['Primary Fur Color'].value_counts()['Black']


data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon, gray, black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Central Park Squirrel Registry")
