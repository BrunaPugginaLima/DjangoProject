from django.contrib import admin

from .models import Vlan

from .models import Subnet

admin.site.register(Vlan)
admin.site.register(Subnet)

#comment

#Register your models here.admin.site.register()