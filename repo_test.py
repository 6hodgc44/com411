def sandwich():
    ingredients = ["Bread", "Cheese", "Mayo", "Butter"]
    ingredients.append("Ham")
    return ingredients

def list_items():
    ing_list = sandwich()
    while len(ing_list) < 7:
        for i in ing_list:
            print(i)
        ing_list.append(str(input("Anything to add?")))
        for i in ing_list:
            print(i)

list_items()
