
import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


def test_ticket_price_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_ticket_price_morning():
    assert ticket_price("regular", 25, 10, False) == 100


def test_ticket_price_evening_weekend():
    assert ticket_price("premium", 30, 20, True) == 320


def test_ticket_price_child():
    assert ticket_price("recliner", 2, 15, False) == 0


def test_ticket_price_young_person_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_ticket_price_senior_discount():
    assert ticket_price("premium", 60, 15, False) == 125


def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)


def test_invalid_show_time_below_zero():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_invalid_show_time_above_23():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_group_discount_no_discount():
    assert group_discount(2, False) == 0


def test_group_discount_medium_group():
    assert group_discount(5, False) == 10


def test_group_discount_large_group():
    assert group_discount(10, False) == 15


def test_group_discount_student_group():
    assert group_discount(5, True) == 15


def test_group_discount_student_small_group():
    assert group_discount(2, True) == 0


def test_invalid_ticket_count():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_small_snack_with_coupon():
    assert snack_combo("small", True) == 70


def test_medium_snack_without_coupon():
    assert snack_combo("medium", False) == 180


def test_large_snack_with_coupon():
    assert snack_combo("large", True) == 200
