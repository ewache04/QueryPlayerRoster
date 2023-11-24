
'''
Discription:

This program will meant to read a text file and pring player bio or profile
User will be ask to provide the full name of the player and jersey number
if all the entry is correct, the program will loop through the roster and output the player's
name that was entered
'''

import json #Python package for reading text file and storing it in dictionary format
import time #Import time
from graphics import*
from button import Button #Import button
win = GraphWin("SEARCH RWC BASKETBALL TEAM ROSTER",500,500) # window
win.setBackground("#edf5f4") #Window color



def heading_on_load(): #Title displayed at the top of the window
    label = Text (Point (250,25) , "SEARCH RWC BASKETBALL TEAM ROSTER")
    label.setSize(16)
    label.setTextColor("darkblue")
    label.draw(win)

def loading_background(): #Rectangle box will be displayed once application starts runing eg blue color
    label = Rectangle (Point(5,150) , Point (495,490))
    label.setFill("darkblue")
    label.setOutline("green")
    label.setWidth(10)
    label.draw(win)
    body_text = Text(Point(250,270),"Player Biography")
    body_text.setFill("white")
    body_text.setSize(36)
    body_text.draw(win)


def background_on_click(): #Rectangle box will appear once enter is cliced
    label = Rectangle (Point(5,150) , Point (495,490))
    label.setFill("#edf5f4")
    label.setOutline("darkblue")
    label.setWidth(3)
    label.draw(win)


# Labels for file_name
label = Text(Point (70,55), "File Name          ")
label.draw(win)

# Labels for first_name
label = Text(Point (70,80), "First Name         ")
label.draw(win)

#  Labels for last_name
label = Text(Point (70,105), "Last Name         ")
label.draw(win)

#  Labels for jersey_number
label = Text(Point (70,130), "Jersey Number    ")
label.draw(win)


# Entry box to Set file_name
file_name = Entry(Point (250 , 55) , 25)
file_name.setText("basketball.txt")
file_name.draw(win)

# Entry box to Set first_name
first_name = Entry(Point (250 , 80) , 25)
first_name.setText("Amari")
first_name.draw(win)

# Entry box to Set last_name
last_name = Entry(Point (250 , 105) , 25)
last_name.setText("Lee")
last_name.draw(win)


# Entry box to Set jersey_number
jersey_number = Entry(Point (250 , 130) , 25)
jersey_number.setText("1")
jersey_number.draw(win)


def get_value(): # Get all the info from user and store in dictionary
    values = {} # Empty dictioinary for storing entered values
    values["file_name"] = file_name.getText() # file_name
    values["first_name"] = first_name.getText() # first_name
    values["last_name"] = last_name.getText() # last_name
    values["jersey_number"] = jersey_number.getText() # jersey_number
    return values
        
def file_name_error(): # Error message if file name is invalid
    return "Invalid file name or directory not found"
    
def is_file_name_valid(): # Function check to see if file_name is valid
    
    values = get_value() #Call function that has the info user entered
    file_name = values["file_name"]
    
    try: # Checking to make sure file name is in the directory or folder
        file = open(file_name)
        return get_value()
       
    except FileNotFoundError: #Error type
        return file_name_error()


def empty_file_error(): # Error message if file is empty
    return "You are seraching from an empty text file"

def process_text_flie(): #Read file into memory
  
    if is_file_name_valid() == file_name_error():
        return file_name_error()
    
    else:

        try:    
            values = is_file_name_valid()
            file_name = values["file_name"]
            file = open(file_name, "r")
            file_content = (file.read())
        
            if len(file_content) > 0: # check if text file is empty
                return file_content
                
            else:
                raise Exception("empty file")
        except:
            return empty_file_error()

        
def convert_error(): #Error message if player info is not properly stored in text file
    return "Please store players info in the correct format"
        
def convert(): #Use split method to seperate user info

    if process_text_flie() == file_name_error(): # file error
        return file_name_error()
    
    elif process_text_flie() == empty_file_error():
        return empty_file_error()
    
    else:
        player_info = {}
        values = get_value()
        file_name = values["file_name"]

    
        try:
            with open(file_name) as file_content:
                for content in file_content:
                    key,value = content.strip().split('#') #items befor # sign are key and after it are values in a list form
                    key = key.strip() # remove white space
                    value = value.strip() # remove white space
                    player_info[key] = value.split("|") # Seperate list items using | sign

            return(player_info)
                                
        except:
            return convert_error()
            


def user_search_error(): #Error message if user name or Jersey is invalid
    return "Player name or Jersey number is invalid."

def is_search_valid(): # Verify if user name or Jersey is valid

    if convert() ==  file_name_error(): # file error
        return file_name_error()

    elif convert() == empty_file_error():
        return empty_file_error() 

    elif convert() == convert_error():
        return convert_error()

    else:
        try:   
            user_entry = get_value()
            first_name     = user_entry["first_name"]
            last_name      = user_entry["last_name"]
            jersey_number  = user_entry["jersey_number"] 
            full_name  = first_name + " " + last_name


            data_base = convert() # data base that contains player infomation
            palyer_id1 = data_base.copy()

            
            
            palyer_id2 = data_base[full_name][4] # use jersey number as a unique id for players

            

            if full_name in palyer_id1 and palyer_id2 == jersey_number: # Check if item searched is in data base

                #print(full_name + " was found in data base.")
                for key,value in data_base.items():
                    outcome = (key,value)
                    #print(outcome)

                player_info =  data_base[full_name] # Access only searched object in data base
                return player_info
            else:
                #print(full_name + " was not found in data base.")     
                raise Exception("user_entry object was not found")
                          
        except:
            return user_search_error()




def player_bio_error(): # encapsulate error message for if appending user info into list has issues
    return "error assosciated with player_bio"


def player_bio(player_profile = []): #Append all user info into a list
    
    
    if is_search_valid() ==  file_name_error(): # file error
        return file_name_error()

    elif is_search_valid() == empty_file_error():
        return empty_file_error()

    elif is_search_valid() == convert_error():
        return convert_error()

    elif is_search_valid() == user_search_error():
        return user_search_error()

    else:
        
        try:   
            user_entry = get_value()
            full_name  = user_entry["first_name"] + " " + user_entry["last_name"]

            player_attribute = is_search_valid() # data base that contains player infomation
            
            player_profile.append(full_name) # player full name
            player_profile.append(player_attribute[0]) # player sport
            player_profile.append(player_attribute[1]) # players position
            player_profile.append(player_attribute[2]) # players height
            player_profile.append(player_attribute[3]) # players weight
            player_profile.append(player_attribute[4]) # players number
            player_profile.append(player_attribute[5]) # players class
            player_profile.append(player_attribute[6]) # players major
            player_profile.append(player_attribute[7]) # players country

            return player_profile[-9:] # return the last player info appended
                                  
 
        except:
            return player_bio_error()


def loading_time(sec = 0.2): #wait a couple seconds before executing something
    return time.sleep(sec)


def text_format_error(): # Print error message if print text form has issues
    return "error found in text_format()"

def text_format(): #print player profile in text format

    if player_bio() ==  file_name_error(): # file error
        return file_name_error()

    elif player_bio() == empty_file_error():
        return empty_file_error()

    elif player_bio() == convert_error():
        return convert_error()

    elif player_bio() == user_search_error():
        print("Player name must start with capital later")
        return user_search_error()

    elif player_bio() == player_bio_error():
        return player_bio_error()

    else:
        try:
            
            player_attribute = player_bio()
            
            print("\nLoading Search Result...\n")
            #loading_time(0.5) #wait a couple seconds before printing next instruction
            
            outcome  = "Player name      ==> "  + player_attribute[0] + "\n"
            outcome += "Player sport     ==> "  + player_attribute[1] + "\n"
            outcome += "Player position  ==> "  + player_attribute[2] + "\n"
            outcome += "Player height    ==> "  + player_attribute[3] + "\n"
            outcome += "Player weight    ==> "  + player_attribute[4] + "\n"
            outcome += "Player number    ==> "  + player_attribute[5] + "\n"
            outcome += "Player calss     ==> "  + player_attribute[6] + "\n"
            outcome += "Player major     ==> "  + player_attribute[7] + "\n"
            outcome += "Player country   ==> "  + player_attribute[8] + "\n"
            return outcome
        
        except:
            text_format_error()

            
            
def graphics_format_error(): #Print error message in graphical format
    label = Text(Point (250,370), "Error found in graphics_format()")
    label.draw(win)


def graphics_success_msg(heading): #Print error message if everything was a success
    heading.setText("Search was successfull")
    

def graphics_no_success_msg(): #Print error message if everything was not a success
    heading = Text(Point (250,165), ("Search was not successfull"))
    heading.setSize(14)
    heading.setTextColor("darkblue")
    heading.draw(win)

def graphics_format(): #print player profile in graphics format

    if player_bio() ==  file_name_error(): # file error
        graphics_no_success_msg()
        label = Text(Point (250,270), file_name_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)

    elif player_bio() == empty_file_error():
        graphics_no_success_msg()
        label = Text(Point (250,270), empty_file_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)

    elif player_bio() == convert_error():
        graphics_no_success_msg()
        label = Text(Point (250,270), convert_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)

    elif player_bio() == user_search_error():
        graphics_no_success_msg()
        label = Text(Point (250,270), user_search_error())
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)

        label = Text(Point (250,300), "Player name must start with capital later")
        label.setSize(14)
        label.setTextColor("Red")
        label.draw(win)


    elif player_bio() == player_bio_error(): # encapsulate error message
        graphics_no_success_msg()
        print(player_bio_error())
        #label = Text(Point (250,270), player_bio_error())
        #label.setSize(14)
        #label.setTextColor("Red")
        #label.draw(win)

    else:
        try:
            
            player_attribute = player_bio()
             
            #Title ==> SEARCH RESULT FOR RWC BASKETBALL TEAM ROSTER
            heading = Text (Point (250,165) , "Loading....")
            heading.setSize(14)
            heading.setTextColor("darkblue")
            heading.draw(win)
            
            loading_time() #wait a couple seconds before printing next instruction
            
                
            #Labels for player Name
            label1 = Text(Point (250,198), "Player name      ==>  "  + player_attribute[0])
            label1.draw(win)

            #Labels for player Sport
            label2 = Text(Point (250,228), "Player sport      ==>  "  + player_attribute[1])
            label2.draw(win)

            #Labels for player Position
            label3 = Text(Point (250,258), "Player position      ==>  "  + player_attribute[2])
            label3.draw(win)

            #Labels for player Height
            label4 = Text(Point (250,288), "Player height      ==>  "  + player_attribute[3] + " feet")
            label4.draw(win)

            #Labels for player Weight
            label5 = Text(Point (250,318), "Player weight      ==>  "  + player_attribute[4] + "lbs")
            label5.draw(win)

            #Labels for player Number
            label6 = Text(Point (250,348), "Player number      ==>  "  + player_attribute[5])
            label6.draw(win)

            #Labels for player Class
            label7 = Text(Point (250,378), "Player class      ==>  "  + player_attribute[6])
            label7.draw(win)

            #Labels for player Major
            label8 = Text(Point (250,405), "Player major      ==>  "  + player_attribute[7])
            label8.draw(win)

            #Labels for player Country
            label9 = Text(Point (250,435), "Player country      ==>  "  + player_attribute[8])
            label9.draw(win)

            graphics_success_msg(heading)
        
        except:
            graphics_no_success_msg(heading)
            return graphics_format_error(heading)


#Control Buttons
def submit_button(): # Submit Button
    button = Button(win,Point (430,70) , 90, 40, "Enter")
    button.activate()
    return button


def quit_button(): # Exit Button
    button = Button(win,Point (430,115) , 90, 40, "Exit")
    button.activate()
    return button




def main(active = True, seperator = "___"*20):

    top_heading = heading_on_load() #Title displayed at the top of the window
    background_on_load = loading_background() #Rectangle box will be displayed once application starts runing
    submit_now = submit_button() #Call button for submiting
    quit_app = quit_button() #Button to quit app
    point_clicked  = win.getMouse() #Hide everything below on till button is clicked

    while active: #Run program untill active is False

        if submit_now.clicked(point_clicked):
            
            #print(text_format()) # Print in text format
            #print(seperator) # Divider

            background_on_click() # display this background on click
            graphics_format() # Print in graphical format
                         
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
