# How to be a Physics Pro
# Created by Team Curiosity
#Group Members:
    #   Fortes, Edgar
    #   Bito, Seth
    #   Ancheta, Viktoria

# At your service and ready to lead!

# ( Libraries )
import json, time as t, csv, random
# ======================================================================================================================
# Team's Watermark
# Got this from Viktoria's initial loading screen!

robot = r''' 
  /¯\     /¯\ 
 /   \    /  \    Fortes, Edgar   
<   |¯|    |¯| >  Bito, Seth
<   |_|  W |_| >  Ancheta, Viktoria
     |     |
'''

# Loop through the string and print each line with a delay
for line in robot.split('\n'):  # used .split to split the string!
    print(line)
    t.sleep(0.3)


# ======================================================================================================================
# =======================================================================================================================
def loading_bar():  # function for the loading bar!
    # Centering the title based on an 80-character terminal width
    print("\n" + "─── INITIALIZING ENGINE ───".center(160))

    bar_length = 40  # Bar length
    padding = " " * 56

    for letters in range(bar_length + 1):
        percent = int((letters / bar_length) * 100)
        bar = "█" * letters + "-" * (bar_length - letters)

        # \r moves the cursor to the start of the line
        # padding centers the bar visually!!!
        print(f"\r{padding}[{bar}] {percent}%", end="", flush=True)

        t.sleep(0.05)

    lift_off_message = r'''

                               SYSTEM READY. PREPARE FOR LIFTOFF.
    '''

    for letters in lift_off_message:
        print(letters, end="", flush=True)
        t.sleep(0.01)
    t.sleep(0.8)


t.sleep(.5)
loading_bar()  # loads the loading bar animation after the watermark
# =======================================================================================================================
# ======================================================================================================================
# This is the banner printer ot the title screen zone!
# This area prints an ascii art of "Gravity Pulls"
# (Text to ASCII Art Generator (TAAG), n.d.)
try:
    print()
    filename = "banner.json"
    with open(filename, "r") as file:  # got this from past codes
        # Loads the JSON data from the file
        data = json.load(file)
    # prints the data here
    for i in range(30):
        print("\n")
        t.sleep(.1)
    print(data["ascii_art"])  # prints the specific part of the data

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")

except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
# =======================================================================================================================
# =======================================================================================================================
# Subtitle Printing
message = "     With Curiosity."
for i in range(50):  # for loop to print "--" consecutively 50 times
    t.sleep(.002)
    print("-", end="")

for char in message:  # for loop
    print(char, end="", flush=True)  # typing animation
    t.sleep(0.1)  # speed of the typing


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

       This is Seth here (your 2nd dev).
       Are you ready for a fun physics journey?

       Make sure to take your time and enjoy.
       Good luck!

       Sup! This is Viktoria here (your 3rd dev)
       I hope you enjoy our cool physics code! 
       And probably, you can get a good score on your LTs instead of a 12/30.

       Have fun!!!
    '''

    for idx in welcome_message:
        print(idx, end="", flush=True)  # adds a cool typing animation
        t.sleep(0.01)  # speed of the typing
    t.sleep(5)


welcome()
for i in range(30):
    print("\n")
    t.sleep(0.1)

# =======================================================================================================================
# Authentication system for the leaderboard
# noinspection PyTypeChecker
def update_data(name, password=None, score=0, signup=False):
    try:
        with open("users.json", "r") as f:
            user_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        user_data = {}

    if signup:
        if name in user_data:
            return "exists"
        user_data[name] = {"password": password, "score": 0}

    elif name in user_data:
        user_data[name]["score"] = user_data[name].get("score", 0) + score

    else:
        return None


    with open("users.json", "w") as users:
        json.dump(user_data,users, indent=4)

    return user_data.get(name)

# log in/ sign up functions
setup = r'''
            ------ AUTHENTICATION FIRST ------
            [1] >> Log In 
            [2] >> Sign Up

'''
for i in setup:
    print(i, end="", flush=True)
    t.sleep(0.05)
t.sleep(0.3)
log_in_message = r'''
    If you have an existing account: Type "Log In", "Sign In", or "1"
    If you are brand new: Type "Sign Up", "Create", or "2"  
'''
for i in log_in_message:
    print(i, end="", flush=True)
    t.sleep(0.01)
    # authentication input

while True:
    authentication = input(" >> ").strip().lower()
    if authentication in ["1", "log in", "login", "in"]:  # LOG IN, signing in to an account made before
        while True:
            username = input("\n Name: ").lower()
            passw = input(" Password: ").lower()

            # Gets the data from the JSON
            account = update_data(username)

            if account and account.get("password") == passw:
                print("\n Login successful.")
                break
            else:
                print(" Wrong name or password. Try again!")
                print("\n" * 10)
        break

    elif authentication in ["2", "sign up", "signup", "up", "create"]:  # SIGN UP, creating a new account
        username = input(" Name: ").lower()
        passw = input("Password: ").lower()
        update_data(username, passw, signup=True)
        break

creation_message = r'''
    Your account has been created! 
    Please proceed to the code!
'''

t.sleep(0.8)
for i in creation_message:
    print(i, end="", flush=True)
    t.sleep(0.01)

    account = update_data(username)  # Load the newly created account

loginMessage = "\n*** ACCESS GRANTED ***\n"
for i in loginMessage:
    print(i, end="", flush=True)
    t.sleep(.05)


# ======================================================================================================================
# ======================================================================================================================
# =======================================================================================================================
# =======================================================================================================================

def physics_mission():
    # In this def function, the user must complete a quiz, which has questions that vary; if they get it incorrect, they lose -0.25,
    # and they are still allowed to retake the same question, which keeps repeating.
    # They choose which quarter they want to learn
    missed_questions = []

    choices = r'''
        [Q1] > Quarter 1 (Motion, Kinematics, Force, Newton's Laws, Impulse and Momentum, Conservation of Momentum)
        [Q2] > Quarter 2 (Historical Development of the Universal Law of Gravitation, Gravitational Force, Field, and Potential Energy, Acceleration due to Gravity,
                       Conservation of Mechanical Energy, Heat Transfer.)
        [Q3] > Quarter 3 (Introduction to Waves, Characteristic Behaviors of Waves, Sound as a Wave and the Physics of Echolocation, 
                       Historical Development of Ideas about Light, Colors, Wave Nature of Light, Electromagnetic Wave)
        [Q4] > Quarter 4 in Progress (Historical Development & Application of Electricity and Magnetism, Electric Charge & Charging Methods, 
                       Problem Solving in Coulomb’s Law, Voltage, Current, and Resistance, Electromagnetism, and Electrical Safety)
       '''
    print()
    print("\n" + "--- SELECT WHAT QUARTER YOU DESIRE ---".center(50))
    for index in choices:
        print(index, end="", flush=True)
        t.sleep(0.01)

    while True:
        sub_choice = input("\nSelect Quarter [1-4]: ").strip()
        if sub_choice in ["1", "2", "3", "4"]:
            quarter = f"physics_q{sub_choice}.csv"
            break
        else:
            print("[!] Invalid mission. Choose 1, 2, 3, or 4.")
    try:
        with open(quarter, mode='r', encoding='utf-8') as quarter_file:
            reader = csv.DictReader(quarter_file)
            questions = list(reader)

        if not questions:
            print("\n⚠️ Database is empty! Devs, add some questions!.")
            return

        diff = r'''
           Easy [1]      -> 5 Questions
           Medium [2]    -> 10 Questions
           Hard [3]      -> 20 Questions 
           Limitless [4] -> ? Questions
           '''
        for index in diff:
            print(index, end="", flush=True)
            t.sleep(.003)
        while True:
            try:
                difficulty = input("\n Select Difficulty [1-4]: ").strip()
                if difficulty == "1":
                    limit = 5
                    break
                elif difficulty == "2":
                    limit = 10
                    break
                elif difficulty == "3":
                    limit = 50
                    break
                elif difficulty == "4":
                    # Dynamic limit based on how many CSV lines it has
                    limit = len(questions)
                    break

            except ValueError:
                # Triggers if there is a math error or data type mismatch,,,
                print("[!] DATA ERROR: Calculation failed. Defaulting to Easy.")
                limit = 5
                break

            except KeyboardInterrupt:
                # Triggers if the user tries to force-quit (Ctrl+C),,,
                print("\n[!] MISSION ABORTED BY USER.")
                return

        random.shuffle(questions)
        selected_questions = questions[:limit]

        total_earned = 0
        potential_max = 0

        for index, q in enumerate(selected_questions, 1):
            label = q['Difficulty'].strip().title()
            if label == "Easy":
                value = 1.0
            elif label == "Medium":
                value = 2.0
            elif label == "Hard":
                value = 5.0
            else:
                value = 1.0

            potential_max += value
            current_val = value
            answered_correctly = False

            while not answered_correctly and current_val > 0:
                print(f"\n Question {index} | Potential: {current_val} pts")
                t.sleep(0.3)
                print(f"TOPIC: {q['Topic']}")
                t.sleep(0.3)
                print(f"QUESTION: {q['Question']}")
                t.sleep(0.3)

                t.sleep(0.4)
                if q.get('Choice_A'): print(f" [A] {q['Choice_A']}")
                t.sleep(0.4)
                if q.get('Choice_B'): print(f" [B] {q['Choice_B']}")
                t.sleep(0.4)
                if q.get('Choice_C'): print(f" [C] {q['Choice_C']}")
                t.sleep(0.4)
                if q.get('Choice_D'): print(f" [D] {q['Choice_D']}")

                ans = input("\nYour Answer >> ").strip().upper()

                if ans == q['Correct'].upper():
                    if q.get('Explanation'):
                        print(f"📖 Explanation: {q['Explanation']}")
                    print(f" Correct! +{current_val} points added.")
                    total_earned += current_val
                    answered_correctly = True

                else:
                    if q not in missed_questions:
                        missed_questions.append(q)

                    current_val -= 0.25
                    if current_val > 0:
                        print(f"❌ Incorrect. Penalty: -0.25. Potential now: {current_val}")
                        print("You can do it! Just think outside the box!")
                    else:
                        print(f"❌ Out of points! The answer was: {q['Correct']}.")
                        if q.get('Explanation'):
                            print(f"📖 Explanation: {q['Explanation']}")

        # Call the review page before syncing data
        review_page(missed_questions, total_earned, potential_max)

        update_data(username, score=total_earned)

    except FileNotFoundError:
        print(f"\n[❌] ERROR: '{quarter}' not found.")
        print(">>> CEO ACTION REQUIRED.")

    except Exception as error:
        print(f"\n[⚠️] UNKNOWN GLITCH: {error}")


# ======================================================================================================================
def review_page(missed_list, score, total):
    """Displays a summary of the mission and specific questions missed."""
    print("\n" + "═" * 50)
    print(" 📋  PERSONAL PERFORMANCE ".center(50))
    print("═" * 50)
    print("Make sure to review your mistakes!".center(50))

    # Calculate the percentage
    percent = (score / total * 100) if total > 0 else 0
    print(f"\n Final Result: {score:.2f} / {total:.2f} points ({percent:.1f}%)")
    print("You did amazing! Keep on trying and do your best, not only in physics but other subjects as well!")

    if not missed_list:  # If the user didn't have any mistakes
        print("\n ⭐ An AMAZING VICTORY! You answered every topic in this mission correctly.")
    else:
        print(f"\n You had some trouble with {len(missed_list)} question(s).")
        print("But that doesn't mean you suck! You just need to learn a bit better!")
        print("-" * 50)

        for indx, item in enumerate(missed_list, 1):
            print(f"\n [{indx}] TOPIC: {item['Topic']}")
            print(f"     Question: {item['Question']}")
            print(f"     ✅ Correct Answer: {item['Correct']}")
            if item.get('Explanation'):
                print(f"     💡 Review Note: {item['Explanation']}")
            t.sleep(0.4)

    print("\n" + "═" * 50)
    input(" Mission logged. Press [ENTER] to return to HQ...")


# ======================================================================================================================
# Instructions/Menu Function
def show_instructions():
    for counter in range(20):
        print("\n")
        t.sleep(0.1)

    """Explains what the program does, how to use it, and menu options."""
    instructions = r'''
   📜 PROGRAM INSTRUCTIONS & MANUAL 📜

    [Part A: What it does]

WHAT IS THIS PROGRAM?
    'Gravity Pulls With Curiosity' is a study tool built specifically
    for Grade 8 students to master Physics. It uses gamified quizzes
    to help you understand Motion, Force, Energy, and Heat Transfer.

    [Part B: How to use it]
   HOW TO USE IT:
   1. Navigation: Use the numbers [1-3] to select menu options.
   2. Quizzes: Type the letter (A, B, C, or D) of your answer.
   3. Scoring: Correct answers give full points. Mistakes have a -0.25 penalty, but you can retry until you get it right!

    # Part C: Menu Meanings
    MENU OPTIONS:
    [1] Physics Mission: Take pre-made quizzes based on school quarters.
    [2] Instructions: Opens this manual.
    [3] Exit: Safely closes the system.

    '''

    for counter in instructions:
        print(counter, end="", flush=True)
        t.sleep(0.01)

    t.sleep(6.7)


# =======================================================================================================================
def exit_message():  # exit message is printed if you want to exit the code instead of continuing.
    exitm = r'''
    Come back next time! As your fellow devs and fellow schoolmates, we entrust you to comeback for a brighter day and a better physics grade'''
    for idx in exitm:
        print(idx, end="", flush=True)
        t.sleep(.1)

# =======================================================================================================================
def return_to_menu():
    print("\n" + "—" * 38)
    input("Mission complete! Press [ENTER] to return to HQ...")
    print("\n" * 30)  # "Clears" the screen for a clear menu


# =======================================================================================================================
def main_menu():

    choices = r'''
    [1] > Launch Physics Mission
    [2] > Menu/Instructions
    [3] > Exit System
    '''
    for index in choices:
        print(index, end="", flush=True)
        t.sleep(0.01)  # speed of the typing

    print("\n " + "—" * 38)

    while True:
        #
        choice = input(" Select >> ").strip().lower()

        # Check for numbers or keywords
        if choice in ["1", "launch", "mission", "physics"]:
            return "1"
        elif choice in ["2", "menu", "instructions", "help"]:
            return "2"
        elif choice in ["3", "exit", "quit", "stop"]:
            return "3"
        else:
            print("[!] Invalid selection. Please type the number or the menu name.")

# ============================================================================================================================================
# --- Execution ---
# main menu!
header_art = r'''
               .--.                   .---.
          .---|__|           .-.      |~~~|
       .--|===|--|_         |_|      |~~~|--.
       |  |===|  |'\     .---!~|  .--|   |--|
       |%%|   |  |.'\    |===| |--|%%|   |  |
       |%%|   |  |\.'\   |   | |__|  |   |  |
       |  |   |  | \  \  |===| |==|  |   |  |
       |  |   |__|  \.'\ |   |_|__|  |~~~|__|
       |  |===|--|   \.'\|===|~|--|%%|~~~|--|
       ^--^---'--^    `-'`---^-^--^--^---'--'

          __...--~~~~~-._   _.-~~~~~--...__
        //                `V'                \\ 
       //                  |                  \\ 
      //__...--~~~~~~-._   |   _.-~~~~~~--...__\\ 
     //__.....----~~~~._\  |  /_.~~~~----.....__\\
    ====================\\ | //====================
                         `---`
    :'######:::'########:::::'###::::'##::::'##:'####:'########:'##:::'##::::'########::'##::::'##:'##:::::::'##::::::::'######::
    '##... ##:: ##.... ##:::'## ##::: ##:::: ##:. ##::... ##..::. ##:'##::::: ##.... ##: ##:::: ##: ##::::::: ##:::::::'##... ##:
     ##:::..::: ##:::: ##::'##:. ##:: ##:::: ##:: ##::::: ##:::::. ####:::::: ##:::: ##: ##:::: ##: ##::::::: ##::::::: ##:::..::
     ##::'####: ########::'##:::. ##: ##:::: ##:: ##::::: ##::::::. ##::::::: ########:: ##:::: ##: ##::::::: ##:::::::. ######::
     ##::: ##:: ##.. ##::: #########:. ##:: ##::: ##::::: ##::::::: ##::::::: ##.....::: ##:::: ##: ##::::::: ##::::::::..... ##:
     ##::: ##:: ##::. ##:: ##.... ##::. ## ##:::: ##::::: ##::::::: ##::::::: ##:::::::: ##:::: ##: ##::::::: ##:::::::'##::: ##:
    . ######::: ##:::. ##: ##:::: ##:::. ###::::'####:::: ##::::::: ##::::::: ##::::::::. #######:: ########: ########:. ######::
    :......::::..:::::..::..:::::..:::::...:::::....:::::..::::::::..::::::::..::::::::::.......:::........::........:::......::: 

        '''

# Printing the art line by line for a "loading" effect
for line in header_art.split('\n'):
    print(line)
    t.sleep(0.03)

while True:
    user_choice = main_menu()
    # Handle the choice  ==============================================================================================================
    # Using a single loop ensures the user can keep choosing options until they hit option '3'
    if user_choice == "1":
        physics_mission()
        return_to_menu()

    elif user_choice == "2":
        show_instructions()
        return_to_menu()

    elif user_choice == "3":
        # Exit the program
        exit_message()
        break
# =======================================================================================================================
# =======================================================================================================================
# ============================================================================================================================================
# =======================================================================================================================
# =======================================================================================================================
