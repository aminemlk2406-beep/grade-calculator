from calculator import is_passing


def test_passing_grade():
    assert is_passing(12) is True


def test_failing_grade():
    assert is_passing(8) is False


def test_passing_grade_boundary():
    assert is_passing(10) is True
