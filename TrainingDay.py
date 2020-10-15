
class TrainingDay:
    """Base class for days available for training

    @actualDate - date of the day
    @weekday - name of the day
    @availableHours - number of hours available for occupation
    @dayId - ID of the day
    """

    def __init__(self, actualDate, weekday, availableHours, dayId):
        self.actualDate = actualDate
        self.weekday = weekday
        self.availableHours = availableHours
        self.dayId = dayId

    def print(self):
        print(
            "Date:", self.actualDate, "\n",
            "Day:", self.weekday, "\n",
            "Available hours:", self.availableHours, "\n",
            "ID:", self.dayId, "\n")
