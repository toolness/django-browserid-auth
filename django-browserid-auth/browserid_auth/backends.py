import urllib
import urllib2

from django.contrib.auth.models import User
from django.utils import simplejson as json

# TODO: This should be a setting.
VERIFICATION_SERVER = 'https://browserid.org/verify'

class BrowserIdBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, assertion=None, email=None, host=None, port=None):
        qs = urllib.urlencode({'assertion': assertion,
                               'audience': '%s:%s' % (host, port)})
        response = urllib2.urlopen('%s?%s' % (VERIFICATION_SERVER, qs))
        result = json.loads(response.read())
        if result['status'] == 'okay':
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                user = User(username=email, password='nonexistent')
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
