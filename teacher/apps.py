from django.apps import AppConfig

class TeacherConfig(AppConfig):
    name = 'teacher'

    def ready(self):
        from django.db.models.signals import post_migrate
        from core.commands import load_initial_data
        post_migrate.connect(load_initial_data, sender=self)