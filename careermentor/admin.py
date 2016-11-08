from django.contrib import admin
from . import models

admin.AdminSite.site_header="OpenHouse 管理後台"
admin.AdminSite.site_title="OpenHouse"
admin.AdminSite.index_template="admin/admin_index.html"

class SignupInline(admin.TabularInline):
    model = models.Signup
    extra = 0
# Register your models here.
@admin.register(models.Mentor)
class CareerMentorAdmin(admin.ModelAdmin):
    inlines = (SignupInline,)
    list_display=('title', 'company', 'date','start_time','end_time',
                  'mentor', 'place','limit', 'updated' )

@admin.register(models.Signup)
class CareerSignupAdmin(admin.ModelAdmin):
    list_display=('mentor', 'name', 'student_id','dep','phone',
                  'email', 'time_available','question', 'updated' )

