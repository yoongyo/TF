from django.shortcuts import render
from .models import Category, Post


def main(request):
    return render(request, 'travel/_main.html')

def local_list(request):
    queryset = Category.objects.all()

    queryset1 = Post.objects.all()


    return render(request, 'travel/local_list.html', {
        'local' : queryset,
        'local_list' : queryset1
    })

def local_detail(request, local):
    queryset1 = Category.objects.all()
    queryset = Post.objects.all()
    path = request.path
    print(path)
    filter = path.split('/')[3]
    print(filter)
    qs = queryset.filter(local__local_category=filter)

    return render(request, 'travel/local_detail.html',{
        'local_list': qs
    })