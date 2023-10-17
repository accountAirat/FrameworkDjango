import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    page = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return HttpResponse(page)


def about(request):
    logger.info('About page accessed')
    poem = ['Я программист, осознавший едва',
            'Всю суть программистских контор.',
            'Я миддл опять в мои двадцать два,',
            'А в двадцать один был сеньор',
            ]
    page = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return HttpResponse(page)
