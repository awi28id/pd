from pprint import pprint

student = {
    "name" : "mamat",
    "age" : 22,
    "gender" : "laki",
    "film" : "kartun",
}

student.pop("gender")
pprint(student)

student.popitem()
pprint(student)

student.clear()
pprint(student)