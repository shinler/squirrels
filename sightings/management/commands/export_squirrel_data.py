import csv
import pandas as pd
import re
from sightings.models import Sighting
from django.core.management.base import BaseCommand, CommandError
import dateutil.parser
from datetime import date
from sightings.forms import SightingForm
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csvfile',nargs='+', type=str)
    def handle(self, *args, **options):
        filepath = options['csvfile'][0]
        import os
        with open(filepath, 'w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            field_names = [f.name for f in Sighting._meta.fields]
            field_names = field_names[1:]
            writer.writerow(field_names)
            count = 0
            for instance in Sighting.objects.all():
                writer.writerow(getattr(instance, f) for f in field_names)
                count = count+1
            print(count)
            csvFile.close()
