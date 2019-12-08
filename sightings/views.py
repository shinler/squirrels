from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from sightings.forms import SightingForm
from django.shortcuts import redirect
from .models import Sighting
from django.template import loader
from django.contrib import messages
from collections import Counter

def add(request):
    form_class = SightingForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect(f'/sightings')
    else:
         form = SightingForm()
    return render(request, 'sightings/add.html', {'form': form})

def sightings(request):
    all_sightings = Sighting.objects.all()[::-1]
    return render(request, 'sightings/sightings.html', {'all_sightings': all_sightings})

def update(request, unique_squirrel_id):
    squirrel_instance = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST or None, instance=squirrel_instance)
        if form.is_valid():
            squirrel_instance.save()
            form.save()
            return redirect(f'/sightings')
        else:
            return HttpResponseRedirect(reverse('sightings:sightings'))
    else:
        form = SightingForm(instance=squirrel_instance)
    context = {'form': form, 'squirrel_instance': squirrel_instance,}
    return render(request, 'sightings/update.html', context)

def stats(request):
    all_sightings = Sighting.objects.all()
    all_sightings_PM = Sighting.objects.filter(Shift='PM').count()
    all_sightings_AM = Sighting.objects.filter(Shift='AM').count()
    all_sightings_grey = Sighting.objects.filter(Primary_Fur_Color='Gray').count()
    all_sightings_cinnamon = Sighting.objects.filter(Primary_Fur_Color='Cinnamon').count()
    all_sightings_black = Sighting.objects.filter(Primary_Fur_Color='Black').count()
    all_sightings_running = Sighting.objects.filter(Running='true').count()
    all_sightings_ground_plane = Sighting.objects.filter(Location='Ground Plane').count()
    all_sightings_above_ground = Sighting.objects.filter(Location='Above Ground').count()
    all_sightings_adult = Sighting.objects.filter(Age='Adult').count()
    all_sightings_juvenile = Sighting.objects.filter(Age='Juvenile').count()

    context = {'all_sightings_PM': all_sightings_PM,
               'all_sightings_AM': all_sightings_AM,
               'all_sightings': all_sightings,
               'all_sightings_grey': all_sightings_grey,
               'all_sightings_cinnamon': all_sightings_cinnamon,
               'all_sightings_black': all_sightings_black,
               'all_sightings_running': all_sightings_running,
               'all_sightings_ground_plane': all_sightings_ground_plane,
               'all_sightings_above_ground': all_sightings_above_ground,
               'all_sightings_adult': all_sightings_adult,
               'all_sightings_juvenile': all_sightings_juvenile,
               }
    return render(request, 'sightings/stats.html', context)

def delete(request, unique_squirrel_id):
    squirrel_instance = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        squirrel_instance.delete()
        messages.success(request, "Sighting successfully deleted!")
        return redirect(f'/sightings')
    context = {'squirrel_instance': squirrel_instance,}
    return render(request, 'sightings/delete.html', context)

def map_(request):
    all_sightings = Sighting.objects.all()[:100]
    return render(request, 'sightings/map.html', {'all_sightings': all_sightings})
