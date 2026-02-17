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
import csv
import random

#=======================================================================================================================
# Loading screen
def loading_bar(): # function for the loading bar!
    print("\n--- INITIALIZING TEAM CURIOSITY PHYSICS ENGINE ---") # THIS IS SO COOL
    bar_length = 40 # Bar length so that I can use this for the for loop!
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)  # divides
        # Create the bar string: blocks for progress thingy thingy, spaces for the remaining to be filled up
        bar = "█" * i + "-" * (bar_length - i) # I got this coding from google but i can't remember where!

        # \r moves the cursor to the start of the line, i saw this in google iand it actually helped
        # end="" prevents a new line, so it doesnt print by columns
        print(f"\r[{bar}] {percent}%", end="", flush=True)

        t.sleep(0.05)

    print("\n\nSYSTEM READY. PREPARE FOR LIFTOFF.\n") # Double \n\n

# Cool Watermark! Got this from Viktoria's initial loading screen!
robot = r''' 
  /¯\     /¯\ 
 /   \    /  \    Fortes, Edgar   
<   |¯|    |¯| >  Bito, Seth
<   |_|  W |_| >  Ancheta, Viktoria
     |     |
'''

# Loop through the string and print each line with a delay
for line in robot.split('\n'): # used .split to split the string!
    print(line)
    t.sleep(0.3)

loading_bar() #loads the laoding bar animation after the watermark
#=======================================================================================================================
# This is the banner printer ot the title screen zone!
# This area prints an ascii art of "Gravity Pulls"
#(Text to ASCII Art Generator (TAAG), n.d.)
try:
    print("\n"*20)
    t.sleep(.5)
    filename = "banner.json"
    with open(filename, "r") as file: # got this from past codes
        # Loads the JSON data from the file
        data = json.load(file)
    # prints the data here
    t.sleep(.5)
    print("\n"*10)
    t.sleep(2)
    print(data["ascii_art"]) # prints the specific part of the data
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

#=======================================================================================================================
# Subtitle Printing
message = "     With Curiosity."
for i in range(50): # for loop to print "--" consecutively 50 times
    t.sleep(.2)
    print("--",end="" )
for char in message: # for loop
    print(char, end="", flush=True) # typing animation
    t.sleep(0.1) # speed of the typing
#=======================================================================================================================
# ======================================================================================================================
def welcome():
    # welcome message
    welcome_message = r''' 
       ✨ TEAM CURIOSITY HQ ✨
       -----------------------
       Yo! Edgar here (aka your dev). 
       We're about to make physics actually help you guys... Trust. 
    
       If the code starts acting up, 
       call the CEO (that's me btw).
    
       LETS GET IT. 🚀
    '''
    print("\n" + "  WELCOME TO THE FUTURE  ".center(50, "="))
    print(r'''
           _____  _    _  _____  _____  
          |  _  || |  | ||_   _||___  |
          | | | || |  | |  | |     / /    
          | | | || |  | |  | |    / /       
          \ \_/ /| |__| | _| |_  / /__   
           \___/  \____/ |_____||_____| 
    
    ''')
    for i in welcome_message:
        print(i, end="", flush=True) # adds a cool typing animation
        t.sleep(0.1) # speed of the typing
welcome()
print("\n"*30)
#=======================================================================================================================
def physics_mission(): # physics mission 1
    choices = r'''
     [Q1] > Quarter 1 (Motion, Kinematics, Force, Newton's Laws, Impulse and Momentum, Conservation of Momentum.)
     [Q2] > Quarter 2 (Historical Development of the Universal Law of Gravitation,Gravitational Force, Field, and Potential Energy, Acceleration due to Gravity,
                    Conservation of Mechanical Energy, Heat Transfer.)
    '''
    print("\n" + "--- SELECT YOUR CURRENT MISSION ---".center(50)) #eme
    for i in choices:
        print(i, end="", flush=True)
        t.sleep(0.01)  # speed of the typing
    try:
        sub_choice = input("\nSelect Mission [1-2]: ").strip()

        # Determining the file target
        if sub_choice == "1":
            filename = "physics_q1.csv"
        elif sub_choice == "2":
            filename = "physics_q2.csv"
        else:
            print("\n[!] Input is wrong!. You shall now be./////////. Defaulting to Q2 Mission...")
            filename = "physics_q2.csv"

        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            questions = list(reader)

        if not questions:
            print("\n⚠️ Database is empty! Edgar, add some questions!.")
            return

        difficulty = input("\nSelect Difficulty [1-4]: ").strip()

        # Mapping difficulty to question counts
        if difficulty == "1":
            limit = 5
        elif difficulty == "2":
            limit = 10
        elif difficulty == "3":
            limit = 20
        elif difficulty == "4":
            limit = random.randint(20, 30)  # Randomizes the "Limitless" vibe
        else:
            print("[!] Unknown setting. Defaulting to Easy mode.")
            limit = 5

        random.shuffle(questions)
        # Randomize for that fresh experienc
        #e
        # To be continued


    except FileNotFoundError:
        print(f"\n[❌] ERROR: '{filename}' not found.")
        print(">>> CEO ACTION REQUIRED.")

    except Exception as e:
        print(f"\n[⚠️] UNKNOWN GLITCH: {e}")

#======================================================================================================================
def architect_quiz():
    print()
#======================================================================================================================
def leaderboard():
    print()
#======================================================================================================================
def exit():
    print()
#======================================================================================================================
def main_menu():
    # main menu!
    print(" ╔════════════════════════════════════╗")
    print(" ║       TEAM CURIOSITY : OS v1.0     ║")
    print(" ╚════════════════════════════════════╝")

    choices = r'''
    [1] > Launch Physics Mission
    [2] > Access Quiz Architect
    [3] > Leaderboard
    [4] > Exit System
    '''
    for i in choices:
        print(i, end="", flush=True)
        t.sleep(0.1) # speed of the typing

    print("\n " + "—" * 38)

    choice = input(" Select >> ")
    return choice # since choice wasis an input that comes from the function, we must return the value , so that other functions could use it.

# --- Execution ---
user_choice = main_menu()

# Handle the choice
if user_choice == "1":
    print("\nLoading the quiz... Good luck!")
    physics_mission()
elif user_choice == "2":
    print("\nOpening the Quiz Maker.")
    architect_quiz()
elif user_choice == "3":
    print()
    leaderboard()
elif user_choice == "4":
    print("\nPeace out! See you next time.")
    exit()
else:
  print()

#=======================================================================================================================

#=======================================================================================================================

'''
References:
Text to ASCII Art Generator (TAAG). (n.d.). https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
Self Taught Videos for Coding:
macmostvideo. (2023, April 10). Understanding CSV files [Video]. YouTube. https://www.youtube.com/watch?v=UofTplCVkYI
Google Search. (n.d.). https://www.google.com/search?q=how+to+use+csv+notes&sca_esv=d6eb6bac57f34326&rlz=1C1BNSD_enPH1082PH1082&sxsrf=ANbL-n7Dbhx7sAttp9fJN5TlTFq4hw5Iyg%3A1771314944412&ei=AB-UafjtGIXR0-kPze_CUQ&biw=1365&bih=683&ved=0ahUKEwj47a-whuCSAxWF6DQHHc23MAoQ4dUDCBM&uact=5&oq=how+to+use+csv+notes&gs_lp=Egxnd3Mtd2l6LXNlcnAiFGhvdyB0byB1c2UgY3N2IG5vdGVzMgYQABgWGB4yCBAAGBYYChgeMgYQABgWGB4yBhAAGBYYHjIIEAAYFhgKGB4yBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFSLwWULULWMEVcAF4AZABAJgBswGgAcoGqgEDMC41uAEDyAEA-AEBmAIGoAKJB8ICChAAGLADGNYEGEfCAgsQABiABBiRAhiKBcICChAAGIAEGBQYhwLCAgUQABiABJgDAIgGAZAGCJIHAzEuNaAH6yeyBwMwLjW4B4IHwgcFMi0zLjPIBzSACAA&sclient=gws-wiz-serp
'''



