from django.contrib import admin

# Register your models here.
from blog.models import Blog
#from django.utils.html import format_html
#from django.contrib.auth.models import User


from blog.models import *
#from django.contrib import admin

admin.site.register(Author)
admin.site.register(Post)
#admin.site.register(PostCatagory)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
