# Generated by Django 3.0.8 on 2020-07-03 19:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marcas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MarcaPage',
            new_name='MarcasPage',
        ),
    ]
