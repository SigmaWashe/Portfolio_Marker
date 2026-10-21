from django.contrib import admin
from .models import Teacher, Student, Tests, Marks

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Tests)
admin.site.register(Marks)
