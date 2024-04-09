### Imports modules needed to run script

# Used to exit program
import sys
# Used to run external commands
import subprocess
# Used to obtain system paths
import os

### Series of functions that script uses to operate

# Function that welcomes user to the program upon startup
def welcome_handler():
    # Prints ASCII art display
    print(r"     ___           ___                    ___           ___           ___           ___")
    print(r"    /\  \         |\__\                  /\  \         /\  \         /\  \         /\__\\")
    print(r"   /::\  \        |:|  |                /::\  \       /::\  \       /::\  \       /::|  |")
    print(r"  /:/\:\  \       |:|  |               /:/\ \  \     /:/\:\  \     /:/\:\  \     /:|:|  |")
    print(r" /::\~\:\  \      |:|__|__            _\:\~\ \  \   /:/  \:\  \   /::\~\:\  \   /:/|:|  |__")
    print(r"/:/\:\ \:\__\     /::::\__\          /\ \:\ \ \__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/ |:| /\__\\")
    print(r"\/__\:\/:/  /    /:/~~/~             \:\ \:\ \/__/ \:\  \  \/__/ \/__\:\/:/  / \/__|:|/:/  /")
    print(r"     \::/  /    /:/  /                \:\ \:\__\    \:\  \            \::/  /      |:/:/  /")
    print(r"      \/__/     \/__/                  \:\/:/  /     \:\  \           /:/  /       |::/  /")
    print(r"                                        \::/  /       \:\__\         /:/  /        /:/  /")
    print(r"                                         \/__/         \/__/         \/__/         \/__/")
    # Welcomes user to program
    print("Welcome to Py-Scan, An Nmap automation tool written in Python\n")

# Function that checks for and creates configuration directory and text file
def configuration_handler():
    ### If statements determined by whether the configuration directory and file are detected

    # Occurs when neither are detected
    if not os.path.exists(os.path.expanduser("~/pyscan_directory/")) and not os.path.exists(os.path.expanduser("~/pyscan_directory/pyscan_text.txt")):
        # Informs user that neither were detected
        print("Pyscan configuration directory and file were not detected!\n")
        # Requests user to input an absolute path for script to reference when saving results to text file
        results = input("Use absolute path to store scan results\n"
                        "Example: C:/Users/Username/Desktop/Results_Directory\n"
                        "Enter Here: ")
        # Makes the directory within the users home folder
        os.makedirs(os.path.expanduser("~/pyscan_directory/"))
        # Creates text file within the Pyscan directory and appends the user's defined path  
        with open(os.path.expanduser("~/pyscan_directory/pyscan_text.txt"), 'a') as f:
            f.write("path=" + results.strip())
    # Occurs when the directory exists but not the text file        
    elif os.path.exists(os.path.expanduser("~/pyscan_directory/")) and not os.path.exists(os.path.expanduser("~/pyscan_directory/pyscan_text.txt")):
        # Informs user that directory was found but not the text file
        print("Pyscan configuration directory was found but the text file was not detected!\n")
        # Requests user to input an absolute path for script to reference when saving results to text file
        results = input("Use absolute path to store scan results\n"
                        "Example: C:/Users/Username/Desktop/Results_Directory\n"
                        "Enter Here: ")
        # Creates text file within the Pyscan directory and appends the user's defined path
        with open(os.path.expanduser("~/pyscan_directory/pyscan_text.txt"), 'a') as f:
            f.write("path=" + results.strip())
        #with open(os.path.expanduser("~/pyscan_directory/pyscan_text.txt"), 'r') as f:
            #contents = f.read().strip()[5:]
    # Occurs when no action is required by the user
    else:
        # Passes 
        pass

# Defines the function that lists options that user can choose from
def options_handler():
    # Displays list of scan options
    print("1)TCP Scan\n"
          "2)UDP Scan\n"
          "3)Comprehensive Scan\n"
          "4)Ping\n"
          "5)Traceroute\n"
          "6)Show Options\n"
          "7)Help\n"
          "8)Configuration\n"
          "9)Exit\n")
    
# Defines the function that runs the command associated with the users choosen action  
def command_handler(command):
    # Runs the command and stores the output within a variable
    results = subprocess.run(command, capture_output=True, text=True)
    # Prints the standard output of the command
    print(results.stdout)
    # Creates space
    print("")
    # Returns to action handler function
    actions_handler()

# Defines function that allows user to choose scan function and target    
def actions_handler():
    pass

#
def export_handler():
    pass

### Runs functions in order

# Runs the welcome handler
#welcome_handler()
# Runs the configuration handler
configuration_handler()
# Runs the options handler
#options_handler()
# Runs the actions handler
#actions_handler()