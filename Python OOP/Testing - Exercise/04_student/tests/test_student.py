from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Name", {"course_name": ["notes"]})
        self.second_student = Student("Name2")

    def test_correct_initialized(self):
        self.assertEqual("Name", self.student.name)
        self.assertEqual({"course_name": ["notes"]}, self.student.courses)
        self.assertEqual("Name2", self.second_student.name)
        self.assertEqual({}, self.second_student.courses)

    def test_enroll_with_valid_course_name_and_notes(self):
        result = self.student.enroll("course_name", ["other notes", "third note"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"course_name": ["notes", "other notes", "third note"]}, self.student.courses)
        self.assertEqual(3, len(self.student.courses["course_name"]))
        self.assertEqual(["notes", "other notes", "third note"], self.student.courses["course_name"])
        self.assertEqual("notes", self.student.courses["course_name"][0])
        self.assertEqual("other notes", self.student.courses["course_name"][1])

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.second_student.enroll("python", ["class", "circle", "function"])

        self.assertEqual({"python": ["class", "circle", "function"]}, self.second_student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_to_non_existing_course_with_third_param_y(self):
        result = self.second_student.enroll("python", ["class", "circle", "function"], "Y")

        self.assertEqual({"python": ["class", "circle", "function"]}, self.second_student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll("python", ["class", "circle", "function"], "N")

        self.assertEqual([], self.student.courses["python"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student.add_notes("course_name", "class")

        self.assertEqual(["notes", "class"], self.student.courses["course_name"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "other notes")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        result = self.student.leave_course("course_name")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
