# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from datetime import date

from django import forms
from django.db import models
from django.http import Http404, HttpResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format



import wagtail
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.models import Image
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

#from blog.blocks import TwoColumnBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
#from wagtailmd.utils import MarkdownField, MarkdownPanel

class MarcasPage(Page):
    descripcion = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('descripcion', classname="full")
    ]

class PostPage(Page):

    nombremarca = RichTextField(blank=True)
    body = RichTextField(blank=True)
    categories  =  ParentalManyToManyField('marcas.MarcasCategory', blank = True)

    imagen = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [

        FieldPanel('nombremarca', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('imagen'),
        FieldPanel('categories', widget = forms.CheckboxSelectMultiple),
    ]



@register_snippet
class MarcasCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class MarcasPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='post_tags')


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
