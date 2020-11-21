from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import account.signals
