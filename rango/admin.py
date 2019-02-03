from django.contrib import admin
from rango.models import Category 
from rango.models import Page
from rango.models import UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
