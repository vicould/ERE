# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.conf import settings

import ldap

class LDAPBackend(object):
    """A simple LDAP authentication backend, inspired by brutasse"""
    def authenticate(self, username=None, password=None):
        if not self.is_valid(username, password):
            return None

        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            l = ldap.initialize(settings.LDAP_SERVER)
            dn = 'uid=%s,ou=people,dc=emse,dc=fr' % username
            first_name, last_name, mail = l.search_s(dn, ldap.SCOPE_BASE,
                                               'objectClass=*',\
 ['givenName', 'initials', 'mail'])[0][1].values()
            user = User.objects.create_user(username,
                                            mail[0],
                                            password=password)
            user.first_name = first_name[0]
            user.last_name = last_name[0].capitalize()
            user.save()
            l.unbind_s()
            return user

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
            return False


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
