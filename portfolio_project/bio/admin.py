from django.contrib import admin
# Register your models here.
from .models import Bio

admin.site.register(Bio)

admin.site.site_header = "Awais Portfolio Admin"
admin.site.site_title = " Dashboard"
admin.site.index_title = " Welcome to My Portfolio Panel"

