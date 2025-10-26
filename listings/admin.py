from django.contrib import admin
from .models import Listing
from django.forms import NumberInput
from django.db import models

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id','title','district','is_publish', 'rooms', 'doctor'
    list_display_links = 'id','title'
    list_filter = "doctor",
    list_editable = "is_publish","rooms"
    search_fields = "title", "district", "doctor"
    list_per_page = 25
    ordering=['-id']
    prepopulated_fields = {"title" : ('title',)}
    formfield_overrides ={
        models.IntegerField:{
        'widget' : NumberInput(attrs={'size':'10'})
        },
    }    
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Listing,ListingAdmin)