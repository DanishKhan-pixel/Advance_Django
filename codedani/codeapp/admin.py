from django.contrib import admin
from codeapp.models import*
# Register your models here
class ServiceAdmin(admin.ModelAdmin):
    list_display=("Service_icon","Service_title","Service_des")


admin.site.register(Service,ServiceAdmin)