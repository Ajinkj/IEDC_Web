from django.contrib import admin

# Register your models here.
from .models import iedcinfo, milestone,events,all_photos,form_msg



admin.site.register(iedcinfo)
admin.site.register(milestone)
admin.site.register(events)
admin.site.register(all_photos)
admin.site.register(form_msg)


