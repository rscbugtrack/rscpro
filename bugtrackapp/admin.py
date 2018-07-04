from django.contrib import admin

# Register your models here.
from bugtrackapp.models import *
from django.utils.html import format_html
from django.contrib.auth.models import User


class ModelAdmin(admin.ModelAdmin):
    """
    Abstract admin models for populating columns updated_by and created_by
    """
    exclude = ('updated_by', 'created_by',)

    def save_form(self, request, form, change):
        obj = super(ModelAdmin, self).save_form(request, form, change)

        if hasattr(obj, 'updated_by'):
            obj.updated_by = str(request.user)

        if hasattr(obj, 'created_by') and not obj.created_by:
            obj.created_by = str(request.user)

        return obj

class SysConfigAdmin(ModelAdmin):
    list_display = ('name', 'value', 'description',)
    search_fields = ('name', 'value', 'description',)
    date_hierarchy = 'created_on'


admin.site.register(SysConfig, SysConfigAdmin)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Bugtrack)
class BugtrackAdmin(admin.ModelAdmin):
    list_display = ['assigned_to','title','created_on','priority','current_status','final_status','points','img']
    list_filter = ( 'priority','created_on',)

    def img(self,obj):
        return format_html('<img src="{}" width=50,height=40 alt="*"/>'.format(obj.upload_image.url))
    img.allow_tags = True

    def get_queryset(self, request):
        qs = super(BugtrackAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(assigned_to=request.user)

    def get_actions(self, request):
        actions = super(BugtrackAdmin, self).get_actions(request)
        if request.user.is_superuser:
            return actions
        else:
            del actions['delete_selected']

    def get_readonly_fields(self, request, obj=None):
        # readonly_fields = ('admission', 'courses',)
        if request.user.is_superuser:
            return self.readonly_fields

        # readonly_fields = ('title','description','assigned_to','created_on','priority','upload_image',
        # 'reference','final_status','points',)

        return self.readonly_fields + ('title','description','assigned_to','created_on','priority','upload_image','reference','final_status','points',)