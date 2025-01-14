from django.contrib import admin
from .models import About

# Models registered:
class AboutAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'content',
  )

  ordering = ('pk',)

admin.site.register(About, AboutAdmin)