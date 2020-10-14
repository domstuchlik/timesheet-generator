import os
import Lecturer, Subject

def main():
    """Main loop for timesheet generation.

    Multiple iterations will asure optimal calculation of the timesheet.
    The output will be csv file with correctly calculated times.
    """
    listOfLecturers = loadLecturers()
    listOfSubjects = loadSubjects()

    for lecturer in listOfLecturers:
        lecturer.print()
    for subject in listOfSubjects:
        subject.print()

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
        lecturer_id = "{0}{1}{2}".format(parsedLine[0][0], parsedLine[1][0], increment)

        newLecturer = Lecturer.Lecturer(parsedLine[0], parsedLine[1], parsedLine[2], parsedLine[3], parsedLine[4], lecturer_id)

        listOfLecturers.append(newLecturer)

        currentLine = lecturers.readline()
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

        newSubject = Subject.Subject(parsedLine[0], parsedLine[1], parsedLine[2], parsedLine[3], subjectId)

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
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

main()
