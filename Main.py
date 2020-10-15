import os
from datetime import date, timedelta, datetime
from Lecturer import Lecturer
from Subject import Subject
from CalculatedDay import CalculatedDay
from TrainingDay import TrainingDay

def main():
    """Main loop for timesheet generation.

    Multiple iterations will asure optimal calculation of the timesheet.
    The output will be csv file with correctly calculated times.
    """

    print("Loading lecturers...\n")
    listOfLecturers = loadLecturers()

    print("Loading subjects...\n")
    listOfSubjects = loadSubjects()

    periodFrom, periodTo = getTimePeriod()
            
    print("Extracting days from time period...\n")
    listOfTrainingDays = trainingDaysExtractor(periodFrom, periodTo)

    print("Calculating optimal timesheets...")
    getTimesheets(listOfLecturers, listOfSubjects, listOfTrainingDays)

def loadLecturers():
    """Load all lecturers from file

    Opens file lecturers.txt, creates the lecturers and stores them into the list
    """
    pathToFile = find("lecturers.txt", "/Users/dstuchli/")
    listOfLecturers = []
    increment = 0

    lecturers = open(pathToFile, "r")
    lines = lecturers.readlines()

    for currentLine in lines:
        parsedLine = parseLecturer(currentLine)
        lecturerId = "{0}{1}{2}".format(parsedLine[0][0], parsedLine[1][0], increment)

        newLecturer = Lecturer(parsedLine[0], parsedLine[1], parsedLine[2], parsedLine[3], parsedLine[4], lecturerId)

        listOfLecturers.append(newLecturer)

        increment += 1
    
    lecturers.close()

    return listOfLecturers

def loadSubjects():
    """Load all subjects from file

    Opens file subjects.txt, creates subjects and stores them into the list
    """
    pathToFile = find("subjects.txt", "/Users/dstuchli/")
    listOfSubjects = []
    increment = 0

    subjects = open(pathToFile, "r")
    lines = subjects.readlines()

    for currentLine in lines:
        parsedLine = parseSubject(currentLine)
        subjectId = "{0}{1}".format(parsedLine[3], increment)

        newSubject = Subject(parsedLine[0], parsedLine[1], parsedLine[2], parsedLine[3], subjectId)

        listOfSubjects.append(newSubject)

        increment += 1

    subjects.close()

    return listOfSubjects

def parseLecturer(line):
    """Parses the line with lecturer's information

    Splits the line appropriately to firstName, lastName, specialization, 
    preferedDates and residence
    """
    logicalChunks = line.split(':')

    name = logicalChunks[0].split(' ')
    subjects = logicalChunks[1].split(',')
    preferedDates = logicalChunks[2].split(',')

    parsedLine = [name[0], name[1], subjects, preferedDates, logicalChunks[3].strip()]

    return parsedLine

def parseSubject(line):
    """Parses the line with subject's information

    Splits the line appropriately to name, hourlyAllowance, prerequisites
    and domain
    """
    logicalChunks = line.split(':')

    prerequisites = logicalChunks[2].split(',')

    parsedLine = [logicalChunks[0], logicalChunks[1], prerequisites, logicalChunks[3].strip()]

    return parsedLine

def find(name, path):
    """Finds the file in system

    Uses the file name and approximate path to find the file in the system

    Args:
        name (string): file name
        path (string): approximate path to file

    Returns:
        string: Absolute path to file
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def trainingDaysExtractor(periodFrom, periodTo):
    """Stores all fridays and saturdays with correct times and dates

    """
    listOfTrainingDays = []
    periodFrom = datetime.strptime(periodFrom, '%d.%m.%Y')
    periodTo = datetime.strptime(periodTo, '%d.%m.%Y')

    currentDay = periodFrom

    dateDelta = None
    increment = 0

    while currentDay <= periodTo:
        if 3 < currentDay.weekday() < 6:
            dayId = "{0}{1}".format(currentDay.strftime("%A")[0], increment)
            newTrainingDay = TrainingDay(currentDay.strftime('%d.%m.%Y'), currentDay.strftime("%A"), 8, dayId)
            listOfTrainingDays.append(newTrainingDay)
        
        if currentDay.weekday() == 4:
            dateDelta = timedelta(days = 1)
        else:
            dateDelta = timedelta(days = 6)

        currentDay += dateDelta
        increment += 1

    return listOfTrainingDays

def getTimePeriod():
    periodFrom = ""
    periodTo = ""

    while True:
        periodFrom = input("Please enter the time period from:\n")
        try:
            datetime.strptime(periodFrom, '%d.%m.%Y')
        except ValueError:
            print("Incorrect date format. Please use DD.MM.YYYY format.")
            continue
        else:
            break
    
    while True:
        periodTo = input("to:\n")
        try:
            datetime.strptime(periodTo, '%d.%m.%Y')
        except ValueError:
            print("Incorrect date format. Please use DD.MM.YYYY format.")
            continue
        else:
            break

    return periodFrom, periodTo

def getTimesheets(listOfLecturers, listOfSubjects, listOfTrainingDays):
    listOfTimesheets = []
    increment = 0

    listOfCalculatedDays = createPrecalculatedDays(listOfTrainingDays)

    distributeLecturers(listOfLecturers, listOfCalculatedDays)

    distributeSubjects(listOfSubjects, listOfCalculatedDays)

    for i in listOfCalculatedDays:
        i.print()

    # for lecturer in listOfLecturers:
    #     for preferedDate in lecturer.preferedDates:
    #         if preferedDate[0] == 'P':
    #             for trainingDay in listOfTrainingDays:
    #                 if datetime.strptime(trainingDay.actualDate, '%d.%m.%Y') == datetime.strptime(preferedDate[1:], '%d.%m.%Y'):
    #                     newCalculatedDay

    return listOfTimesheets

def createPrecalculatedDays(listOfTrainingDays):
    listOfCalculatedDays = []

    for trainingDay in listOfTrainingDays:
        listOfCalculatedDays.append(CalculatedDay(trainingDay.actualDate, trainingDay.weekday, trainingDay.availableHours, 0, {}, set(), [], trainingDay.dayId))

    return listOfCalculatedDays

def distributeLecturers(listOfLecturers, listOfCalculatedDays):
    increment = 0
    for calculatedDay in listOfCalculatedDays:
        for lecturer in listOfLecturers:
            for preferedDate in lecturer.preferedDates:
                if datetime.strptime(preferedDate[1:], '%d.%m.%Y') == datetime.strptime(calculatedDay.actualDate, '%d.%m.%Y'):
                    if preferedDate[0] == 'P':
                        listOfCalculatedDays[increment].availableLecturers["{0}{1}".format(lecturer.firstName, lecturer.lastName)] = "P"
                    else:
                        listOfCalculatedDays[increment].availableLecturers["{0}{1}".format(lecturer.firstName, lecturer.lastName)] = "N"
                    for specialization in lecturer.specializations:
                        listOfCalculatedDays[increment].availableSpecializations.add(specialization)
        increment += 1

def distributeSubjects(listOfSubjects, listOfCalculatedDays):
    increment = 0

    for calculatedDay in listOfCalculatedDays:
        for subject in listOfSubjects:
            for specialization in calculatedDay.availableSpecializations:
                if subject.name == specialization:
                    calculatedDay.possibleSubjects.append(subject.name)
        increment += 1


main()
