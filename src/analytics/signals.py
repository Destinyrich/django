from django.db.models.signals import Signal

object_viewed_signal = Signal()


# from django.dispatch import Signal


# object_viewed_signal = Signal(providing_args=['instance', 'request'])