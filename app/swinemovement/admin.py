from django.contrib import admin
from swinemovement.models.premise import Premise
from swinemovement.models.company import Company
from swinemovement.models.species import Species
from swinemovement.models.movement import Movement


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class PremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'postal_code', 'state', 'latitude', 'longitude')


class MovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin_premise_id', 'destination_premise_id',
                    'get_species', 'get_company', 'reason',
                    'items_moved', 'shipment_start_date')

    @admin.display(ordering='species__name', description='Species')
    def get_species(self, obj):
        return obj.species.name

    @admin.display(ordering='company__name', description='Company')
    def get_company(self, obj):
        return obj.company.name


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Premise, PremiseAdmin)
admin.site.register(Movement, MovementAdmin)
