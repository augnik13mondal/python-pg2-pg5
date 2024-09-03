my_dict={
    "name":"John",
    "age": 30,
    "city":"New York"
    }

print("Dictionary items:", my_dict)
name = my_dict["name"]
age = my_dict["age"]
print("Accessed items - Name:", name, "Age:", age)
city = my_dict.get("city:", "Unknown")
country = my_dict.get("country:", "Not specified")
print("City:", city, "Country:", country)
my_dict["age"] = 31 
my_dict["city"] = "San Francisco"
print("Updated dictionary:", my_dict)
dict_length = len(my_dict)
print("Length of the dictionary:", dict_length)
