from django.shortcuts import render, redirect
from .models import SharedLocation
import uuid
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.http import JsonResponse

def share_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if not latitude or not longitude:
            return JsonResponse({'error': 'Invalid coordinates'}, status=400)

        location = SharedLocation.objects.create(latitude=latitude, longitude=longitude)
        return JsonResponse({'link': f'/view/{location.id}/'})
    
    return render(request, 'generate.html')

def view_location(request, id):
    location = get_object_or_404(SharedLocation, id=id)
    return render(request, 'view.html', {'sharer': location})
def save_location(request):
    import json
    data = json.loads(request.body)
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    location = SharedLocation.objects.create(latitude=latitude, longitude=longitude)
    return JsonResponse({'link': f'/view/{location.id}/'})