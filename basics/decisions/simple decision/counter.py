
age = int(input("How old are you? "))
def test_function(set_age=40):
    global age
    if age >= set_age:
        print("You're older than", set_age)
    else:
        return False

if test_function() == False:
    print("You're not Old!")


