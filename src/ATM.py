class InvalidPinException(Exception):
    pass


class ATM:
    """
    Klasa reprezentujÄca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """
    def __init__(self,balance,pin):
        self.balance=balance
        self.pin=pin

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :return: Saldo konta uĹźytkownika.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        return self.balance

    def deposit(self, pin: int, amount: float) -> float:
        """
        WpĹaca Ĺrodki na konto uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wpĹacenia.
        :return: Aktualne saldo po wpĹacie.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount <= 0:
            raise ValueError("Kwota do wpłaty musi być większa od zera.")
        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:
        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount > self.balance:
            raise ValueError("Kwota do wyplaty musi byc mniejsza od aktualnego balansu.")
        self.balance -= amount
        return self.balance