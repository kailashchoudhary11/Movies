from django.shortcuts import render
from django.views import View
from .helper import apology, get_movie_data
from .models import Saved
# Create your views here.

class MovieDetails(View):
    def get(self, request):
        return render(request, "moviedetails/index.html")
    
    def post(self, request):
        q = request.POST.get("q").lower()
        data = get_movie_data(q)
        if data.get("Response") == "False":
            return apology(request, data.get("Error"))
        
        context = {
            "data": data,
        }
        try: 
            Saved.objects.get(name=q)
        except Exception:
            Saved.objects.create(name=q)    
        return render(request, "moviedetails/detail.html", context)
    
def saved(request):
    movies = []
    try:
        names = Saved.objects.all()
        for name in names:
            movies.append(get_movie_data(name.name))
    except Exception:
        movies = None
    
    context = {
        "movies": movies
    }
        
    return render(request, "moviedetails/saved.html", context)
    
        