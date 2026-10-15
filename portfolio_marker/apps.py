from django.apps import AppConfig, apps

class PortfolioMarkerConfig(AppConfig):
    name = 'portfolio_marker'

    def ready(self):
        from django.db.models.signals import post_migrate
        from core.commands import load_initial_data
        post_migrate.connect(load_initial_data, sender=apps.get_app_config('common'))