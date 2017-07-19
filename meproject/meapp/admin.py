from django.contrib import admin
from meapp.models import AtmosLog
# Register your models here.
class AtmosLogAdmin(admin.ModelAdmin):
	list_display=[f.name for f in AtmosLog._meta.fields]
admin.site.register(AtmosLog,AtmosLogAdmin)