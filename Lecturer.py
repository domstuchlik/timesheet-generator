
class Lecturer:
    """Base class for lecturers

    @firstName - first name of the lecturer
    @lastName - last name of the lecturer
    @specialization - List of subjects that lecturer can lecture
    @preferedDates - List of dates on which the lecturer is available
    @residence - Place where the lecturer lives
    @lecturerId - ID of the lecturer
    """

    def __init__(self, firstName, lastName, specialization, preferedDates, residence, lecturerId):
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.preferedDates = preferedDates
        self.residence = residence
        self.lecturerId = lecturerId

    def print(self):
        print(
            "Last Name:", self.lastName, "\n",
            "First Name:", self.firstName, "\n",
            "Specialization:", self.specialization, "\n",
            "Prefered dates:", self.preferedDates, "\n",
            "Residence:", self.residence, "\n",
            "ID:", self.lecturerId, "\n")