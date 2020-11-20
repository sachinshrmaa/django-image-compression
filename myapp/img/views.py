from django.shortcuts import render
from .models import Upload



# Create your views here.
def all_post_view(request):

    obj = Upload.objects.all()

    context = {
        'imgs':obj
    }

    return render(request, "post.html", context)