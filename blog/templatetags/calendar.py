# -*- coding: utf-8 -*-
from django import template

register = template.Library()

import datetime
from ere.blog.models import Meeting

class MeetingLlistNode(template.Node):
    """Defines the meeting list. It gets the variable name to use directly from
    the template as the user defined it."""
    def __init__(self, var_name):
        self.var_name = var_name

    def get_current_5(self):
        """Gets current 5 objects"""
        raw_meeting_list = Meeting.objects.all()
        "TODO filter the meetings to get all the recent entries"
        meeting_list = []
        i = 0
        now = datetime.datetime.now()
        for meeting in raw_meeting_list:
            if (i == 5):
                break
            else:
                if (now < meeting.date):
                    meeting_list.append(meeting)
            
        return meeting_list

    def render(self, context):
        context[self.var_name] = self.get_current_5()
        return ''


import re

@register.tag('upcoming_meetings')
def get_meeting_list(parser, token):
    """Parses the content of the token before calling the Node class."""
    try:
        # Splitting by None == splittinh by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag syntax is to only specify \
    the variable name " % token.contents.split()[0]
    if (arg.split().__len__() > 2):
        raise template.TemplateSyntaxError, "%s tag requires no argument" % \
    tag_name
    var_name = arg.split()[1]
    return MeetingLlistNode(var_name)
 
