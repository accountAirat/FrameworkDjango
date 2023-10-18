import logging

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User, Order, Product
from .forms import ImageForm

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    page = '<h1>ДЗ2</h1>'
    return HttpResponse(page)


def all_users(request):
    logger.info('All page accessed')
    users = User.objects.all()
    page = '<h1>Все пользователи</h1>\n<p>' + '<br/>'.join([str(i) for i in users]) + '</p>'
    return HttpResponse(page)


def get_user_ordered_products(request, user_id):
    logger.debug(f'get_user_ordered_products start {user_id = }')
    orders = Order.objects.filter(client=user_id).order_by('date_ordered')
    logger.debug(f'{orders = }')
    # products = []
    #
    # for i in orders:
    #     temp = i.products.all()
    #     logger.debug(f'{temp = }')
    #     for j in temp:
    #         products.append(j)

    # logger.debug(f'{products = }')
    return render(request, 'homework2app/products.html', {'orders': orders})


def add_image_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.image = image.name
            product.save()
    else:
        form = ImageForm()
    return render(request, 'homework2app/product_image.html', {'form': form, 'product': product})
