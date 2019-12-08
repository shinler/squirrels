from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    X = models.DecimalField(help_text=_('Longitude'), max_digits=50, decimal_places=20)
    
    Y = models.DecimalField(help_text=_('Latitude'), max_digits=50, decimal_places=20)
    
    unique_squirrel_id = models.CharField(help_text=_('unique squirrel id'), max_length=100, primary_key=True)
    
    AM = 'AM'
    PM = 'PM'
    
    SHIFT = (
            (AM,'AM'),
            (PM,'PM'),
            )
    
    Shift = models.CharField(help_text=_('Shift'), max_length=10, choices=SHIFT)
    
    Date = models.DateField(help_text=_('Date'),)
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Nil = ''
    Unknown = 'Unknown'
    
    AGE = (
          (Adult,'Adult'),
          (Juvenile,'Juvenile'),
          (Nil,''),
          (Unknown,'?'),
          )
    
    Age = models.CharField(help_text=_('Age'), max_length=50, choices=AGE, blank=True)
    
    Gray = 'Gray'
    Black = 'Black'
    Cinnamon = 'Cinnamon'
    Nil = ''
    
    Primary_Fur_Color = (
                         (Gray, 'Gray'),
                         (Black, 'Black'),
                         (Cinnamon, 'Cinnamon'),
                         (Nil, ''),
                         )
    
    Primary_Fur_Color = models.CharField(help_text=_('Primary Fur Color'), max_length=20, choices = Primary_Fur_Color, blank=True)
    
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    Nil = ''
    
    LOCATION = (
               (Ground_Plane, 'Ground Plane'),
               (Above_Ground, 'Above Ground'),
               (Nil, ''),
               )
    
    Location = models.CharField(help_text=_('Location'), max_length=100, choices = LOCATION, blank=True)
    
    Specific_Location = models.CharField(help_text=_('Specific Location'), max_length=100, blank=True)
    
    TRUE = 'True'
    FALSE = 'False'

    True_False = (
                 (TRUE, 'True'),
                 (FALSE, 'False')
                 )
    
    Running = models.CharField(help_text=_('Running'), max_length=10, choices=True_False)
    Chasing = models.CharField(help_text=_('Chasing'), max_length=10, choices=True_False)
    Climbing = models.CharField(help_text=_('Climbing'), max_length=10, choices=True_False)
    Eating = models.CharField(help_text=_('Eating'), max_length=10, choices=True_False)
    Foraging = models.CharField(help_text=_('Foraging'), max_length=10, choices=True_False)
    Other_Activities = models.CharField(help_text=_('Other Activities'), max_length=100, blank=True)
    Kuks = models.CharField(help_text=_('Kuks'), max_length=10, choices=True_False)
    Quaas = models.CharField(help_text=_('Quaas'), max_length=10, choices=True_False)
    Moans = models.CharField(help_text=_('Moans'), max_length=10, choices=True_False)
    Tail_Flags = models.CharField(help_text=_('Tail Flags'), max_length=10, choices=True_False)
    Tail_Twitches = models.CharField(help_text=_('Tail Twitches'), max_length=10, choices=True_False)
    Approaches = models.CharField(help_text=_('Approaches'), max_length=10, choices=True_False)
    Indifferent = models.CharField(help_text=_('Indifferent'), max_length=10, choices=True_False)
    Runs_From = models.CharField(help_text=_('Runs From'), max_length=10, choices=True_False)
    
    def __str__(self):
        return self.unique_squirrel_id
