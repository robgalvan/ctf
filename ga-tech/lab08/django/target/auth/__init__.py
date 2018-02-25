from django.contrib.auth.models import User

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def startup():
    # create guest/guest
    GUEST = 'guest'
    if not user_exists(GUEST):
        create_user(GUEST, GUEST)

startup()

