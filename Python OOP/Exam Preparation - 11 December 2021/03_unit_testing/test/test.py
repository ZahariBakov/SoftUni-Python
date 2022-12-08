from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Alpha")

    def test_correct_initialized(self):
        self.assertEqual("Alpha", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_with_wrong_parameter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Alpha8"

        expected = "Team Name can contain only letters!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_member(self):
        result = self.team.add_member(Ivan=25)

        expected = "Successfully added: Ivan"
        self.assertEqual(expected, result)
        self.assertEqual({"Ivan": 25}, self.team.members)

        second_result = self.team.add_member(Gosho=27)
        self.assertEqual({"Ivan": 25, "Gosho": 27}, self.team.members)
        second_expected = "Successfully added: Gosho"
        self.assertEqual(second_expected, second_result)

    def test_remove_member_that_does_not_exist(self):
        self.team.add_member(Gosho=27, Petko=23)
        result = self.team.remove_member("Ivan")

        expected = "Member with name Ivan does not exist"
        self.assertEqual(expected, result)
        self.assertEqual({"Gosho": 27, "Petko": 23}, self.team.members)

    def test_successful_remove_member(self):
        self.team.add_member(Ivan=25, Gosho=27, Petko=23)

        result = self.team.remove_member("Gosho")
        expected = "Member Gosho removed"

        self.assertEqual(expected, result)
        self.assertEqual({"Ivan": 25, "Petko": 23}, self.team.members)

    def test__gt__method_return_true(self):
        other = Team("Beta")
        self.team.add_member(Ivan=25, Gosho=27, Petko=23)
        other.add_member(Dragan=25, Cvetan=27)
        result = self.team > other

        self.assertEqual(True, result)

    def test__gt__method_return_false(self):
        other = Team("Beta")
        self.team.add_member(Ivan=25, Gosho=27)
        other.add_member(Dragan=25, Cvetan=27, Petko=23)
        result = self.team > other

        self.assertEqual(False, result)

    def test__len__method(self):
        self.team.add_member(Ivan=25, Gosho=27, Petko=23)
        self.assertEqual(3, len(self.team))

    def test__add__method(self):
        other = Team("Beta")
        self.team.add_member(Ivan=25, Gosho=27, Petko=23)
        other.add_member(Dragan=25, Cvetan=27)

        new_team = self.team + other

        self.assertEqual("AlphaBeta", new_team.name)
        expected = {"Ivan": 25, "Gosho": 27, "Petko": 23, "Dragan": 25, "Cvetan": 27}
        self.assertEqual(expected, new_team.members)

    def test__str__method(self):
        self.team.add_member(Ivan=25, Gosho=27, Petko=23)
        expected = "Team name: Alpha\n"\
                   "Member: Gosho - 27-years old\n"\
                   "Member: Ivan - 25-years old\n"\
                   "Member: Petko - 23-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()
