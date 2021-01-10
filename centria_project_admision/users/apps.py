from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "centria_project_admision.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import centria_project_admision.users.signals  # noqa F401
        except ImportError:
            pass
