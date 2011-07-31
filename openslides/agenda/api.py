#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openslides.agenda.api
    ~~~~~~~~~~~~~~~~~~~~~

    Useful functions for the agenda app.

    :copyright: 2011 by the OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from openslides.system.api import config_get


def get_active_item(only_id=False):
    """
    Returns the active Item. If no item is active, or it can not find an Item,
    it raise Item.DoesNotExist

    if only_id is True, returns only the id of this item. Returns None if not Item
    is active. Does not Raise Item.DoesNotExist
    """
    from agenda.models import Item
    id = config_get("presentation", None)
    if only_id:
        if id is None:
            return None
        return int(id)
    return Item.objects.get(pk=id)


def is_summary():
    """
    True, if a summery shall be displayed
    """
    from agenda.models import Item
    try:
        get_active_item()
    except Item.DoesNotExist:
        return True
    if config_get('summary', False):
        return True
    return False

def children_list(items):
    """
    Return a list for items with all childitems in the right order.
    """
    l = []
    for item in items:
        l.append(item)
        if item.children:
            l += children_list(item.children)
    return l
