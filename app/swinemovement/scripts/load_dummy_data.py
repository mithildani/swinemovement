import pandas as pd
from datetime import datetime
from django.db.models import Sum
from swinemovement.models import Species, Company, Premise, Movement
from swinemovement.models.movement import MovementReasonConstant


def load_dummy_data():
    """
        from swinemovement.scripts.load_dummy_data import load_dummy_data
        load_dummy_data()
    """
    try:
        swine = Species.objects.get(name='Swine')
    except Species.DoesNotExist:
        swine = Species.objects.create(name='Swine')
    try:
        company = Company.objects.get(name='Mypigcmopany')
    except Company.DoesNotExist:
        company = Company.objects.create(name='Mypigcmopany')

    movement_data = pd.read_csv("./data/movement.csv")
    for index, record in movement_data.iterrows():
        print(f"Adding {index}")
        try:
            origin_premise = Premise.objects.get(id=record["new_originpremid"])
        except Premise.DoesNotExist:
            origin_premise = Premise.objects.create(
                id=record["new_originpremid"],
                name=record["new_originname"],
                city=record["new_origincity"],
                address=record["new_originaddress"],
                postal_code=int(record["new_originpostalcode"]),
                state=record["new_originstate"],
                latitude=float(record["origin_Lat"]),
                longitude=float(record["origin_Lat"])
            )
        try:
            destination_premise = Premise.objects.get(id=record["new_destinationpremid"])
        except Premise.DoesNotExist:
            destination_premise = Premise.objects.create(
                id=record["new_destinationpremid"],
                name=record["new_destinationname"],
                city=record["new_destinationcity"],
                address=record["new_destinationaddress"],
                postal_code=record["new_destinationpostalcode"],
                state=record["new_destinationstate"],
                latitude=record["destination_Lat"],
                longitude=record["destination_Long"]
            )
        movement = Movement.objects.create(
            origin_premise=origin_premise,
            destination_premise=destination_premise,
            species=swine,
            company=company,
            reason=record["new_movementreason"],
            items_moved=int(record["new_numitemsmoved"]),
            shipment_start_date=datetime.strptime(record["new_shipmentsstartdate"], "%y-%m-%d").date(),
        )
    print("All movement data added")

    for premise in Premise.objects.all():
        outgoing = Movement.objects.filter(origin_premise_id=premise.id).aggregate(Sum('items_moved'))["items_moved__sum"] or 0
        incoming = Movement.objects.filter(destination_premise_id=premise.id).aggregate(Sum('items_moved'))["items_moved__sum"] or 0
        total = incoming-outgoing
        print(f"{premise.id} total animal: {total}")
        if total < 0:
            movement = Movement.objects.create(
                origin_premise=None,
                destination_premise=premise,
                species=swine,
                company=company,
                reason=MovementReasonConstant.OTHER,
                items_moved=2000,
                shipment_start_date=datetime.strptime("18-01-01", "%y-%m-%d").date(),
            )
    print("Added pre-existing population")
