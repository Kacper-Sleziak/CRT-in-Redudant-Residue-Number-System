class RNS:

    def __init__(self, positional_number_a, base):
        self.positional_number = positional_number_a
        self.base = base
        self.rns_number = self.convert_to_rns()

    def convert_to_rns(self):
        rns_number = []

        for modulo in self.base:
            remainder = self.positional_number % modulo
            print()
            rns_number.append(remainder)

        return rns_number

    def addition(self, RNS_b):
        result = []
        for i in range(len(self.rns_number)):
             remainders_sum = self.rns_number[i] + RNS_b.get_rns_number()[i]
             result.append(remainders_sum % self.base[i])

        return result

    def subtraction(self, RNS_b):
        result = []
        for i in range(len(self.rns_number)):
            remainders_sum = self.rns_number[i] - RNS_b.get_rns_number()[i]
            result.append(remainders_sum % self.base[i])

        return result

    def division(self, RNS_Number_b):
        result = 0
        return result

    def multiplication(self, RNS_b):
        result = []
        for i in range(len(self.rns_number)):
            remainders_sum = self.rns_number[i] * RNS_b.get_rns_number()[i]
            result.append(remainders_sum % self.base[i])

        return result

    def get_rns_number(self):
        return self.rns_number
