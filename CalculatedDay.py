
class CalculatedDay:
    """Base class for calculated days

    @actualDate - date of the day
    @weekday - name of the day
    @availableHours - number of hours available for occupation
    @occupiedHours - number of hours occupied
    @availableLecturers - dictionary of lecturers available this day with possible "prefer" flag
    @availableSubjects - list of subjects on this day
    @dayId - ID of the day
    """
    def __init__(self, actualDate, weekday, availableHours, occupiedHours, availableLecturers, availableSpecializations, possibleSubjects, dayId):
        self.actualDate = actualDate
        self.weekday = weekday
        self.availableHours = availableHours
        self.occupiedHours = occupiedHours
        self.availableLecturers = availableLecturers
        self.availableSpecializations = availableSpecializations
        self.possibleSubjects = possibleSubjects
        self.dayId = dayId

    def print(self):
        print(
            "Date:", self.actualDate, "\n",
            "Day:", self.weekday, "\n",
            "Available hours:", self.availableHours, "\n",
            "Occupied hours:", self.occupiedHours, "\n",
            "Available lecturers:", self.availableLecturers, "\n",
            "Available specializations:", self.availableSpecializations, "\n",
            "Possible subjects:", self.possibleSubjects, "\n",
            "ID:", self.dayId, "\n")
