import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name, description):
    """
    Создает продукт.
    """
    product = stripe.Product.create(name=name, description=description)
    return product


def create_stripe_price(amount):
    """
    Создает цену.
    """
    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={
            "name": "Course Buying",
        },
    )


def create_stripe_session(price):
    """
    Создаёт сессию на оплату
    """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
