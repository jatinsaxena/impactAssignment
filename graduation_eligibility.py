class Graduation:
    """
    Graduation class for
    """
    def __init__(self, n: int, m: int = 4):
        self.number_of_days = n
        self.consec_holidays_allowed = m

    def rec(self, n: int, m: int):
        if self.consec_holidays_allowed == m:
            return 0
        if n == 0:
            return 1

        return self.rec(n - 1, 0) + self.rec(n - 1, m + 1)

    def calculate(self):
        x1 = self.rec(self.number_of_days, 0)  # total number of valid way to attend classes
        x2 = self.rec(self.number_of_days - 1, 1)  # total number of way to miss last day

        return f"{x2}/{x1}"
