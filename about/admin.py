from django.contrib import admin
from .models import About, Testimonial

# Models registered:
class AboutAdmin(admin.ModelAdmin):
  list_display = (
    'title',
    'content',
  )

  ordering = ('pk',)

admin.site.register(About, AboutAdmin)

admin.site.register(Testimonial)