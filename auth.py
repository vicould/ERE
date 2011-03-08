# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.conf import settings

import ldap

class LDAPBackend(object):
    """A simple LDAP authentication backend, from brutasse"""
    def authenticate(self, username=None, password=None):
        if not self.is_valid(username, password):
            return None

        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def is_valid(self, username, password):
        if password is None or password == '':
            return False

        try:
            l = ldap.initialize(settings.LDAP_SERVER) # ldap://localhost
            dn = 'uid=%s,ou=people,dc=emse,dc=fr' % username
            try:
                password = password.decode('utf-8')
            except UnicodeEncodeError:
                pass
            l.simple_bind_s(dn, password)
            l.unbind_s()
            return True
        except ldap.LDAPError as e:
            print e
            return False


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
