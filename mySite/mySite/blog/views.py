from django.shortcuts import render_to_response
from .models import Post
from django.db.models import Q



def search(request):
    query = request.GET.get("search_bar", "")
    if query:
        qset = (Q(title__icontains=query) | Q(topic__title__icontains=query))
        results = Post.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search_results.html", {"query":query, "results":results})

def django_handler(request, slug):
    return  render_to_response("django/%s.html"%slug)
