num_guest = 2
bill_amount = 80
tip_percentage = 0.10


def tip_calculator():
    bill_per_person = (bill_amount // num_guest)
    tip_amount = (bill_per_person * tip_percentage)
    total_amount = (bill_per_person + tip_amount)
    return total_amount


print(tip_calculator())
