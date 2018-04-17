from django.shortcuts import render


# Create your views here.
def allblogs(request):
    print("Blogs")
    return render(request, 'blog/allblogs.html')
