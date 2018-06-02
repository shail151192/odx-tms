from users.models import *

class CustomAuthentication(object):
    def authenticate(self, request, username, password):
        pass

    def user(self, user_id):
        try:
            AuthUser.objects.get(pk=1)
        except User.DoesNotExist:
            pass