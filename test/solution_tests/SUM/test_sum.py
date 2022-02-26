import pytest

from solutions.SUM import sum_solution
from solutions.SUM.sum_solution import ValidationException


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_negative_values(self):
        with pytest.raises(ValidationException):
            sum_solution.compute(-10, 10) == 3

    def test_sum_validates_arguments_greater_than_100(self, caplog):
        with pytest.raises(ValidationException) as context:
            sum_solution.compute(200, 300)

        breakpoint()




