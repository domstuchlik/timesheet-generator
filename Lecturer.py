
class Lecturer:
    """Base class for lecturers

    @firstName - first name of the lecturer
    @lastName - last name of the lecturer
    @specialization - List of subjects that lecturer can lecture
    @preferedDates - List of dates on which the lecturer is available
    @residence - Place where the lecturer lives
    @id - ID of the lecturer
    """

    def __init__(self, firstName, lastName, specialization, preferedDates, residence, id):
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.preferedDates = preferedDates
        self.residence = residence
        self.id = id

    def print(self):
        print(self.firstName, self.lastName, ",", self.specialization, ",", self.preferedDates, ",", self.residence)