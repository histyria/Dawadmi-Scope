from django.contrib import admin

# Register your models here.
from .models import *
from .forms import Support_TeamForm

admin.site.register(User)
admin.site.register(Cloud_Site)
admin.site.register(DEPARTEMNTS)
admin.site.register(Profile)
admin.site.register(User_Role)



from django.shortcuts import render , get_object_or_404


from home.models import *
@admin.register(Section_Support_Team)
class Section_Support_TeamAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(Section_Support_TeamAdmin, self).get_form(request, obj=None, **kwargs)
        print(request.user)
        form.base_fields['Section_Name'].queryset = DEPARTEMNTS.objects.filter(id = request.user.DEPARTEMNT.id)
        form.base_fields['Mempers'].queryset = User.objects.filter(DEPARTEMNT__id = request.user.DEPARTEMNT.id)
        return form