from django.contrib import admin
from django import forms
from river.models.transitionapproval import TransitionApproval


class TransitionApprovalForm(forms.ModelForm):
    class Meta:
        model = TransitionApproval
        exclude = ('previous',)

class TransitionApprovalAdmin(admin.ModelAdmin):
    form = TransitionApprovalForm


admin.site.register(TransitionApproval, TransitionApprovalAdmin)
