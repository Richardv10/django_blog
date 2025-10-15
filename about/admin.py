from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from about.models import About
# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    #list_display = ('title', 'content','updated_on')
    summernote_fields = ('content',)


# Register your models here.


# admin.site.register(About) "You don't need this as the decorator is doing that, absolute wally!"