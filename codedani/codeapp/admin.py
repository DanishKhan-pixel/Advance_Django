from django.contrib import admin
from codeapp.models import*
# Register your models here
class ServiceAdmin(admin.ModelAdmin):
    list_display=("Service_icon","Service_title","Service_des")

class NewAdmin(admin.ModelAdmin):
    list_display=('new_title','new_des')

admin.site.register(Service,ServiceAdmin)
admin.site.register(New,NewAdmin)