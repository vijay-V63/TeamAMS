from django.contrib import admin
from .st import St
from .category import Category
from .alumni import Alumni
from .realalumni import Realalumni
from .studentreg import Studentreg
# Register your models here.

class Categoryinfo(admin.ModelAdmin):
    list_display=["name"]

class Stinfo(admin.ModelAdmin):
    list_display=["name","regdno"]

class Alumniinfo(admin.ModelAdmin):
    list_display=["name","mobileno","email"]
class Realalumniinfo(admin.ModelAdmin):
    list_display=["name","mobileno","email"]

class Studentreginfo(admin.ModelAdmin):
    list_display=["name","regdno","dept"]


admin.site.register(St,Stinfo)
admin.site.register(Category,Categoryinfo)
admin.site.register(Alumni,Alumniinfo)
admin.site.register(Realalumni,Realalumniinfo)
admin.site.register(Studentreg,Studentreginfo)