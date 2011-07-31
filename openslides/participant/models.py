#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openslides.participant.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Models for the participant app.

    :copyright: 2011 by the OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Profile(models.Model):
    GENDER_CHOICES = (
        ('none', _('Not specified')),
        ('male', _('Male')),
        ('female', _('Female')),
    )
    TYPE_CHOICE = (
        ('delegate', _('Delegate')),
        ('guest', _('Guest')),
        ('observer', _('Observer')),
        ('staff', _('Staff')),
    )

    user = models.OneToOneField(User, unique=True, editable=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='none', verbose_name = _("Gender"))
    group = models.CharField(max_length=100, null=True, blank=True, verbose_name = _("Group"))
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, default='delegate', verbose_name = _("Typ"))
    committee = models.CharField(max_length=100, null=True, blank=True, verbose_name = _("Committee"))

    def __unicode__(self):
        if self.group:
            return "%s (%s)" % (self.user.get_full_name(), self.group)
        return "%s" % self.user.get_full_name()


    class Meta:
        permissions = (
            ('can_view_participants', "Can see the list of participants"),
            ('can_manage_participants', "Can manage the participant list"),
        )
