from django.shortcuts import render, redirect
from textbook.models import Post
from django.contrib.auth.models import User

from post.models import Message

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_sell_page(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        bookname = request.POST.get('bookname')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        post = Post.objects.create(
            text_book = bookname,
            type = 1,
            price = price,
            picture = image,
            create_by=user
        )
    return render(request, template_name='post/sell.html')

@login_required
def add_buy_page(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        bookname = request.POST.get('bookname')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        post = Post.objects.create(
            text_book = bookname,
            type = 2,
            price = price,
            picture = image,
            create_by=user
        )
    return render(request, template_name='post/buy.html')

def detail_page(request, id):
    context = {}
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            post = Post.objects.get(pk=id)
            create_by = User.objects.get(pk=request.user.id)
            msg = Message.objects.create(
                message = comment,
                post_id = post,
                create_by = create_by
            )
            return redirect('detail', id=id)
        else:
            return redirect('detail', id=id)
    else:
        if Post.objects.filter(pk=id).exists() and Post.objects.filter(pk=id).exclude(status=2): 
            detail = Post.objects.get(pk=id)
            context['detail'] = detail
            comment = Message.objects.filter(post_id=id)
            context['comment'] = comment
            if request.user.is_authenticated:
                context['show'] = True
            if detail.type == '1':
                context['type'] = "ขาย"
            else:
                context['type'] = "ซื้อ"
            if detail.create_by.id == request.user.id:
                context['close'] = True
        else:
            return redirect('index')

    return render(request, template_name='post/detail.html', context=context)

@login_required
def close_post(request, id):
    if Post.objects.filter(pk=id).exists():
        detail = Post.objects.get(pk=id)
        user = request.user.id
        if user == detail.create_by.id:
            detail.status = '2'
            detail.save()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('index')
