from models.product import Product


def extract_prices(products: list[Product]) -> list[int]:
    return [product.price for product in products]
