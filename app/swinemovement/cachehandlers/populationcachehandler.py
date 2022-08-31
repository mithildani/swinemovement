from django.db.models import Sum
from swinemovement.adapters.rediscacheadapter import RedisCacheAdapter
from swinemovement.cachehandlers.basecachehandler import BaseCacheHandler
from swinemovement.models import Movement


class PopulationCacheHandler(BaseCacheHandler):
    """
    Stores Count of Total Population for a particular premise id
    """

    BASE_KEY = "v1_population_{premise_id}"
    TIMEOUT = 60 * 60 * 1   # 1 hour
    MACHINE_ALIAS = "default"

    def __init__(self, premise_id):
        self.premise_id = premise_id
        self.key = PopulationCacheHandler.BASE_KEY.format(premise_id=self.premise_id)
        super().__init__(
            self.key,
            PopulationCacheHandler.TIMEOUT,
            PopulationCacheHandler.MACHINE_ALIAS,
        )

        self.population_count = None

    def get_configuration(self):
        _cached_content = RedisCacheAdapter.get(
            self.key,
            machine_alias=PopulationCacheHandler.MACHINE_ALIAS,
        )

        if _cached_content:
            print(f"PopulationCacheHandler: {self.key} From Cache")
            self.population_count = _cached_content["population_count"]
        else:
            print(f"PopulationCacheHandler: {self.key} From DB")
            try:
                outgoing = Movement.objects.filter(origin_premise_id=self.premise_id).aggregate(Sum('items_moved'))[
                               "items_moved__sum"] or 0
                incoming = Movement.objects.filter(destination_premise_id=self.premise_id).aggregate(Sum('items_moved'))[
                               "items_moved__sum"] or 0
                self.population_count = int(incoming - outgoing)
                print(f"{self.premise_id} total animal: {self.population_count}")
                self._save_config_to_cache()
            except:
                print("Error in PopulationCacheHandler")

    def _save_config_to_cache(self):
        _cache_content = {
            "population_count": self.population_count,
        }
        self.set_configuration(_cache_content)
