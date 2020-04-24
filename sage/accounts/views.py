from django.shortcuts import render
from django.http import HttpResponse # To send raw HTTP Response-Remove is if not required ~subrat

# Create your views here.

# Temp data for testing: REMOVE ~subrat
data = {
        "fname": "subrat",
        "lname": "prasad",
        "email": "subrat@sage.com",
        "rank": 1,
        "badge":"Great Sage",
    }

# Profile View for the users profile
# Profile/id will be actual URL once the database is functional ~subrat
def profile(request):
    return render(request, "accounts/profile.html",{
        "data": data,
    })