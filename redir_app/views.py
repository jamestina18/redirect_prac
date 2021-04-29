from django.shortcuts import render, redirect


def index(request):
     return render (request, 'index.html')

def add_user(request):
     if request.method == "POST":
          request.session ['fname'] = request.POST['fname']
          request.session ['lname'] = request.POST['lname']
          request.session ['loc'] = request.POST['loc']
          request.session ['type'] = request.POST['type']
          request.session ['campus'] = request.POST['campus']
          return redirect('/show')
def show(request):
    return render(request, 'show.html')     

