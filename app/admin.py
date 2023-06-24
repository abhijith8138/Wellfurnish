from django.contrib import admin

# Register your models here.
from app.models import *
class BlindsAdmin(admin.ModelAdmin):
    list_display =('name','about',)
class BedAdmin(admin.ModelAdmin):
    list_display =('name','about')
class CurtainsAdmin(admin.ModelAdmin):
    list_display = ('name','about')
class DoorlockAdmin(admin.ModelAdmin):
    list_display = ('name','about')
class SofaAdmin(admin.ModelAdmin):
    list_display = ('name','about')

admin.site.register(Blinds,BlindsAdmin)
admin.site.register(Bed,BedAdmin)
admin.site.register(Curtains,CurtainsAdmin)
admin.site.register(Doorlock,DoorlockAdmin)
admin.site.register(Sofa,SofaAdmin)
