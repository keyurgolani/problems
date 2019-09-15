from utilities import BaseProblem


class TestProblem(BaseProblem):
    def get_name(self):
        return "TestProblem"

    def solve(self):
        return "Solve called"

    def show(self):
        return "Show called"

    def test(self):
        return "Test called"

    def define(self):
        return "Define called"

    def detail(self):
        return "Detail called"

