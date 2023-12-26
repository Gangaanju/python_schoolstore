# store_app/context_processors.py

from .models import Department

def departments(request):
    departments = Department.objects.all()
    return {'departments': departments}
