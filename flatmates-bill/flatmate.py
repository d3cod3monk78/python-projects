from bill import Bill


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        to_pay = weight * bill.amount
        return to_pay
