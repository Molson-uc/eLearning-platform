from django.contrib import admin
from .models import Subject, CourseModule, Course


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


class ModuleInline(admin.StackedInline):
    model = CourseModule


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "created")
    list_filter = ("title", "created")
    search_fields = ("title", "subject")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ModuleInline,
    ]
