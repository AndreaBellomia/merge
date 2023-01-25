from django.shortcuts import render
from django.views.generic          import ListView

# Create your views here.



def user_profile_view(request):
    ''' 
    View della UserPorfile page del sito 
    '''

    
    return render(request, "index.html", )
