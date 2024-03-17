from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Course, User, Tag
from django.urls import path
from .dao import count_course_by_cate
# Register your models here.


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

    def get_urls(self):
        return [
                   path('course-stats/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        stat = count_course_by_cate()
        return TemplateResponse(request,
                                'admin/course-stats.html', {'stat':stat})


admin_site = CourseAppAdminSite(name='myadmin')


class CourseTagInlineAdmin(admin.TabularInline):
    model = Course.tags.through

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    search_fields = ['subject']
    list_filter = ['id', 'subject']
    readonly_fields = ['ava']
    form = CourseForm
    inlines = [CourseTagInlineAdmin]
    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(User)
admin_site.register(Tag)