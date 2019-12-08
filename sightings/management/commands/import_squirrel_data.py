import re
from sightings.models import Sighting
from django.core.management.base import BaseCommand, CommandError
from datetime import date
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csvfile',nargs='+', type=str)
    def handle(self, *args, **options):
        filepath = options['csvfile'][0]
        import os
        import csv
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',')
            list_ = []
            count = 0
            for line in reader:
                m,d,y = re.match(pattern, line['Date']).groups()
                if line['Unique Squirrel ID'] in list_:
                    continue
                else:
                    list_.append(line['Unique Squirrel ID'])
                    s = Sighting(X=line['X'],
                        Y=line['Y'],
                        unique_squirrel_id=line['Unique Squirrel ID'],
                        Shift=line['Shift'],
                        Date=date(int(y),int(m),int(d)),
                        Age = line['Age'],
                        Primary_Fur_Color = line['Primary Fur Color'],
                        Location = line['Location'],
                        Specific_Location = line['Specific Location'],
                        Running = line['Running'],
                        Chasing = line['Chasing'],
                        Climbing = line['Climbing'],
                        Eating = line['Eating'],
                        Foraging = line['Foraging'],
                        Other_Activities = line['Other Activities'],
                        Kuks = line['Kuks'],
                        Quaas = line['Quaas'],
                        Moans = line['Moans'],
                        Tail_Flags = line['Tail flags'],
                        Tail_Twitches = line['Tail twitches'],
                        Approaches = line['Approaches'],
                        Indifferent = line['Indifferent'],
                        Runs_From = line['Runs from'])
                    s.save()
                    count = count+1
            print(count)
