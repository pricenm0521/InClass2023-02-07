# demo.py
from pip._vendor.urllib3 import response
def demo():
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    # add another key/value pair to the dictionary
    myDictionary["Louisville"] = "Cardinals"
    print(myDictionary)
    # remove Xavier from the dictionary
    myDictionary.pop("Xavier") # alternate way to do it is del
    print(myDictionary)
    # print myDictionary, want to know the mascot for Purdue, will fail produces key error
    try:
        print(myDictionary["Purdue"])
    except: 
        # the code ends up here if an exception was thrown
        pass # easiest thing to do called eating the exception in slang terms, not a great idea most of the time
    # add error handling so this does not crash starts on line 13
    # print myDictionary, want to know the mascot for Purdue, will fail produces key error
    # iterate over the dictionary
    # print key:value in each iteration
    for key in myDictionary.keys(): # returns one key at a time
        print(key, ":", myDictionary[key])
    # convert the dictionary to a list called myList
    # cannot easily convert keys and values easily to one list
    myList = [key for key in myDictionary.keys()]
    print(myList)
    # print the values from the dictionary in a list
    myListV = [value for value in myDictionary.values()]
    print(myListV)
    # create a new dictionary called myNewDictionary with the key and value swapped
    myNewDictionary = dict((v,k) for  k,v in myDictionary.items()) # could also look like myNewDictionary = {v:k for k,v in myDictionary.items()}
    print(myNewDictionary)

    