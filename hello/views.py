from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse
# Create your views here.
def index(request):
  msg = request.GET['msg']
  return HttpResponse('you typed: "'+msg+'".')
>>>>>>> 0e0c10cb1f7391a224877ea39d93ad8716c47639
