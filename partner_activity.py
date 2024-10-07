Partner activity.. Names:_Abigail S, Jovanny Z.______________________________________________________
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"
school["class"]["students"]["student1"] = "A+"

Find the student who is making an A and upgrade it to an A +


 Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1

product_inventory["warehouse"]["quantities"][1]
#Sum up all the quantities in the warehouse

print(sum(product_inventory["warehouse1"]["quantities"])
      + sum(product_inventory["warehouse2"]["quantities"])


quantity1 = product_inventory["warehouse1"]["quantities"]
quantity2 = product_inventory["warehouse2"]["quantities"]
print(sum(quantity1)+sum(quantity2))