from django.contrib import admin
from django.forms import ModelChoiceField
# Register your models here.
from .models import *


class PonicsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='ponics'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SeedsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='seeds'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Ponic, PonicsAdmin)
admin.site.register(Seed, SeedsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)

