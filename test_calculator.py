import pytest
from calculator import calculate_average, get_grade_category, is_passing


def test_average():
    assert calculate_average([10, 12, 14]) == 12


def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])


def test_passing():
    assert is_passing(10) is True
    assert is_passing(9) is False


def test_grade_categories():
    assert get_grade_category(17) == "Excellent"
    assert get_grade_category(13) == "Good"
    assert get_grade_category(10.5) == "Average"
    assert get_grade_category(7) == "Fail"
