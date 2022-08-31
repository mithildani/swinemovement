from django.shortcuts import render
from django.db.models import Sum
from swinemovement.models import Premise, Movement
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view


@staff_member_required
@api_view(['GET'])
def get_population(request):
    population = []

    for premise in Premise.objects.all():
        outgoing = Movement.objects.filter(origin_premise_id=premise.id).aggregate(Sum('items_moved'))["items_moved__sum"] or 0
        incoming = Movement.objects.filter(destination_premise_id=premise.id).aggregate(Sum('items_moved'))["items_moved__sum"] or 0
        total = incoming-outgoing
        population.append({
            "id": premise.id,
            "name": premise.name,
            "count": total
        })
        print(f"{premise.id} total animal: {total}")

        context = {
            "population": population
        }
    return render(request, '../templates/population_table.html', context=context)
