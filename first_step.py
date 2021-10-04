import pandas




data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()


avg = round(sum(temp_list) / len(temp_list), 2)
print(avg)
print(data["temp"].mean())

print(data["temp"].max())

#Get data in Columns
print(data["condition"])
print(data.condition)

#Get data in Row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
# # Get the temperature of Monday but converted in Fahrenheit
# print(monday.temp * 1.800 + 32)

#Create a dataframe from scratch
data_dict ={
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
