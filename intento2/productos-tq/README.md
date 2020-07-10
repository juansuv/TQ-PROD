## Introduction

[![Build Status](https://travis-ci.org/AccordBox/wagtail-bootstrap-marcas.svg?branch=master)](https://travis-ci.org/AccordBox/wagtail-bootstrap-marcas)

This project is developed exclusively for Wagtail Tutorial [Build Marcas With Wagtail CMS](https://www.accordbox.com/marcas/wagtail-tutorials/), which shows people how to create a Wagtail marcas using Bootstrap step by step. You can also import it into your Django project to quickly add professional marcas function based on Wagtail.

## Project Detail

* Python 3
* Django 2
* Wagtail 2
* Bootstrap 4

## Live Demo

I have deployed a live Wagtail Marcas Demo on Heroku, you can check it [Wagtail Marcas Live Demo](http://wagtail-bootstrap-marcas.accordbox.com/marcas/).

The admin page of this live demo is [marcas admin](http://wagtail-bootstrap-marcas.accordbox.com/admin/pages/4/) , you can use `admin:admin` to login and publish articles as you like.

**The database and media files would be reset after a while, so do not be surprised if your article is gone.**

## Run it in local env

```bash
git clone https://github.com/michael-yin/wagtail-bootstrap-marcas.git
cd wagtail-bootstrap-marcas
git checkout master

# setup virtualenv
pip install -r requirements.txt

./manage.py runserver
# http://127.0.0.1:8000/marcas
# username: admin  password: admin
```

If you have any problem with your Wagtail project you can [contact me](https://www.accordbox.com/contact/)

## ScreenShot

![](https://marcas.michaelyin.info/upload/images/wagtail-demo-live-screenshot-bootstrap4.original.jpg)

