from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.cache import cache_page
from django.utils.encoding import force_text


# @cache_page(60 * 2)  # cache for 2 minutes
def index(request):
    template = loader.get_template('blees/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))