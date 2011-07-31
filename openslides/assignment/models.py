#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openslides.assignment.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Models for the assignment app.

    :copyright: 2011 by the OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from django.db import models
from django.utils.translation import ugettext as _

from participant.models import Profile


class Assignment(models.Model):
    STATUS = (
        ('sea', _('Searching for candidates')),
        ('vot', _('Voting')),
        ('fin', _('Finished')),
    )

    name = models.CharField(max_length=100, verbose_name = _("Name"))
    description = models.TextField(null=True, blank=True, verbose_name = _("Description"))
    assignment_number = models.PositiveSmallIntegerField(verbose_name = _("Number of available posts"))
    polldescription = models.CharField(max_length=50, null=True, blank=True, verbose_name = _("Short description (for ballot paper)"))
    profile = models.ManyToManyField(Profile, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='sea')

    def set_status(self, status):
        error = True
        for a, b in Assignment.STATUS:
            if status == a:
                error = False
                break
        if error:
            raise NameError(_('%s is not a valid status.') % status)
        if self.status == status:
            raise NameError(_('The assignment status is already %s.') % self.status)
        self.status = status
        self.save()

    def run(self, profile):
        """
        run for a vote
        """
        if self.is_candidate(profile):
            raise NameError(_('<b>%s</b> is already a candidate.') % profile)
        self.profile.add(profile)

    def delrun(self, profile):
        """
        stop running for a vote
        """
        if self.is_candidate(profile):
            self.profile.remove(profile)
        else:
            raise NameError(_('%s is no candidate') % profile)

    def is_candidate(self, profile):
        if profile in self.profile.get_query_set():
            return True
        else:
            return False

    def gen_poll(self):
        from poll.models import Poll
        poll = Poll()
        poll.title = _("Election for %s") % self.name
        
        # Option A: candidates <= available posts -> yes/no/abstention
        if self.profile.count() <= self.assignment_number:
            poll.optiondecision = True
        else:
            poll.optiondecision = False
        
        # Option B: candidates == 1 -> yes/no/abstention
        #if self.profile.count() == 1:
        #    poll.optiondecision = True
        #else:
        #    poll.optiondecision = False
        
        poll.assignment = self
        poll.description = self.polldescription
        poll.save()
        for profile in self.profile.get_query_set():
            poll.add_option(profile)
        return poll

    @models.permalink
    def get_absolute_url(self, link='view'):
        if link == 'view':
            return ('assignment_view', [str(self.id)])
        if link == 'delete':
            return ('assignment_delete', [str(self.id)])

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ('can_view_assignment', "Can see the assignments"),
            ('can_nominate_other', "Can nominate another person"
                                   " for a election"),
            ('can_nominate_self', "Can nominate hisself for a election"),
            ('can_manage_assignment', "Can manage assignments"),
        )
