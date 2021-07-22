from django.contrib import admin
from .models import StudentDetail, GuardianDetail
from django.contrib import messages


admin.site.register(GuardianDetail)



class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'standard',
        'evaluation',
        'active',
        'joined_on'
    ]
    # fieldsets = (
    #     (None, {'fields': ['first_name', 'last_name']}),
    #     ('Availability', {'fields': ['standard', 'evaluation', 'city']})
    # )
    list_filter = ['active']
    list_editable = ['standard']
    search_fields = ('first_name', 'last_name')

    def active(self, obj):
        return obj.active == 1

    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(active=1)
        messages.success(
            request, "Selected Record(s) Marked as Active Successfully !!"
        )

    def make_inactive(modeladmin, request, queryset):
        queryset.update(active=0)
        messages.success(
            request, "Selected Record(s) Marked as Inactive Successfully !!"
        )

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

    

admin.site.site_header = 'Detail Admin'
admin.site.register(StudentDetail, StudentAdmin)
