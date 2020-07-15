# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.search.models import Query
from home.models import CopyWritingSettings


def home(request):
    social_media_setting = CopyWritingSettings.for_site(request.site)
    context = {'social_media_setting': social_media_setting}
    return render(request, 'home/home_page.html', context=context)


def search(request):
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'home/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })