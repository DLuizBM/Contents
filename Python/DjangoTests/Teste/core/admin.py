from django.contrib import admin
from .models import Person, Admin, Evaluation
# Register your models here.


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'grade',)
