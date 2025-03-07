class Student:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def get_name(self):
        return self.name

class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """

    def __init__(self):
        self.students_list=[]
        self.students_grades=[]

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if not any(student[0] == id for student in self.students_list):
            self.students_list.append({"id": id, "name": name, "age": age})
            return True
        else:
            return False

    def students(self):
        return self.students_list

    def grades(self):
        return self.students_grades

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        for student in self.students_list:
            if student["id"]==id:
                student["name"]=name
                student["age"]=age
                return True
        return False

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        for student in self.students_list:
            if student["id"] == id:
                self.students_list.remove(student)
                return True
        return False


    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        if (grade not in (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)):
            return False
        else:
            self.students_grades.append({"student_id":student_id,"subject":subject,"grade":grade})
            return True


    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        total = 0
        count = 0
        for grade in self.students_grades:
            if grade["subject"] == subject:
                total += grade["grade"]
                count += 1

        if count == 0:
            return 0.0
        return total / count

