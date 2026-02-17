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
import json, time as t, csv, random, os

#=======================================================================================================================
# Loading screen
def loading_bar(): # function for the loading bar!
    print("\n--- INITIALIZING ENGINE ---") # THIS IS SO COOL
    bar_length = 40 # Bar length so that I can use this for the for loop!
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)  # divides and gets the percentage
        bar = "█" * i + "-" * (bar_length - i)

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

#======================================================================================================================
# Authentication system for the leaderboard
def update_data(name, password=None, score=0, signup=False):
    # Log in or Sign Up
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
    except:
        data = {}
    if signup:
        data[name] = {"password": password, "score": 0}
    elif name in data:
        data[name]["score"] += score

    with open("users.json", "w") as f:
        json.dump(data, f)
    return data.get(name)

print("Welcome!")
print("------ AUTHENTICATION FIRST ------")
setup = r'''
[1] >> Log In
[2] >> Sign Up
'''

for i in setup:
    print(i, end="", flush=True)
    t.sleep(0.2)
t.sleep(0.3)
t.sleep(0.6)
print("\n If you have an existing account: [1] Log In"
      "\n If you are brand new: [2] Sign Up"
      "\n\n [1] / [2]")
t.sleep(0.8)
authentication = input(" >> ")
username = input(" Name: ").lower()
passw = input("Password: ")

if authentication == "2":
    update_data(username, passw, signup=True)
    t.sleep(.4)
    print("Account created.")
    # Important: reload account data so the rest of the script can use it
    account = update_data(username)
else:
    account = update_data(username, passw)
    if not account or account.get("password") != passw:
        print("Wrong login, restart the program, try again.")
        exit()

t.sleep(.5)
print(f"\n\nLogin Successful! Welcome {username}.")

#======================================================================================================================
t.sleep(.5)
print("\n"*50)
loading_bar() #loads the loading bar animation after the watermark

#=======================================================================================================================
# This is the banner printer ot the title screen zone!
# This area prints an ascii art of "Gravity Pulls"
#(Text to ASCII Art Generator (TAAG), n.d.)
try:
    print("\n"*10)
    t.sleep(.5)
    filename = "banner.json"
    with open(filename, "r") as file: # got this from past codes
        # Loads the JSON data from the file
        data = json.load(file)
    # prints the data here
    t.sleep(.5)
    print("\n"*20)
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
    
       LETS DOOOOOOOOOOO IT. 🚀  
    '''

    for i in welcome_message:
        print(i, end="", flush=True) # adds a cool typing animation
        t.sleep(0.1) # speed of the typing
welcome()
print("\n"*50)
#=======================================================================================================================


def physics_mission():
    # In this def function, the user must complete a quiz, that has questions that vary, if they get it incorrect they lose -0.25,
    # and they are still allowed to retake the same question, which keeps repeating.
    # They choose what quarter they want to learn
    choices = r'''
    [Q1] > Quarter 1 (Motion, Kinematics, Force, Newton's Laws, Impulse and Momentum, Conservation of Momentum.)
    [Q2] > Quarter 2 (Historical Development of the Universal Law of Gravitation,Gravitational Force, Field, and Potential Energy, Acceleration due to Gravity,
                   Conservation of Mechanical Energy, Heat Transfer.)
    [Q3] > Quarter 3 in Progress (True or False, Modified True or False, incoming alongside it.)
   '''
    #
    print()
    print("\n" + "--- SELECT WHAT QUARTER YOU NEED ---".center(50))  # eme
    for i in choices:
        print(i, end="", flush=True)
        t.sleep(0.01)  # speed of the typing

    try:
        sub_choice = input("\nSelect Mission [1-2]: ").strip()

        # Determine what csv file is needed, through the quarter choosing
        if sub_choice == "1":
            filename = "physics_q1.csv"
        elif sub_choice == "2":
            filename = "physics_q2.csv"
        else:
            print("\n[!] Input is wrong!. You shall now be./////////. Defaulting to Q2 Mission...")
            filename = "physics_q2.csv"

        with open(filename, mode='r', encoding='utf-8') as file:  # Using encoding='utf-8' ensures your text files...
            reader = csv.DictReader(file)
            questions = list(
                reader)  # questions, the variable acts as a list so you can see anywhere from the list list, useful for randomize

        if not questions:
            print("\n⚠️ Database is empty! Devs, add some questions!.")
            return

        # ==============================================================================================================
        # This part is basically the user choosing how many questions they want to do.
        diff = r'''
       Easy [1]      -> 5 Questions
       Medium [2]    -> 10 Questions
       Hard [3]      -> 20 Questions 
       Limitless [4] -> ? Questions
       '''
        for i in diff:
            print(i, end="", flush=True)
            t.sleep(.003)

        difficulty = input("\nSelect Difficulty [1-4]: ").strip()

        if difficulty == "1":
            limit = 5
        elif difficulty == "2":
            limit = 10
        elif difficulty == "3":
            limit = 20
        elif difficulty == "4":
            if sub_choice == "2":
                limit = random.randint(20, 95)
            else:
                limit = random.randint(20, 103)

        else:
            print("[!] Error: Defaulting to Easy mode.")
            limit = 5

        # Shuffle and Slice
        random.shuffle(questions)
        selected_questions = questions[:limit]

        # Initialize point counters
        total_earned = 0
        potential_max = 0
        # ===============================================================================================================
        for i, q in enumerate(selected_questions, 1):
            # Determine points for a specific question
            label = q['Difficulty'].strip().title()  # .title() acts just like .upper(), and .lower() but instead it
            # capitalizes the first letter, and lowers the other.
            if label == "Easy":  # if the difficulty in the
                value = 1.0
            elif label == "Medium":
                value = 2.0
            elif label == "Hard":
                value = 5.0
            else:
                value = 1.0  # Just in case an error happens

            potential_max += value  #

            current_val = value  # This will decrease with mistakes!
            answered_correctly = False

            # ===============================================================================================================

            while not answered_correctly and current_val > 0:
                # Prints this for every question!
                print(f"\n Question {i} | Potential: {current_val} pts")
                t.sleep(0.3)
                print(f"TOPIC: {q['Topic']}")
                t.sleep(0.3)
                print(f"QUESTION: {q['Question']}")
                t.sleep(0.3)
                # ===============================================================================================================
                t.sleep(0.4)
                if q.get('Choice_A'): print(f" [A] {q['Choice_A']}")
                t.sleep(0.4)
                if q.get('Choice_B'): print(f" [B] {q['Choice_B']}")
                t.sleep(0.4)
                if q.get('Choice_C'): print(f" [C] {q['Choice_C']}")
                t.sleep(0.4)
                if q.get('Choice_D'): print(f" [D] {q['Choice_D']}")
                # ===============================================================================================================
                ans = input("\nYour Answer >> ").strip().upper()

                if ans == q['Correct'].upper():
                    if q.get('Explanation'):
                        print(f"📖 Explanation: {q['Explanation']}")
                    print(f" Correct! +{current_val} points added.")
                    total_earned += current_val
                    answered_correctly = True  # This tells the while loop to stop repeating this question!

                else:
                    current_val -= 0.25  # Apply penalty
                    if current_val > 0:
                        print(f"❌ Incorrect. Penalty: -0.25. Potential now: {current_val}")
                        print("You can do it! Just think outside the box! !")
                    else:
                        print(f"❌ Out of points! The answer was: {q['Correct']}.")
                        if q.get('Explanation'):
                            print(f"📖 Explanation: {q['Explanation']}")
                        # The loop ends because current_val is no longer > 0

        # ===============================================================================================================

        # 3. Syncs to user.json, to see the pointers!

        print(f"\nYou earned {total_earned} out of {potential_max} potential points.")

        update_data(username, score=total_earned)  # update the data!


    except FileNotFoundError:
        print(f"\n[❌] ERROR: '{filename}' not found.")
        print(">>> CEO ACTION REQUIRED.")

    except Exception as e:
        print(f"\n[⚠️] UNKNOWN GLITCH: {e}")
#=======================================================================================================================
def architect_quiz():
    print()
#=======================================================================================================================
def leaderboard():
    print()
#=======================================================================================================================

#=======================================================================================================================

#=======================================================================================================================
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



