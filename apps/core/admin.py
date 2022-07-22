from django.contrib import admin

from apps.core.models import Contact, PopularClients
admin.site.site_header = "National Electronics Admin"
admin.site.site_title = "Welcome to National Electronics Admin"
admin.site.index_title = "Welcome to National Electronics Admin"
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('name','feedback','date')
class PopularClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name','image','ratting')
admin.site.register(Contact,ContactAdmin)
# admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(PopularClients,PopularClientsAdmin)
