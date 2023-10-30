from django.contrib import admin
from django import forms
from river.models.transition import Transition


class TransitionForm(forms.ModelForm):
    class Meta:
        model = Transition

class TransitionAdmin(admin.ModelAdmin):
    form = TransitionForm
    fields = '__all__'


admin.site.register(Transition, TransitionAdmin)
