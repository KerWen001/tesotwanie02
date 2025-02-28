class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.prices = {}
        self.totalValue = 0
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        """Dodawanie produktu do koszyka"""
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
            self.prices[product_name] = price
        self.totalValue += price * quantity
        return True

    def remove_product(self, product_name: str) -> bool:
        """Usuwanie produktu z koszyka"""
        self.products[product_name] = self.products[product_name] - 1
        self.totalValue = self.totalValue - self.prices[product_name]
        return True

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        """Aktualizacja ilosci produktu w koszyku"""
        if product_name in self.products:
            self.totalValue = self.totalValue - self.products[product_name] * self.prices[product_name]
            self.products[product_name] = new_quantity
            self.totalValue = self.totalValue + new_quantity * self.prices[product_name]
        else:
            return False
        return True

    def get_products(self):
        """Pobieranie nazw produktow z koszyka"""
        list = [value for value in self.products.keys()]
        return list

    def count_products(self) -> int:
        """Pobieranie liczby produktow znajdujacych sie w koszyku"""
        sum = 0
        for value in self.products.values():
            sum += value
        return sum

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktow w koszyku"""
        return self.totalValue * (1 - self.discount / 100)

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        if discount_code == "dsc5":
            self.discount = 5
            return True
        elif discount_code == "dsc20":
            self.discount = 20
            return True
        elif discount_code == "dsc10":
            self.discount = 10
            return True
        else:
            return False

    def checkout(self) -> bool:
        """Realizacja zamowienia"""
        if len(self.products) == 0:
            return False
        else:
            return True
