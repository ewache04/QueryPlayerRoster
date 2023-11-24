# Description:
# This program reads a text file and prints player bio or profile.
# The user is prompted to provide the full name of the player and jersey number.
# If all the entries are correct, the program loops through the roster and outputs the player's name that was entered.

import json  # Python package for reading text files and storing data in dictionary format
import time  # Import time
from graphics import *
from button import Button  # Import button

win = GraphWin("SEARCH RWC BASKETBALL TEAM ROSTER", 500, 500)  # Window
win.setBackground("#edf5f4")  # Window color


def heading_on_load():  # Title displayed at the top of the window
    label = Text(Point(250, 25), "SEARCH RWC BASKETBALL TEAM ROSTER")
    label.setSize(16)
    label.setTextColor("darkblue")
    label.draw(win)


def loading_background():  # Rectangle box will be displayed once application starts running, e.g., blue color
    label = Rectangle(Point(5, 150), Point(495, 490))
    label.setFill("darkblue")
    label.setOutline("green")
    label.setWidth(10)
    label.draw(win)
    body_text = Text(Point(250, 270), "Player Biography")
    body_text.setFill("white")
    body_text.setSize(36)
    body_text.draw(win)


def background_on_click():  # Rectangle box will appear once Enter is clicked
    label = Rectangle(Point(5, 150), Point(495, 490))
    label.setFill("#edf5f4")
    label.setOutline("darkblue")
    label.setWidth(3)
    label.draw(win)


# Labels for file_name
label = Text(Point(70, 55), "File Name          ")
label.draw(win)

# Labels for first_name
label = Text(Point(70, 80), "First Name         ")
label.draw(win)

# Labels for last_name
label = Text(Point(70, 105), "Last Name         ")
label.draw(win)

# Labels for jersey_number
label = Text(Point(70, 130), "Jersey Number    ")
label.draw(win)

# Entry box to set file_name
file_name = Entry(Point(250, 55), 25)
file_name.setText("basketball.txt")
file_name.draw(win)

# Entry box to set first_name
first_name = Entry(Point(250, 80), 25)
first_name.setText("Amari")
first_name.draw(win)

# Entry box to set last_name
last_name = Entry(Point(250, 105), 25)
last_name.setText("Lee")
last_name.draw(win)

# Entry box to set jersey_number
jersey_number = Entry(Point(250, 130), 25)
jersey_number.setText("1")
jersey_number.draw(win)


def get_value():  # Get all the info from the user and store it in a dictionary
    values = {}  # Empty dictionary for storing entered values
    values["file_name"] = file_name.getText()  # File name
    values["first_name"] = first_name.getText()  # First name
    values["last_name"] = last_name.getText()  # Last name
    values["jersey_number"] = jersey_number.getText()  # Jersey number
    return values


def file_name_error():  # Error message if the file name is invalid
    return "Invalid file name or directory not found"


def is_file_name_valid():  # Function to check if file name is valid

    values = get_value()  # Call function that has the info the user entered
    file_name = values["file_name"]

    try:  # Checking to make sure the file name is in the directory or folder
        file = open(file_name)
        return get_value()

    except FileNotFoundError:  # Error type
        return file_name_error()


def empty_file_error():  # Error message if the file is empty
    return "You are searching from an empty text file"


def process_text_file():  # Read file into memory

    if is_file_name_valid() == file_name_error():
        return file_name_error()

    else:

        try:
            values = is_file_name_valid()
            file_name = values["file_name"]
            file = open(file_name, "r")
            file_content = (file.read())

            if len(file_content) > 0:  # Check if the text file is empty
                return file_content

            else:
                raise Exception("empty file")
        except:
            return empty_file_error()


def convert_error():  # Error message if player info is not properly stored in the text file
    return "Please store players' info in the correct format"


def convert():  # Use the split method to separate user info

    if process_text_file() == file_name_error():  # File error
        return file_name_error()

    elif process_text_file() == empty_file_error():
        return empty_file_error()

    else:
        player_info = {}
        values = get_value()
        file_name = values["file_name"]

        try:
            with open(file_name) as file_content:
                for content in file_content:
                    key, value = content.strip().split('#')  # Items before # sign are keys, and after it are values in a list form
                    key = key.strip()  # Remove white space
                    value = value.strip()  # Remove white space
                    player_info[key] = value.split("|")  # Separate list items using | sign

            return player_info

        except:
            return convert_error()


def user_search_error():  # Error message if the user name or Jersey is invalid
    return "Player name or Jersey number is invalid."


def is_search_valid():  # Verify if the user name or Jersey is valid

    if convert() == file_name_error():  # File error
        return file_name_error()

    elif convert() == empty_file_error():
        return empty_file_error()

    elif convert() == convert_error():
        return convert_error()

    else:
        try:
            user_entry = get_value()
            first_name = user_entry["first_name"]
            last_name = user_entry["last_name"]
            jersey_number = user_entry["jersey_number"]
            full_name = first_name + " " + last_name

            data_base = convert()  # Database that contains player information
            player_id1 = data_base.copy()

            player_id2 = data_base[full_name][4]  # Use jersey number as a unique id for players

            if full_name in player_id1 and player_id2 == jersey_number:  # Check if the item searched is in the database

                for key, value in data_base.items():
                    outcome = (key, value)

                player_info = data_base[full_name]  # Access only the searched object in the database
                return player_info
            else:
                raise Exception("user_entry object was not found")

        except:
            return user_search_error()


# Function to handle errors in the player_bio() function
def player_bio_error():
    return "Error associated with player_bio"

# Function to append user info into a list
def player_bio(player_profile=[]):
    if is_search_valid() == "Invalid file name or directory not found":
        return "Invalid file name or directory not found"
    elif is_search_valid() == empty_file_error():
        return empty_file_error()
    elif is_search_valid() == convert_error():
        return convert_error()
    elif is_search_valid() == user_search_error():
        return user_search_error()
    else:
        try:
            user_entry = get_value()
            full_name = user_entry["first_name"] + " " + user_entry["last_name"]

            player_attribute = is_search_valid()

            player_profile.append(full_name)
            player_profile.append(player_attribute[0])
            player_profile.append(player_attribute[1])
            player_profile.append(player_attribute[2])
            player_profile.append(player_attribute[3])
            player_profile.append(player_attribute[4])
            player_profile.append(player_attribute[5])
            player_profile.append(player_attribute[6])
            player_profile.append(player_attribute[7])

            return player_profile[-9:]

        except:
            return player_bio_error()

# Function to wait for a couple of seconds before executing something
def loading_time(sec=0.2):
    return time.sleep(sec)

# Function to handle errors in the text_format() function
def text_format_error():
    return "Error found in text_format()"

# Function to print player profile in text format
def text_format():
    if player_bio() == "Invalid file name or directory not found":
        return "Invalid file name or directory not found"
    elif player_bio() == empty_file_error():
        return empty_file_error()
    elif player_bio() == convert_error():
        return convert_error()
    elif player_bio() == user_search_error():
        print("Player name must start with a capital letter")
        return user_search_error()
    elif player_bio() == player_bio_error():
        return player_bio_error()
    else:
        try:
            player_attribute = player_bio()

            print("\nLoading Search Result...\n")
            loading_time(0.5)

            outcome = "Player name      ==> " + player_attribute[0] + "\n"
            outcome += "Player sport     ==> " + player_attribute[1] + "\n"
            outcome += "Player position  ==> " + player_attribute[2] + "\n"
            outcome += "Player height    ==> " + player_attribute[3] + " feet\n"
            outcome += "Player weight    ==> " + player_attribute[4] + " lbs\n"
            outcome += "Player number    ==> " + player_attribute[5] + "\n"
            outcome += "Player class     ==> " + player_attribute[6] + "\n"
            outcome += "Player major     ==> " + player_attribute[7] + "\n"
            outcome += "Player country   ==> " + player_attribute[8] + "\n"
            return outcome

        except:
            return text_format_error()

# Function to handle errors in the graphics_format() function
def graphics_format_error():
    label = Text(Point(250, 370), "Error found in graphics_format()")
    label.draw(win)

# Function to display a success message in graphical format
def graphics_success_msg(heading):
    heading.setText("Search was successful")

# Function to display a failure message in graphical format
def graphics_no_success_msg():
    heading = Text(Point(250, 165), "Search was not successful")
    heading.setSize(14)
    heading.setTextColor("darkblue")
    heading.draw(win)

# Function to print player profile in graphical format
def graphics_format():
    if player_bio() == "Invalid file name or directory not found":
        graphics_no_success_msg()
        label = Text(Point(250, 270), "Invalid file name or directory not found")
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)
    elif player_bio() == empty_file_error():
        graphics_no_success_msg()
        label = Text(Point(250, 270), empty_file_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)
    elif player_bio() == convert_error():
        graphics_no_success_msg()
        label = Text(Point(250, 270), convert_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)
    elif player_bio() == user_search_error():
        graphics_no_success_msg()
        label = Text(Point(250, 270), user_search_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)

        label = Text(Point(250, 300), "Player name must start with a capital letter")
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)
    elif player_bio() == player_bio_error():
        graphics_no_success_msg()
        print(player_bio_error())
    else:
        try:
            player_attribute = player_bio()

            heading = Text(Point(250, 165), "Loading....")
            heading.setSize(14)
            heading.setTextColor("darkblue")
            heading.draw(win)

            loading_time()

            label1 = Text(Point(250, 198), "Player name      ==>  " + player_attribute[0])
            label1.draw(win)

            label2 = Text(Point(250, 228), "Player sport      ==>  " + player_attribute[1])
            label2.draw(win)

            label3 = Text(Point(250, 258), "Player position      ==>  " + player_attribute[2])
            label3.draw(win)

            label4 = Text(Point(250, 288), "Player height      ==>  " + player_attribute[3] + " feet")
            label4.draw(win)

            label5 = Text(Point(250, 318), "Player weight      ==>  " + player_attribute[4] + " lbs")
            label5.draw(win)

            label6 = Text(Point(250, 348), "Player number      ==>  " + player_attribute[5])
            label6.draw(win)

            label7 = Text(Point(250, 378), "Player class      ==>  " + player_attribute[6])
            label7.draw(win)

            label8 = Text(Point(250, 405), "Player major      ==>  " + player_attribute[7])
            label8.draw(win)

            label9 = Text(Point(250, 435), "Player country      ==>  " + player_attribute[8])
            label9.draw(win)

            graphics_success_msg(heading)

        except:
            graphics_no_success_msg(heading)
            graphics_format_error()

# Control Buttons
def submit_button():  # Submit Button
    button = Button(win, Point(430, 70), 90, 40, "Enter")
    button.activate()
    return button


def quit_button():  # Exit Button
    button = Button(win, Point(430, 115), 90, 40, "Exit")
    button.activate()
    return button


def main(active=True, separator="___" * 20):
    top_heading = heading_on_load()  # Title displayed at the top of the window
    background_on_load = loading_background()  # Rectangle box will be displayed once the application starts running
    submit_now = submit_button()  # Call button for submitting
    quit_app = quit_button()  # Button to quit app
    point_clicked = win.getMouse()  # Hide everything below until the button is clicked

    while active:  # Run the program until active is False

        if submit_now.clicked(point_clicked):
            # print(text_format())  # Print in text format
            # print(separator)  # Divider

            background_on_click()  # display this background on click
            graphics_format()  # Print in graphical format

        elif quit_app.clicked(point_clicked):
            win.close()
            active = False

        else:
            pass

        point_clicked = win.getMouse()


try:
    main()
except:
    pass

