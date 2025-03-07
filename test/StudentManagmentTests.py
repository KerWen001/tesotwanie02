import unittest
from src.student_managment import StudentManagement

class StudentManagementTest(unittest.TestCase):
    def test_add_student_should_add_student_to_list(self):
        # Given
        student_management = StudentManagement()

        # When
        student_management.add_student(1, "Janek", 20)

        # Then
        self.assertEqual(student_management.students(), [{"id": 1, "name": "Janek", "age": 20}])


    def test_update_student_should_update_student(self):
        #Given
        student_management=StudentManagement()

        #When
        student_management.add_student(1, "Robert", 20)
        student_management.update_student(1,"Gerwazy",20)

        # Then
        self.assertEqual(student_management.students(), [{"id": 1, "name": "Gerwazy", "age": 20}])

    def test_remove_student_should_remove_student_from_list(self):
        #Given
        student_management=StudentManagement()

        #When
        student_management.add_student(1, "Robert", 20)
        student_management.remove_student(1)

        # Then
        self.assertEqual(student_management.students(), [])

    def test_add_grade_should_add_grade_to_list(self):
        #Given
        student_management=StudentManagement()

        #When
        student_management.add_student(1, "Robert", 20)
        student_management.add_grade(1, "WF", 4.5)

        # Then
        self.assertEqual(student_management.grades(), [{"student_id":1,"subject":"WF","grade":4.5}])

    def test_avg_grade_should_return_subject_average_grade(self):
        # Given
        student_management = StudentManagement()

        # When
        student_management.add_student("1", "Robert", 20)
        student_management.add_grade("1", "WF", 4.5)
        student_management.add_grade("1", "Matematyka", 3.0)
        student_management.add_grade("1", "Matematyka", 5.0)

        # Then
        self.assertEqual(student_management.avg_grades("Matematyka"), 4.0)



if __name__ == "__main__":
    unittest.main()