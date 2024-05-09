from django.shortcuts import render
from .models import Page, Text


# Create your views here.
def page_view(request, url, child_url=None):
    try:
        page = Page.objects.get(url=child_url)
        text = Text.objects.filter(page_id=page.id).first()
    except:
        page = Page.objects.get(url=url)
        text = Text.objects.filter(page_id=page.id).first()
    return render(request, 'content/page.html', {'page': page,
                                                                     'text': text})
