import json

# some JSON:
x =  '''
    {
        "name":"John",
        "age":30,
        "city":"New York",
        "favorite_icecream_flavours": [
            "Chocolate Fudge Brownie",
            "Caramel Chew Chew"
        ]
    }
'''

# parse x:
john = json.loads(x)

# the result is a Python dictionary:
# print(john["city"]) # What would happen here?
# print(john["phone"]) # What would happen here?
# print(john["favorite_icecream_flavours"]) # What would happen here?

# What if we copied x into a variable without it being a string?