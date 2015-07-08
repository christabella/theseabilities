from django.shortcuts import render

# Create your views here.
def index(request):

    # stories = Story.objects.all().order_by('-created')[:4]

    return render(request, 'index.html', {})