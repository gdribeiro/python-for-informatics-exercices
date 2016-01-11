"""
    Brooks Kindle <brooks.kindle@wsu.edu>
    11/3/12
    schedule.py

    Program Description: This program helps students find the right class
    schedule for their next semester. It can be hard to ensure that school
    classes don't overlap each other, so this program helps with that. Simply
    enter in the desired classes and the times that they meet and this
    program will spit out a list of possible class schedules that don't
    overlap. Choose your favorite and the schedule will be saved to a file
"""    

import sys
import os

if not os.path.isdir(os.getcwd() + "\\resources\\output"): #path doesn't exist
    os.mkdir(os.getcwd() + "\\resources\\output") #make path

if not os.path.isdir(os.getcwd() + "\\resources\\saves"): #path doesn't exist
    os.mkdir(os.getcwd() + "\\resources\\saves") #make path

#include lib folder in the path when searching for imports
sys.path.insert(0, os.getcwd() + "\\resources\\lib")

import dirChange
from _time import Time
from _course import Course
from _schedule import Schedule
from _courseList import CourseList

dirs = dirChange.DirChange() #initialize directory locations for ease of access

#############################################################################
#Main program body                                                          |
#############################################################################
def courseListMenu(courseList = CourseList()):
    """Displays the course list menu until the user wants to go back or exit.
    If no existing course list is passed in, the default course list will be
    blank (ie, a new course list)"""
    
    menu = ["Add course", "Delete course", "Save course list",
            "Display schedules", "Help", "Return to main menu", "Exit program"]

    #loop course list menu
    while True:
        choice = createMenu(menu, "Course List Menu")

        #add course
        if choice == 1:
            courseList.addSectionList(newCourse()) #add section list

        #delete course
        elif choice == 2:
            #delete course/course section from courseList
            removeCourse(courseList)

        #save course list
        elif choice == 3:
            saveCourseList(courseList)

        #display schedules
        elif choice == 4:
            schedules = courseList.getSchedules() #get the list of schedules
            displayInfo(schedules) #display the schedule information

        #display the help file
        elif choice == 5:
            displayHelp()

        #return to main menu
        elif choice == 6 and confirm():
            return

        #exit program
        elif choice == 7 and confirm(): #user confirms quitting
            exit()

def loadCourseList():
    """Displays a list of saved course lists and asks the user which one to
    load. If there are no saved course lists in the save directory, then it
    will print an error message and start a new course list for the user"""
    dirs.saves() #change directory to the saves directory
    cur = os.getcwd() #get current directory
    files = os.listdir() #get a list of the current directory
    courseListSaves = [] #list of course saves in the current directory
    
    for f in files:
        if(os.path.isfile(cur + "\\" + f) and isCourseListSave(f)):
            courseListSaves.append(f) #add file to list of course saves

    #print course list saves to the screen
    print("Course list saves:\n")
    for f in courseListSaves:
        i = f.find(".courselist")
        print(f[:i])
        
    #get desired course list file from user
    inp = input("Enter name of course list save you wish to load: ")

    #open course save file
    save = open(inp + ".courselist", "r")
    save = save.readlines()
    courseList = CourseList()
    os.chdir(inp) #change directory to course save folder
    for i in range(len(save)): #loop through lines
        save[i] = save[i].replace("\n", "") #strip newline character
        courses = getCourseList(save[i]) #get course and sections from file
        courseList.addSectionList(courses)

    dirs.root() #change directory back to the root
    
    courseListMenu(courseList) #call the courseListMenu

def newCourseList():
    """calls courseListMenu with a blank course list"""
    courseListMenu(CourseList())

def isCourseListSave(filename):
    """Returns true if the file is a course list save. False otherwise."""
    return filename[-11:].lower() == ".courselist"

def displayHelp():
    """displays the contents of the help.help file to the screen"""
    dirs.doc() #change directory to the docs directory
    file = open("help.help", "r") #open the help file for reading
    lines = file.read()
    print(lines) #print contents of the help file
    dirs.root() #change directory back to root

def displayAbout():
    """displays the contents of the about.about file to the screen"""
    dirs.doc()
    file = open("about.about", "r") #open the about file for reading
    lines = file.read()
    print(lines) #print contents of the about file
    dirs.root()

def createMenu(menu, title = "Course Scheduler Menu"):
    """creates a menu interface from an list of strings (input parameter)
    and returns the user's menu choice (provided it's a valid choice)"""
    n = len(menu) #determine number of menu options

    #create menu
    print('*' * 60)
    print(title)
    print('*' * 60)
    
    for i in range(n):
        print(i + 1, ') ', menu[i], sep = '')
    
    print('*' * 60)
    
    choice = getMenuChoice(n) #get the user's menu choice
    
    return choice #return that choice

def getMenuChoice(n):
    """prompts the user for an integer value between 1 and n and returns it.
    If the user enters an incorrect value (either not an integer or it is not
    between 1 and n), continually re-prompts the user for another value until
    a valid value is entered."""

    try:
        val = int(input("Enter choice: ")) #get user's choice
    except:
        val = -1

    invalidMsg = "Invalid Choice."
    retryMsg = "Please enter an integer value between 1 and " + str(n) + ": "
    
    while (val < 1 or val > n): #user entered invalid value
        print(invalidMsg)
        try:
            val = int(input(retryMsg)) #re-prompt for new value
        except:
            val = -1

    return val #return user's valid choice

def confirm():
    #Written by Martin Kindle
    print("Any unsaved changes will be lost.")
    c=input("Do you wish to continue (y/n)? ")
    if c.lower()=="y":
        return True
    else:
        return False

def saveCourseList(courseList):
    """saves the parameter course list and its courses to a file"""
    dirs.saves() #change directory to saves
    prompt = "Files will be saved as name.courselist\n"
    prompt += "Enter the name you wish to save the course list as: "
    name = input(prompt) #get user input
    fname = name + ".courselist"
    file = open(fname, "w") #open file for writing

    createCourseFolder(name) #create folder for course saves
    os.chdir(os.getcwd() + "\\" + name) #change directory to that folder
    
    for course in courseList.getCourseList():
        name = saveCourse(course) #save each course to a file.
        file.write(name) #write name of the section filename in the list file
        file.write("\n")
    file.close() #close file
    dirs.root() #switch directory back to root

def createCourseFolder(name):
    """creates a folder in the current directory"""
    path = os.getcwd() + "\\" + name
    exists = os.path.exists(path)
    isDir = os.path.isdir(path)
    if (not exists): #path doesn't exist
        os.mkdir(path) #create folder
    elif (exists and isDir): #folder exists already
        pass
    else: #path exists but isn't a folder
        os.remove(path) #remove conflicting file
        os.mkdir(path) #make directory

def saveCourse(sectionList):
    """saves the inputted course and its sections to a file. files will be
    saved in the format of <course name>.course. Returns the name
    of the course file"""
    courseName = sectionList[0].getName() #get the course name
    creds = sectionList[0].getCredits() #get course credits
    inst = ""
    loc = ""
    times = ""
    days = ""
    fileName = courseName + ".course"
    file = open(fileName, "w") #open file for writing
    for sect in sectionList: #iterate through each section
        #add section instructor to the string of course instructors
        inst += sect.getInstructor() + "||"

        #add section location to the string of course locations
        loc += sect.getLocation() + "||"

        #add section times to the string of course times
        start = sect.getStart().getUniversal()
        end = sect.getEnd().getUniversal()
        times += start + '-' + end + "||"

        #add section days to the string of course days
        days += sect.getDaysString() + "||"

    #remove trailing delimiter ('||')
    inst = inst[:-2]
    loc = loc[:-2]
    times = times[:-2]
    days = days[:-2]

    #write info to file
    file.write(courseName + '\n')
    file.write(inst + '\n')
    file.write(loc + '\n')
    file.write(str(creds) + '\n')
    file.write(times + '\n')
    file.write(days)
    
    #close file
    file.close()

    #return the filename
    return fileName
        
def displayInfo(schedules):
    """provides the user with a menu as to what to do with the schedule list"""
    dirs.output() #change directory to the output folder
    menuList = [displayStandard, displayUniversal,
                writeStandard, writeUniversal]
    ans = -1
    while (ans < 1 or ans > 4):
        print()
        print("1) Print schedules to screen in standard am/pm format.")
        print("2) Print schedules to screen in universal 24-hour format.")
        print("3) Write schedules to a file in standard am/pm format.")
        print("4) Write schedules to a file in universal 24-hour format.")
        try:
            ans = int(input("What would you like to do? Answer 1-4.\n--> "))
        except:
            print("Invalid response. Enter an integer between 1 and 4.\n--> ")
            ans = -1
        if (ans < 1 or ans > 4):
            print("Invalid, please enter a number between 1 and 4.")

    menuList[int(ans) - 1](schedules) #call appropriate function

    dirs.root() #change directory back to root

def newCourse():
    """newCourse continually prompts the user for the course information until
    the user has no more course sections to enter information for. newCourse
    then returns a list of course sections that the user entered. An example
    list would look like this:
    raw = [course1section1, course1section2, course1section3, ...]"""
    raw = [] #initialize raw course section list
    #get course information from user
    name = input("Enter course name: ")
    inst = input("Enter course instructor: ")
    loc = input("Enter course location: ")
    try:
        creds = int(input("Enter the number of course credits: "))
    except:
        creds = -1

    while (creds < 0): #user entered invalid value for course credits
        print("Invalid credit number. Please enter a positive integer.")
        try:
            creds = int(input("Enter the number of course credits: "))
        except:
            creds = -1
    start = input("Enter course start time (ex. 1:10pm or 13:10): ")
    end = input("Enter course end time (ex. 1:10pm or 13:10): ")
    dRaw = input("Enter course days separated by a comma (ex. mon,wed,fri): ")
    days = dRaw.replace(" ", "").split(',')
    #create course
    course = Course(name, inst, loc, creds, start, end, days)
    #append course to our raw course list
    raw.append(course)

    more = False
    inp = input("Do you wish to add more course sections (y/n)? ")
    if (inp[0].lower() == 'y'):
        more = True #user wants to add a section
    
    #get the info for those course sections.
    while more:
        newSection(raw) #append another course section

        #ask user if he wants to add another course section
        more = False
        inp = input("Do you wish to add more course sections (y/n)? ")
        if (inp[0].lower() == 'y'):
            more = True #user wants to add a section

    return raw #return a list of the course and its sections

def removeCourse(courseList):
    """removes a course from the course list"""
    displayCourses(courseList) #display list of courses
    length = len(courseList.getCourseList())
    inp = -1

    while (inp < 0 or inp > length):
        try:
            #get course index to remove
            inp = int(input("Which course would you like to delete? "))
        except: #invalid response
            print("Invalid response, enter an integer between 1 and", length)
            inp = -1

    #obtain user desired section list
    sList = courseList.getCourseList()[inp - 1]
    courseList.deleteSectionList(sList) #remove course from courseList

def removeSection(courseList):
    """removes a section from the course section list"""
    displayCourses(courseList) #display list of courses
    length = len(courseList)
    inp = -1

    while (inp < 0 or inp > length):
        try:
            #get course index to remove
            inp = int(input("Which course will you delete a section from? "))
        except: #invalid response
            print("Invalid response, enter an integer between 1 and", length)
            inp = -1

    displaySections(courseList[inp]) #display sections for that course

    num = len(courseList[inp])
    index = -1
    while (inp < 0 or inp > length):
        try:
            #get section index to remove
            inp = int(input("Choose a section to delete: "))
        except: #invalid response
            print("Invalid response, enter an integer between 1 and", num)
            num = -1

    courseList[inp - 1].pop(num - 1) #remove section from course

def displayCourses(courseList):
    """prints the course list to the screen"""
    print("Courses")
    print("*" * 10)
    for i in range(len(courseList.getCourseList())): #loop courses
        print(str(i + 1) + ')', courseList[i][0].getName())

def displaySections(sectionList):
    """prints the section list of a course to the screen"""
    print("Sections")
    print("*" * 10)
    for i in range(len(sectionList)): #loop courses
        #get section information ready to print
        st = sectionList[i].getStart().getStandard()
        end = sectionList[i].getEnd().getStandard()
        loc = sectionList[i].getLocation()
        days = ""
        for day in sectionList[i].getDays():
            days = days + day + ", "
        days = days[:-2]
        display = "{0} - {1}, {2} in {3}".format(st, end, days, loc)
        #display section information
        print(i + 1, ') ', display, sep = '')

def newSection(sectionList):
    """appends a new section to the course section list (that is passed in)"""
    
    if (sectionList): #if there is at least one section
        #get the previous section's information
        name = sectionList[-1].getName() #get name
        inst = sectionList[-1].getInstructor() #get instructor
        loc = sectionList[-1].getLocation() #get location
        creds = sectionList[-1].getCredits() #get the number of credits
        start = sectionList[-1].getStart().getStandard() #get start time
        end = sectionList[-1].getEnd().getStandard() #get end time  
    
        daysList = sectionList[-1].getDays() #get list of section meeting days
        dRaw = ""
        for day in daysList:
            dRaw = dRaw + day + ', ' #create a string from that list
        dRaw = dRaw[:-2] #remove the last comma from the string
        
    else: #there are no previous sections
        name = ""
        inst = ""
        loc = ""
        creds = 0
        start = ""
        end = ""
        dRaw = ""

    #get new info for the course section
    prompt = "Enter section {0} (press <enter> to use \"{1}\"): "
    inst = input(prompt.format("instructor", inst)) or inst
    loc = input(prompt.format("location", loc)) or loc
    start = input(prompt.format("start time", start)) or start
    end = input(prompt.format("end time", end)) or end
    
    dRaw = input(prompt.format("meeting days", dRaw)) or dRaw
    days = dRaw.replace(" ", "").split(",")

    #create section and append to sectionList
    course = Course(name, inst, loc, creds, start, end, days)
    sectionList.append(course)

def getCourseList(filename):
    """gets course info from a file & returns a list of all course sections"""
    file = open(filename, "r") #open file for reading
    cList = []
    raw = file.readlines() #read lines
    for i in range(len(raw)):
        raw[i].replace('\n', '') #strip newline character from lines

    #get course information and strip newline characters
    name = raw[0].replace("\n", "")
    creds = int(raw[3])

    allLoc = raw[2].split("||") #get list of all section meeting locations
    allTimes = raw[4].split("||") #get list of all section meeting times
    allDays = raw[5].split("||") #get list of all section meeting days
    allInst = raw[1].split("||") #get list of all section instructors

    #loop through all sections of the course and create a new
    #course instance for each section. Add them one by one to cList
    #NOTE: allTimes and allDays must have the same number of elements
    #in them, or the code WILL break. Even if a course meets on the
    #same day but different times, you must explicity say on which
    #days a specific time meets
    for i in range(len(allTimes)):
        times = allTimes[i].replace(" ", "").split('-')
        start = times[0].replace("\n", "")
        end = times[1].replace("\n", "")
        days = allDays[i].replace(" ", "").replace("\n", "").split(',')
        inst = allInst[i].strip().replace('\n', '').split(',')
        loc = allLoc[i].strip().replace('\n', '').split(',')

        #append new course to list
        cList.append(Course(name, inst[0], loc[0], creds, start, end, days))
    
    file.close() #close file
    
    return cList #return list of courses

def createSchedules(rawCourses):
    """Takes in a list of courses (double list, because each
    course has n number of instances of itself) and creates all possible
    schedules (valid & nonvalid) that can be created with the courses.
    Returns a list of those schedules"""
    nSect = len(rawCourses[0]) #get number of sections of the first course
    schedules = [] #initialize a blank list of schedules
    for i in range(nSect):
        #create a new schedule that contains only the first course
        sch = Schedule([rawCourses[0][i]])
        
        #recursively add a new course to the schedule
        #(this will also spawn additional unique schedules
        #and append them to schedules as well)
        addCourses(rawCourses[1:], sch, schedules)

    return schedules

def addCourses(rawCourses, sch, schedules):
    """So long as there are still rawCourses, addCourses
    will clone the previous schedule (sch) each time it loops, and then
    addCourses will recursively call itself so the next course can
    add itself. When there are no more courses to add to a schedule,
    then that schedule will be added to the master list
    of schedules (variable named schedules)"""
    if (rawCourses == []): #no more courses left to add to sch
        #add sch to schedules (our master list of schedules)
        schedules.append(sch.copy())
        return #terminate function
    
    else: #still courses to add
        #get first course occurrence
        for course in rawCourses[0]: #loop through course sections
            tempSch = sch.copy() #copy the schedule to a temp schedule
            tempSch.addCourse(course) #add course to the temp schedule

            #recursively call addCourses, advancing to the next course
            addCourses(rawCourses[1:], tempSch, schedules)

def removeInvalid(schedules):
    """removes any invalid schedules from the master list of schedules."""
    temp = [] #keep track of which schedules to delete
    for sch in schedules: #loop through all schedules
        if (not sch.isValid()): #schedule is invalid
            temp.append(sch) #add schedule to temporary list
            
    for sch in temp: #loop through temp list
        schedules.remove(sch) #remove schedule from schedules list

def displayStandard(schedules):
    """displays all schedules within the master
    list in standard AM/PM format"""
    for i in range(len(schedules)):
        print('\n', "*" * 50, "\nSchedule", i + 1, '\n', "*" * 50)
        schedules[i].printStandard()

def displayUniversal(schedules):
    """displays all schedules within the master
    list in universal (24-hour) format"""
    for i in range(len(schedules)):
        print('\n', "*" * 50, "\nSchedule", i + 1, '\n', "*" * 50)
        schedules[i].printUniversal()

def writeStandard(schedules):
    """writes all schedules to a file in standard AM/PM format"""
    filename = input("Enter filename to save as: ")
    file = open(filename, "w") #open file for writing
    for i in range(len(schedules)): #loop through schedules
        file.writelines("*" * 50 + '\n')
        file.writelines("Schedule " + str(i + 1) + '\n')
        file.writelines("*" * 50 + '\n')
        
        courses = schedules[i].getCourses()
        
        for c in courses: #loop through courses
            #write information to file
            file.writelines("Name: " + c.getName())
            file.writelines("\nCredits: " + str(c.getCredits()))
            file.writelines("\nInstructor: " + c.getInstructor())
            file.writelines("\nLocation: " + c.getLocation())
            file.writelines("\nTime: " + c.getStart().getStandard() + ' - ')
            file.writelines(c.getEnd().getStandard())
            file.writelines("\nDays: " +  str(c.getDays()) + '\n\n')

    print("Schedules have been saved to " + os.getcwd())

def writeUniversal(schedules):
    """writes all schedules to a file in universal 24-hour format"""
    filename = input("Enter filename to save as: ")
    file = open(filename, "w") #open file for writing
    for i in range(len(schedules)): #loop through schedules
        file.writelines("*" * 50 + '\n')
        file.writelines("Schedule " + str(i + 1) + '\n')
        file.writelines("*" * 50 + '\n')
        
        courses = schedules[i].getCourses()
        
        for c in courses: #loop through courses
            #write information to file
            file.writelines("Name: " + c.getName())
            file.writelines("\nCredits: " + str(c.getCredits()))
            file.writelines("\nInstructor: " + c.getInstructor())
            file.writelines("\nLocation: " + c.getLocation())
            file.writelines("\nTime: " + c.getStart().getUniversal() + ' - ')
            file.writelines(c.getEnd().getUniversal())
            file.writelines("\nDays: " +  str(c.getDays()) + '\n\n')

    print("Schedules have been saved to " + os.getcwd())

def main():
    """provides the start point for the program"""

    """
    Display the main program menu until user wants to exit the program
    """
    menu = ["New course list", "Load course list from file",
            "Help", "About", "Exit program"]
    while (True): #loop main menu
        choice = createMenu(menu, "Main Menu") #create menu and get user input

        #start course list menu with an empty course list
        if choice == 1:
            newCourseList() 

        #load course list from a file
        elif choice == 2:
            loadCourseList()

        #display help info for the main menu
        elif choice == 3:
            displayHelp()

        #load the about file and print it to the screen
        elif choice == 4:
            displayAbout() 

        #quit program
        elif choice == 5 and confirm(): #user confirms quitting
            exit()

if __name__ == "__main__":
    main()

