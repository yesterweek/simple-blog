#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import datetime

from mongoengine import Document, BooleanField, EmailField, FileField, \
                        DateTimeField, ListField, ImageField, IntField, \
                        StringField, SequenceField, URLField, ReferenceField

class ImageDoc(Document):
    
    id_no = SequenceField()
    description = StringField()
    # image = ImageField(thumbnail_size=(120, 100, True))
    image = FileField()
    url = StringField()
    creat_time = DateTimeField(default=datetime.datetime.now)


class User (Document):
    
    id_no = SequenceField()
    name = StringField()
    email = EmailField(required=True, unique= True)
    pass_word = StringField()


class Category(Document):

    id_no = SequenceField()
    creat_time = DateTimeField(default=datetime.datetime.now)
    name = StringField(unique=True)
    description = StringField()


class BaseArticle(Document):
    
    id_no = SequenceField()
    title = StringField(required=True)
    creat_time = DateTimeField(default=datetime.datetime.now)
    md_content = StringField()
    html_content = StringField()
    img_list = ListField(StringField(), default=[])
    is_del = IntField(default=0, choices=(0, 1))
    
    meta = {
        'allow_inheritance': True,
        'abstract': True,
    }

class Article(BaseArticle):

    category = ReferenceField('Category')
    translate = StringField()
    active = IntField(default=1, choices=(0, 1))
    
    meta = {
        'collection': 'article',
        'allow_inheritance': True,
        'ordering' : ['-creat_time'],
    }


class Novel(Document):

    id_no = SequenceField()
    creat_time = DateTimeField(default=datetime.datetime.now)
    name = StringField(unique=True)
    description = StringField()


class Chapter(BaseArticle):

    active = IntField(default=1, choices=(0, 1))
    novel = ReferenceField('Novel')
    meta = {
        'collection': 'chapter'
    }


class SiglePage(BaseArticle):

    slug = StringField(unique=True)
    translate = StringField()
    meta = {
        'collection': 'page'
    }


class Quote (Document):
    
    id_no = SequenceField()
    body = StringField(required=True, unique=True)
    author = StringField()
    creat_time = DateTimeField(default=datetime.datetime.now)
    
    meta = {
        'ordering' : ['-creat_time'],
    }
