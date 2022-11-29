from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Hero name", 1, 100, 100)
        self.enemy = Hero("Enemy name", 1, 50, 50)

    def test_correct_initialized(self):
        self.assertEqual("Hero name", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_hero_is_same_as_enemy_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_not_have_health_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as vr:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(vr.exception))

    def test_battle_when_enemy_not_have_health_raise_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as vr:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy name. He needs to rest", str(vr.exception))

    def test_battle_when_hero_and_enemy_have_zero_health(self):
        self.hero.health = 50

        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_health_remove_after_fight(self):
        self.hero.health = 50
        self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_when_hero_win(self):
        self.assertEqual("You win", self.hero.battle(self.enemy))

    def test_battle_when_enemy_win(self):
        self.enemy.health = 200
        self.enemy.damage = 200

        self.assertEqual("You lose", self.hero.battle(self.enemy))

    def test_battle_hero_win(self):
        self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_enemy_win(self):
        self.enemy.health = 200
        self.enemy.damage = 200

        self.hero.battle(self.enemy)

        self.assertEqual(105, self.enemy.health)
        self.assertEqual(205, self.enemy.damage)
        self.assertEqual(2, self.enemy.level)

    def test_correct_str_method(self):
        result = str(self.hero)
        expected = "Hero Hero name: 1 lvl\n" \
                   "Health: 100\n" \
                   "Damage: 100\n"

        self.assertEqual(expected, result)


if __name__ == '__main':
    main()
