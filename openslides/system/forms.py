#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openslides.system.forms
    ~~~~~~~~~~~~~~~~~~~~~~~

    Forms for the system app.

    :copyright: 2011 by the OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from django.forms import Form, CharField, TextInput, BooleanField, IntegerField
from django.utils.translation import ugettext as _
from system.api import config_get

class SystemConfigForm(Form):
    error_css_class = 'error'
    required_css_class = 'required'
    
    user_registration = BooleanField(label=_("User registration"), required=False)

class EventConfigForm(Form):
    error_css_class = 'error'
    required_css_class = 'required'
    
    event_name = CharField(widget=TextInput(),label=_("Event name"), max_length=30)
    event_description = CharField(widget=TextInput(),label=_("Short description of event"), max_length=100, required=False)
    event_date = CharField(widget=TextInput(), required=False, label=_("Event date"))
    event_location = CharField(widget=TextInput(), required=False, label=_("Event location"))
    event_organizer = CharField(widget=TextInput(), required=False, label=_("Event organizer"))

class ApplicationConfigForm(Form):
    error_css_class = 'error'
    required_css_class = 'required'

    application_min_supporters = IntegerField(widget=TextInput(attrs={'class':'small-input'}),label=_("Number of (minimum) required supporters for a application"),initial=4, min_value=0, max_value=8)
    application_preamble = CharField(widget=TextInput(), required=False, label=_("Application preamble"))
    