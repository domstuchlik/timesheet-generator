
class Subject:
    """Base class for subjects

    @name - name of the subject
    @hourlyAllowance - time which the subject consumes
    @prerequisites - subjects needed for this subject to be available
    @domain - the general focus of this subject
    @subjectId - ID of the subject
    """

    def __init__(self, name, hourlyAllowance, prerequisites, domain, subjectId):
        self.name = name
        self.hourlyAllowance = hourlyAllowance
        self.prerequisites = prerequisites
        self.domain = domain
        self.subjectId = subjectId

    def print(self):
        print(
            "Name:", self.name, "\n",
            "Hourly Allowance:", self.hourlyAllowance, "\n",
            "Prerequisites:", self.prerequisites, "\n",
            "Domain:", self.domain, "\n",
            "ID:", self.subjectId, "\n")