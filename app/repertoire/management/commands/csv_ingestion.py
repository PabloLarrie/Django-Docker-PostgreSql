import csv

from django.core.management import BaseCommand
from repertoire.models import Country, Manager, Store, CountryStores


class Command(BaseCommand):
    EEUU_csv = 'repertoire/files/EEUU.csv'
    Canada_csv = 'repertoire/files/Canada.csv'
    Spain_csv = 'repertoire/files/Spain.csv'

    def handle(self, *args, **kwargs):

        def csv_ingest(csv_file):
            stores_counter = 0
            country = Country(countryname=csv_file.title().split('/')[-1].split('.')[0])
            country.save()
            countrystores = CountryStores(country_id=country.id)
            countrystores.save()

            with open(csv_file, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    managers_list = []
                    for manager in row["managers"].split('|'):
                        managers_list.append(manager)
                        Manager.objects.get_or_create(name=manager)
                    store = Store(storename=row["storename"],
                                workers_count=row["workers_count"],
                                square_meters=row["square_meters"],
                                location=row["location"],)
                    store.save()
                    for index, manager_store in enumerate(managers_list):
                        store.managers.add(Manager.objects.get(
                            id=Manager.objects.get(name=managers_list[index]).id))
                    countrystores.stores.add(store.id)
                    stores_counter += 1

            country.stores_count = stores_counter
            country.save()

        csv_ingest(self.EEUU_csv)
        csv_ingest(self.Canada_csv)
        csv_ingest(self.Spain_csv)
