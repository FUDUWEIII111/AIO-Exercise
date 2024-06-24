from abc import ABC, abstractmethod  # Import the abstract base class module


class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob

# The Student, Teacher, and Doctor classes inherit from the Person class


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f'Student name: {self._name} - Year of birth: {self._yob} - Grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f'Teacher name: {self._name} - Year of birth: {self._yob} - Subject: {self.__subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f'Doctor name: {self._name} - Year of birth: {self._yob} - Specialist: {self.__specialist}')

# The Ward class contains a list of people and methods to add a person, describe the ward, and count the number of doctors


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f'Ward name: {self.__name}')
        for person in self.__list_people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_by_yob(self):
        self.__list_people.sort(key=lambda x: x.get_yob(),  reverse=True)

    def compute_avg_age(self):
        total_age = 0
        teacher_count = 0
        for person in self.__list_people:
            if isinstance(person, Teacher):
                total_age += person.get_yob()
                teacher_count += 1
        return total_age / teacher_count


def main():
    teacher1 = Teacher('Thien', 2003, 'Artificial  Intelligence')
    doctor1 = Doctor('Cheng', 2004, 'Artificial  Intelligence')
    teacher2 = Teacher('Huy', 2002, 'Machine Learning')
    ward = Ward('My ward')
    ward.add_person(teacher1)
    ward.add_person(doctor1)
    ward.add_person(teacher2)
    number_of_doctor = ward.count_doctor()
    print(f'Number of doctor: {number_of_doctor}')
    ward.describe()
    avg_teacher_age = ward.compute_avg_age()
    print(f'Average teacher age: {avg_teacher_age}')


if __name__ == "__main__":
    main()
