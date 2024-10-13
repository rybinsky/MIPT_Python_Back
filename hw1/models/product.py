class Product:
    def __init__(self, name: str, category: str, price: int) -> None:
        self.name: str = name
        self.category: str = category
        self.price: int = price
        self.sale: int = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: int) -> None:
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> float:
        # Учитываем скидку в процентах
        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        return (
            f"Product(name = '{self.name}', "
            f"category = '{self.category}', "
            f"price = {self.price}, "
            f"sale = {self.sale}%)"
        )
