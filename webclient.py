# importing modules
import requests

# API url address
url = "http://labs.bible.org/api/?passage="

# initial interface
print("\nHello! Welcome to the Daily Bible Search! Below are a list of options for you:\n")
print("1. Enter a single verse (i.e. John 3:16)")
print("2. Enter a range of verses (i.e. Romans 10:9-10)")
print("3. Enter multiple ranges or single verses separated by a semi-colon (i.e. Mark 8:34; John 1:1-3)")
print("4. Enter \"votd\" to get the verse of the day")
print("5. Enter \"random\" to get a random Bible verse")
print("\nWhen you are ready to exit, type \"exit\"\n")

# format for output
format = "&formatting=plain"

# API interface loop
while True:
    # getting user input
    print("*" * 75)
    userInput = input("\nEnter a verse, range, multiple ranges, votd, or random (type \"exit\" to quit): ")
    print("*" * 75)
    
    # checking for exit and user input and outputting API response
    if userInput == "exit":
        print("\nInterface exiting. Thanks for using the Daily Bible Search!\n")
        print("*" * 75)
        break
    elif userInput == "random":
        response = requests.get("\n" + url + "random" + format)
        if response.status_code == 200:
            print("\n" + response.text + "\n")
        else:
            print("\nCould not connect to API. Please try again later.\n")
            print("\nInterface exiting. Thanks for using the Daily Bible Search!\n")
            print("*" * 75)
            break
    elif userInput == "votd":
        response = requests.get("\n" + url + "votd" + format)
        if response.status_code == 200:
            print("\n" + response.text + "\n")
        else:
            print("\nCould not connect to API. Please try again later.\n")
            print("\nInterface exiting. Thanks for using the Daily Bible Search!\n")
            print("*" * 75)
            break        
    else:
        response = requests.get("\n" + url + userInput + format)
        if response.status_code == 200:
            if "SQL" in response.text:
                print("\nPlease enter a valid verse. Please try again.\n")
            else:
                print("\n" + response.text + "\n")
        else:
            print("\nCould not connect to API. Please try again later.\n")
            print("\nInterface exiting. Thanks for using the Daily Bible Search!\n")
            print("*" * 75)
            break
        