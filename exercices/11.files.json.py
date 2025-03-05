
my_dictionary = {
    "name": "John",
    "age": 30,
    "married": True,
}

my_list = [
    {
        "name": "John",
        "age": 30,
        "married": True,
    },
    {
        "name": "Jane",
        "age": 25,
        "married": False,
    },
    {
        "name": "Jack",
        "age": 40,
        "married": True,
    }
]
# The point is that we can hace that DATA written in a file... and we can read it from the file.
# To get...not the text... but the list... of dictionaries itself.

import json

with open ("some_json_data.json", "r") as my_channel:
    data = my_channel.read()
    print(type(data))

    json_data = json.loads(data)
    print(type(json_data))
    for each_item in json_data:
        print(type(each_item))
    for person in json_data:
        print(person["name"], person["age"])



print(json.dumps(my_list, indent=1))

with open ("another_json_data.json", "w") as my_channel:
    my_channel.write(json.dumps(my_list, indent=1))
