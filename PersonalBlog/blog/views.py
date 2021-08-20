from django.views import generic
from django.shortcuts import render
from .models import Post, Contact


def contact(request):
    context = {'success': False}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Textarea = request.POST['Textarea']
        ins = Contact(name=name, email=email, phone=phone, Textarea=Textarea)
        ins.save()
        context = {'success': True}

    return render(request, 'contact.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
