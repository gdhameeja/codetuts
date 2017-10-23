from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")
def search(request):
    return render_to_response("search_results.html")