my_dict = {
    "tuple": (1, None, "new", True, 3.14),
    "list": [
        1,
        None,
        "new",
        True,
        3.14,
    ],
    "dict": {"one": 1, "two": None, "three": "new", "four": True, "five": 3.14},
    "set": {1, None, "new", True, 3.14},
}

# list
my_dict["list"].append("new_element")
my_dict["list"].pop(1)

# dict
my_dict["dict"]["i am a tuple"] = 'new_element'
# del my_dict["dict"]["two"]
my_dict["dict"].pop("three")


# set
my_dict["set"].add("new_element")
# my_dict["set"].pop()  # любой произовольный элемент из списка
my_dict["set"].remove(3.14)  # некий определенный элемент из списка

print(my_dict["tuple"][-1])  #выводит на экран последний элемент ‘tuple’
print(my_dict["list"])
print(my_dict["dict"])
print(my_dict["set"])
