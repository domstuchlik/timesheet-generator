
class Subject:
    """Base class for subjects

    @name - name of the subject
    @hourly_allowance - time which the subject consumes
    @prerequisites - subjects needed for this subject to be available
    @domain - the general focus of this subject
    @id - ID of the subject
    """

    domain = "UNUSED"

    def __init__(self, name, hourly_allowance, prerequisites, domain, id):
        self.name = name
        self.hourly_allowance = hourly_allowance
        self.prerequisites = prerequisites
        self.domain = domain
        self.id = id