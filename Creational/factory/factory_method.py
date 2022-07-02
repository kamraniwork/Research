from abc import ABCMeta, abstractmethod


class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass


class Be(AbstractDegree):
    def info(self):
        print("Bachelor of engineering")

    def __str__(self):
        return "Bachelor of engineering"


class Me(AbstractDegree):
    def info(self):
        print("Master of engineering")

    def __str__(self):
        return "Master of engineering"


class Mba(AbstractDegree):
    def info(self):
        print("Master of business administration")

    def __str__(self):
        return "Master of business engineering"


class AbstractPersonFactory(object):
    def __init__(self):
        self._degrees = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def add_degree(self, degree):
        self._degrees.append(degree)

    def get_degree(self):
        return self._degrees


class ManagerFactory(AbstractPersonFactory):
    def create_profile(self):
        self.add_degree(Be())
        self.add_degree(Mba())


class EngineerFactory(AbstractPersonFactory):
    def create_profile(self):
        self.add_degree(Be())
        self.add_degree(Me())


class ProfileCreateFactory(object):
    @staticmethod
    def create_profile(name):
        return eval(name + 'Factory')()


if __name__ == '__main__':
    profile_type = input("Which Profile would you like to create? Manager/Engineer - ")
    profile = ProfileCreateFactory.create_profile(profile_type)
    print("Profile has following degrees -")
    for deg in profile.get_degree():
        print('- ', deg)
