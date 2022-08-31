from django.shortcuts import render

from swinemovement.cachehandlers.populationcachehandler import PopulationCacheHandler
from swinemovement.models import Premise
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view


@staff_member_required
@api_view(['GET'])
def get_population(request):
    population = []

    for premise in Premise.objects.all():
        population_cache = PopulationCacheHandler(premise_id=premise.id)
        population_cache.get_configuration()

        population.append({
            "id": premise.id,
            "name": premise.name,
            "count": population_cache.population_count
        })

    context = {
        "population": population
    }
    return render(request, '../templates/population_table.html', context=context)
