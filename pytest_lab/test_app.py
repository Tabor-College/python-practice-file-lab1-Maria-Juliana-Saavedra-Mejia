# test_app.py - Complete Test Suite

import pytest
from app import add, divide, divide_strict, is_even


# ====== BASIC UNIT TESTS ======

def test_add_positive_numbers():
    """Test adding positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_and_positive():
    """Test adding negative and positive."""
    assert add(-1, 1) == 0


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-5, -3) == -8


# ====== EDGE CASE TESTS ======

def test_divide_normal():
    """Test normal division."""
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5
    assert divide(100, 4) == 25


def test_divide_with_remainder():
    """Test division with remainder."""
    assert divide(10, 3) == 10 / 3
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """Test division by zero."""
    assert divide(5, 0) == "Error"
    assert divide(0, 0) == "Error"


# ====== PARAMETRIZED TESTS ======

@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-7, False),
    (100, True),
])
def test_is_even(num, expected):
    """Test is_even with multiple inputs."""
    assert is_even(num) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (20, 4, 5.0),
    (7, 2, 3.5),
    (0, 5, 0.0),
])
def test_divide_parametrized(a, b, expected):
    """Test divide with parametrized inputs."""
    assert divide(a, b) == expected


# ====== EXCEPTION TESTS ======

def test_divide_exception_zero_divisor():
    """Test divide_strict raises ValueError."""
    with pytest.raises(ValueError):
        divide_strict(5, 0)


def test_divide_exception_message():
    """Test exception message."""
    with pytest.raises(ValueError, match="Cannot divide"):
        divide_strict(10, 0)


@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
])
def test_divide_exception_multiple(a, b):
    """Test exception with multiple inputs."""
    with pytest.raises(ValueError):
        divide_strict(a, b)


# ====== FIXTURE TESTS ======

@pytest.fixture
def numbers():
    """Fixture providing numbers."""
    return {"a": 10, "b": 5}


def test_add_with_fixture(numbers):
    """Test add using fixture."""
    result = add(numbers["a"], numbers["b"])
    assert result == 15


def test_divide_with_fixture(numbers):
    """Test divide using fixture."""
    result = divide(numbers["a"], numbers["b"])
    assert result == 2.0


@pytest.fixture
def sample_data():
    """Fixture for collection testing."""
    return [1, 2, 3, 4, 5]


def test_sum_with_fixture(sample_data):
    """Test sum with fixture."""
    assert sum(sample_data) == 15


def test_count_with_fixture(sample_data):
    """Test length with fixture."""
    assert len(sample_data) == 5


@pytest.fixture
def calculator_numbers():
    """Fixture with setup and teardown."""
    numbers = [10, 20, 30, 40, 50]
    print("\nSetting up test data...")
    yield numbers
    print("\nCleaning up test data...")


def test_with_setup_teardown(calculator_numbers):
    """Test using setup/teardown fixture."""
    assert sum(calculator_numbers) == 150


# ====== FUNCTIONAL TESTS ======

def test_full_calculation_flow():
    """Test complete workflow."""
    step1 = add(10, 5)
    assert step1 == 15

    final_result = divide(step1, 3)
    assert final_result == 5.0


def test_complex_workflow():
    """Test multi-step workflow."""
    step1 = add(50, 30)
    assert step1 == 80

    step2 = divide(step1, 2)
    assert step2 == 40.0

    step3 = divide(step2, 2)
    assert step3 == 20.0


def test_workflow_with_error_handling():
    """Test workflow with error."""
    result1 = add(100, 50)
    assert result1 == 150

    result2 = divide(result1, 0)
    assert result2 == "Error"


@pytest.fixture
def workflow_data():
    """Fixture for workflow tests."""
    return {
        "initial_a": 20,
        "initial_b": 10,
        "divisor": 5
    }


def test_workflow_with_fixture(workflow_data):
    """Functional test using fixture."""
    step1 = add(workflow_data["initial_a"], workflow_data["initial_b"])
    assert step1 == 30

    step2 = divide(step1, workflow_data["divisor"])
    assert step2 == 6.0