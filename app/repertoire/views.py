from django.http import Http404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from repertoire.models import Country, CountryStores, Store
from repertoire.serializers import CountrySerializer, CountryStoresSerializer, StoreSerializer


class CountryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Country.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["countryname", "stores_count"]
    ordering = ("id",)

    def get_serializer_class(self):
        return CountrySerializer


class StoreViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    ordering = ("id",)

    def get_search_fields(self):
        if self.action == "list":
            return ["storename",
                    "workers_count",
                    "square_meters",
                    "location",
                    "managers"]
        else:
            return ["country", "stores"]

    def get_queryset(self):
        current_country = CountryStores.objects.filter(country=self.kwargs['country_pk'])
        if self.action == "list":
            return current_country
        else:
            try:
                store_id = self.kwargs['pk']
                for work in current_country:
                    if work.id == CountryStores.objects.get(stores=store_id).id:
                        return Store.objects.filter(id=self.kwargs['pk'])
                    else:
                        raise Http404()
            except AttributeError:
                raise Http404()

    def get_serializer_class(self):
        if self.action == "list":
            return CountryStoresSerializer
        else:
            return StoreSerializer



