# How to be a Physics Pro
# Created by Team Curiosity
'''
Group Members:
    Fortes, Edgar
    Bito, Seth
    Ancheta, Viktoria
'''
# At your service and ready to lead!

# ( Libraries )
import json
import time as t
import datetime


#=======================================================================================================================
# This is the banner printer ot the title screen zone!
# This area prints an ascii art of "Gravity Pulls"
try:
    filename = "banner.json"
    with open(filename, "r") as file:
        # Loads the JSON data from the file
        data = json.load(file)
    # prints the data here.
    print("\n"*10)
    t.sleep(0.4)
    print(data["ascii_art"])
    print("\n" * 10)

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
#=======================================================================================================================

# Menu: Options
menu_options = ()
def main_menu():
    while True:
        print("")
        print("")
        print("")
        print("")














































































'''
References:
'''



