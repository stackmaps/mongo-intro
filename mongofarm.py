""" mongofarm.py

    This file presumes a running mongod instance.

    Multiple learning TODO items are listed.

    PyMongo is the Python driver for MongoDB.  
    The PyMongo docs are here:
    https://api.mongodb.com/python/current/
"""

from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["farm"]
animals = client["animals"]
print("we are using db {}".format(db.name))
print("...and collection {}".format(db.animals.name))

choice = input("\nWant to add a document? Y/n > ")
adding_data = (True if "Y" == choice else False)

if adding_data:
    db.animals.insert_one({
      "name": "Charlotte",
      "type": "spider",
      "age": 100,
      "favorite_foods": ["aphids","moths","flies"]})

print("\nLooking for data...\n")
animal = db.animals.find_one()  # returns a document or None
# my_query = {"name": "Charlotte"}
# print(my_query)
# animal = db.animals.find_one(my_query)
print(animal)


print("\nRetrieving a specific field from all documents....\n")

for item in db.animals.find():
    try:
        print(item["favorite_foods"])
    except KeyError as e:
        pass  # not all documents have `favorite_foods` key

# TODO 0
# Read this entire file and add comments explaining each line.
# BEFORE you run the file, open the mongo shell and run this command:
#           > show dbs

# Does the `farm` database exist yet?


# TODO 1
# Run the file!    
# Use the mongo shell to go see what's in the database.
#            > use farm
#            > show collections
#            > db.animals.findOne()


# TODO 2
# Un-comment lines 33-35.  Run the file.  
# Change the data loading code to add a different farm animal.
# Change the query on line 31 to retrieve the different farm animal.
# Have your new query use the `age` or `type` key (not `name`).


# TODO 3
# Try adding some data of a different format to this exact same db.
# What happens?  Does MongoDB crash?


# TODO 4
# Write a function which adds animals to the farm.  
# (specifically, it adds documents to the `animals` collection
# inside the `farm` database)
#       What's the advantage of having a function?
#       Here are a few animals you can add.
#       Note: you can create variables

# new_animal = {
#     "name": "Templeton",
#     "type": "rat",
#     "age": 4}
# db.animals.insert_one(new_animal)

# animal2 = {
#   "name": "Wilbur",
#   "type": "pig",
#   "age": 20}


# TODO 5
# Write a function which takes a dictionary as input
# and which enforces a schema on that dictionary.
# Return `True` if the dictionary has the right schema;
# return `False` otherwise.
# If the dictionary has the right schema, use your function
# from TODO 4 to add it to the database.
# Otherwise, give the user a message stating that the data
# is invalid and cannot be added to the database.


# TODO 6
# Write a function which loads data from a CSV into MongoDB.
# Use the functions you wrote in TODO 4 & 5 in order to enforce a schema.
# Feel free to continue using the Charlotte's Web example
# or devise a new example. 
# Make sure you provide human-readable error messages.


# TODO 7
# Start a standalone app, in a new file, unrelated to this one.
# Your program should be an interface to a MongoDB database.
# The program should first ask for a user ID.
# The program should serve a series of survey questions.
# The program should store survey responses in a MongoDB database.
# Respondents can opt-out of the survey partway through.
# New respondents must be prompted for a user ID.

print("\nDone.")
