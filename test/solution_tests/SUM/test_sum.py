from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_negative_values(self):
        assert sum_solution.compute(-10, 10) == 3

    def test_sum_validates_arguments_greater_than_100(self)

