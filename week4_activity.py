# dictionharie4s 
# unordered changeable index
# #defined by using curly brackets
# capitals = {"kenya":"nairobi",
#             "uganda":"kampala",
#             "tanzamia":"dodma"}
# print(capitals)
# print(dir(capitals))
# print(help(capitals))
# print(len(capitals))
# print(capitals["kenya"])
# print(capitals.get["kenya"]) #will print you the value associated with kenya, so nairobi
# capitals["sputh africa"] + "pretoria"
# capitals.update({"nigeria":"abuja"})
# capitals.update({"france":"paris", "germany":"berlin"})


# if capitals.get("japan"):
#     print("that capital exists")
# else:
#     print("that capital doesnt exist")
# #depends if japan is in dictionary

capitals.update({"Germany":"berlin"}) #inserts a new key value pair
capitals.update({"kenya":"detriot"}) #updates existing key value pair
capitals.pop("uganda") #removes a key value pair in dictionary
capitals.popitem() #removes last item in the dictionary
capitals.clear() #will clear the dictionary


keys = capitals.keys()


print(capitals)

#drilling down:
my_dict ={"values_1":{"v1":3, "v2":6},"points":{"points1":9,"points2":[10.300.15]}}
print(my_dict["points"]["points2"][1])