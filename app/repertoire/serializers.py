from rest_framework import serializers

from repertoire.models import Country, Store, CountryStores


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [
            "id",
            "countryname",
            "stores_count",
        ]


class StoreSerializer(serializers.ModelSerializer):
    managers = serializers.SerializerMethodField()

    def get_managers(self, object):
        managers_list = []
        for manager in object.managers.all():
            managers_list.append(manager.name)
        return managers_list

    class Meta:
        model = Store
        fields = [
            "id",
            "storename",
            "workers_count",
            "square_meters",
            "location",
            "managers",
        ]
        read_only_fields = [
            "id",
            "storename",
            "workers_count",
            "square_meters",
            "managers",
        ]


class CountryStoresSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    stores = StoreSerializer(many=True)
    country = CountrySerializer()

    def get_count(self, object):
        return object.stores.all().count()

    class Meta:
        model = CountryStores
        fields = [
            "count",
            "stores",
            "country",
        ]
