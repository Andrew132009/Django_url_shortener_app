from django.shortcuts import render, redirect
from .models import Links, Clicks


# Create your views here.


def redirect_url(request, short_url):
    try:
        url = Links.objects.get(short_url=short_url)
    except Links.DoesNotExist:
        return render(request, '404.html')
    print(request.META)
    url.clicks_qty += 1
    url.save()
    click = Clicks(
        link_id=url,
        ip_address=request.META['REMOTE_ADDR'],
        user_agent=request.META['HTTP_USER_AGENT']
    )
    click.save()
    return redirect(url.original_url)
