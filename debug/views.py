# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext, Context


def main_debug(request):
    debug_dict = {'host' : request.get_host(),
                  'path' : request.get_full_path(),
                 }
    return render_to_response('debug/debug_index.html', 
                              { 'debug_dict' : debug_dict },
                              context_instance=RequestContext(request))

