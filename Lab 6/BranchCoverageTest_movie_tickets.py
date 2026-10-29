
import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price: valid seat and all time periods
def test_morning_price():
    assert ticket_price("regular", 25, 11, False) == 100


def test_afternoon_price():
    assert ticket_price("premium", 25, 15, False) == 250


def test_evening_price():
    assert ticket_price("recliner", 25, 18, False) == 430


def test_weekend_surcharge():
    assert ticket_price("regular", 25, 15, True) == 190


# Ticket price: validation branches
@pytest.mark.parametrize("seat", ["vip", "economy"])
def test_unknown_seat(seat):
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price(seat, 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_hours(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


# Ticket price: age branches
def test_child_free_ticket():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_adult_full_price():
    assert ticket_price("regular", 30, 15, False) == 150


def test_senior_discount():
    assert ticket_price("regular", 60, 15, False) == 75


# Group discount: invalid, small, medium, and large groups
def test_zero_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_small_group():
    assert group_discount(2, False) == 0


def test_medium_group():
    assert group_discount(5, False) == 10


def test_large_group():
    assert group_discount(10, False) == 15


def test_student_medium_group():
    assert group_discount(5, True) == 15


def test_student_large_group():
    assert group_discount(10, True) == 20


def test_student_small_group():
    assert group_discount(2, True) == 0


# Snack combo: small, medium, other sizes, and coupon branches
def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_without_coupon():
    assert snack_combo("large", False) == 250


def test_unknown_snack_size():
    assert snack_combo("family", False) == 250
