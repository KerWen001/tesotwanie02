from register_form_fields import RegisterFormFields
from validator import Validator

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if not self.pesel or not self.pesel.strip():
            return False

        pesel = self.pesel.strip()

        if len(pesel) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - (control_sum % 10)) % 10

        if control_digit != int(pesel[10]):
            return False

        return True

    def field_name(self):
        return RegisterFormFields.PESEL

