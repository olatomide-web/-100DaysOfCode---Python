# import csv
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)


# print(data["temp"].mean())
# print(data["temp"].max())

#get data in coloumns
# print(data['condition'])
# print(data.condition)


#create a dataframe from scratch

# data_dict = {
#     'students' : ["amy", "james", "tomide"],
#     'scores' : [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import csv

data = pandas.read_csv("central_park_squirrel_data.csv")
gray_squirrels_count = [data["Primary Fur Color"] == "Gray"]
red_squirrels_count = [data["Primary Fur Color"] == "Cinnamon"]
black_squirrels_count = [data["Primary Fur Color"] == "Black"]


print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_count.csv")
