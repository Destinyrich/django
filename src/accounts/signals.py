from django.db.models.signals import Signal

user_logged_in = Signal()

# from django.dispatch import Signal


# user_logged_in = Signal(providing_args=['instance', 'request'])