from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        if race_pos == 1:
            revenue += 1_000_000

        elif race_pos <= 3:
            revenue += 500_000

        if race_pos <= 5:
            revenue += 100_000

        elif race_pos <= 7:
            revenue += 50_000

        revenue -= 200_000
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
