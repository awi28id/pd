from pprint import pprint

student = {
    "name" : "mamat",
    "age" : 22,
    "is_completed" : True,
    "hobbies" : ['makan', 'minum', 'nafas']
}

name = student["name"]
age = student.get("age")

print(name)
print(age)

all_keys = student.keys()
all_values = student.values()

all_items = student.items()

print(f"keys: {all_keys}")
print(f"values: {all_values}")
print(f"items: {all_items}")

