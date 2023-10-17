from random import choices
from homework2app.models import User, Product, Order
from django.core.management.base import BaseCommand


LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeatquasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake data."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        products_list = []

        for i in range(1, count + 1):
            product = Product(name=f'Product_{i}',
                              description=" ".join(choices(text, k=64)),
                              price=i * 100,
                              count=i * 5)
            product.save()
            products_list.append(product)

            user = User(name=f'User_{i}',
                        email=f'mail{i}@mail.ru',
                        msisdn=f'+7{str(i) * 10}',
                        address='Moscow')
            user.save()

            order = Order(client=user, sum_price=product.price)
            order.save()
            order.products.set(choices(products_list, k=3))
            order.save()
