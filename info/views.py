from django.shortcuts import render
from .models import Pornstar, Category, UploadMedia

# Create your views here.
def index(request):
    num_pornstars=Pornstar.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_pornstars'},
    )