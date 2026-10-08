# Atlas of Southeast Asia
from pyscript import display


countries = ["Brunei", "Cambodia", "East Timor", "Indonesia", "Laos", "Malaysia",
             "Myanmar", "Philippines", "Singapore", "Thailand", "VietNam"]

nicknames = ["The Abode of Peace", "The Kingdom of Wonder",
             "The Land of the Rising Sun of Timor", "The Emerald of the Equator",
             "The Land of a Million Elephants", "Truly Asia",
             "The Land of Golden Pagodas", "The Pearl of the Orient Seas",
             "The Lion City", "The Land of Smiles",
             "The Land of the Ascending Dragon"]


def display_title():
    print("ELEVEN NATIONS - ONE ARCHIPELAGO OF NAMES")
    print("The Nickname Atlas of Southeast Asia")
    print("Type a country to uncover the title it has been given.")
    print()


def display_nickname(user_input):
    result = "Country not found. Please try another Southeast Asian nation."

    for i in range(len(countries)):
        if countries[i].lower() == user_input.lower():
            result = "Nickname: " + nicknames[i]
            break

    print(result)


def display_footer():
    print()
    print("Seatwork 1 - 2nd Quarter | 11 nations of Southeast Asia")



display_title()
country_name = input("Enter a Southeast Asian country: ").strip()
display_nickname(country_name)
display_footer()
