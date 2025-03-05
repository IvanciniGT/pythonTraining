
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

import yaml

with open ("yaml_data.yaml", "w") as my_channel:
    my_channel.write(yaml.dump(my_list, indent=1)) # In this yaml module... 
                                                   # we have a dump function instead of dumps

# With this example we have learn:
# - How to deal with yaml files...
# - How to install third party libraries

with open ("more_yaml_data.yaml", "r") as my_channel:
    raws_contents=my_channel.read() # text
    print(type(raws_contents))

    yaml_data = yaml.load(raws_contents, Loader=yaml.SafeLoader)
        # The yaml module, requires a second argument... for the load function
        # LOADER. We have several loaders... 
        # - FullLoader allows to work with the whole yaml syntax (according to the yaml specification)
        # - SafeLoader is more restrictive... it does not allow some yaml syntax

        # The YAML syntax is extremely powerful... and it allows us to do a lot of things
        # Such as encode WHOLE CLASSES in a yaml file... and then decode them back as objects.. python OBJECTS (Instances of classes)
        
    print(type(yaml_data))

    for person in yaml_data:
        print(person["name"], person["age"])