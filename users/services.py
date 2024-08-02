import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(course):
    """
    Создает продукт.
    """
    return stripe.Product.create(name=course.name)


def create_stripe_price(product, amount):
    """
    Создает цену.
    """
    return stripe.Price.create(
        product=product.get('id'),
        currency="rub",
        unit_amount=int(amount * 100),
    )


def create_stripe_session(price):
    """
    Создаёт сессию на оплату.
    """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
