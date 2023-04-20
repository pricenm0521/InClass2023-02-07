# demo01.py
# create a new module in demoPackage called demo01 done
# add a function called demo01 that accepts a dictionary as parameter
# in demo01 print the dictionary
# in the main call the function

def demo01(someDictionary):
    # if someDictionary is 0 length or null print a message but do not print the contents
    # otherwise print the contents
    # check before your do anything else: is someDictionary really a dictionary???
    if isinstance(someDictionary, dict):
        print("Thank you for providing a dictionary") 
    # another option
    if type(someDictionary) == dict:
        print("type() works too")
    if someDictionary == None or len(someDictionary) == 0:  
        print("The dictionary is empty or null")
    else:
        print(someDictionary)
    
