def get_ticket_price(age: int) -> float:
    base_price = 100.00

    if age < 6:
        return 0.0
    elif 6 <= age <= 17:
        return base_price*0.5
    elif 18 <= age <= 59:
        return base_price
    else:
        return base_price*0.7

def test_get_ticket_price():
    assert get_ticket_price(5) == 0.0
    assert get_ticket_price(10) == 50.0
    assert get_ticket_price(30) == 100.0
    assert get_ticket_price(70) == 70.0
    print("successful")

test_get_ticket_price()