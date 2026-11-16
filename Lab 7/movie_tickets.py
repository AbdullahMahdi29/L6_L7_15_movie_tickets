
def parse_seat(seat):
    # Check whether input is a valid string
    if not isinstance(seat, str):
        return None

    seat = seat.strip()

    # Check seat format: one alphabetic row followed by digits
    if len(seat) < 2:
        return None

    if not seat[0].isalpha() or not seat[1:].isdigit():
        return None

    seat_number = int(seat[1:])

    if seat_number <= 0:
        return None

    return seat[0].upper(), seat_number


def total_price(prices_csv):
    # Check input type
    if not isinstance(prices_csv, str):
        return None

    try:
        parts = prices_csv.split(',')

        # Reject empty values
        if not parts or any(not p.strip() for p in parts):
            return None

        prices = [int(p.strip()) for p in parts]

        # Reject negative prices
        if any(p < 0 for p in prices):
            return None

        return round(sum(prices) * 1.18, 2)

    except ValueError:
        return None


def average_rating(ratings):
    # Check input type
    if not isinstance(ratings, str):
        return None

    try:
        parts = ratings.split()

        # Reject empty ratings
        if not parts:
            return None

        values = [int(r) for r in parts]

        return round(sum(values) / len(values), 1)

    except ValueError:
        return None


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
