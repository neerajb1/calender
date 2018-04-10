# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Event
import datetime
import calendar
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from .utils import EventCalendar

# Create your views here.

class calender(TemplateView):
    models = Event
    template_name = "event_list.html"
