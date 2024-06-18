from django.contrib import admin
from .models import ChaiVariety,ChaiStore,ChaiReview,ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "chai_type", "date_added")
    inlines = [ChaiReviewInline]

class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(ChaiStore, ChaiStoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)