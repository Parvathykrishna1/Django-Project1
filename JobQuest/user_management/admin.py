from django.contrib import admin
from .models import CustomUser
from CareerForge.models import Issue

admin.site.register(CustomUser)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('job_listing', 'description', 'reported_by', 'created_at', 'status')
    search_fields = ('job_listing__title', 'description', 'reported_by__username')
    list_filter = ('created_at', 'status')
    readonly_fields = ('created_at',)

    actions = ['mark_as_resolved']

    def mark_as_resolved(self, request, queryset):
        updated_count = queryset.update(status='resolved')
        self.message_user(request, f'{updated_count} issue(s) marked as resolved.')

    mark_as_resolved.short_description = 'Mark selected issues as resolved'