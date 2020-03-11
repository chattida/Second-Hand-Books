from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from textbook.models import Post

from django.contrib.auth.decorators import login_required

# Create your views here.
def index_page(request):
    context = {}
    if request.method == "POST":
        sell_search = request.POST.get('sell_search')
        buy_search = request.POST.get('buy_search')
        if sell_search:
            context['sell_search'] = sell_search
            sell_list = Post.objects.filter(type=1, text_book__icontains=sell_search).exclude(status=2)
            context['sell_list'] = sell_list
            #แสดงหนังสือ
            buy_list = Post.objects.filter(type=2).exclude(status=2)
            context['buy_list'] = buy_list
        elif buy_search:
            context['buy_search'] = buy_search
            buy_list = Post.objects.filter(type=2, text_book__icontains=buy_search).exclude(status=2)
            context['buy_list'] = buy_list

            sell_list = Post.objects.filter(type=1).exclude(status=2)
            context['sell_list'] = sell_list

        else:
            sell_list = Post.objects.filter(type=1).exclude(status=2)
            buy_list = Post.objects.filter(type=2).exclude(status=2)
            context['sell_list'] = sell_list
            context['buy_list'] = buy_list
    else:
        sell_list = Post.objects.filter(type=1).exclude(status=2)
        buy_list = Post.objects.filter(type=2).exclude(status=2)
        context['sell_list'] = sell_list
        context['buy_list'] = buy_list
    return render(request, template_name='textbook/index.html', context=context)

def login_page(request):
    context = {}
    # เช็คว่า login หรือยัง
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #เปรียบเทียบ username, password ใน database ว่าตรงมั้ย
        user = authenticate(request, username=username, password=password)
        next_url = request.POST.get('next_url')
        if user:
            login(request, user)

            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'บัญชีผู้ใช้ หรือ รหัสผ่านผิด'
            context['next_url'] = next_url
    
    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

@login_required
def logout_page(request):
    logout(request)
    return redirect('index')

def register_page(request):
    context = {}

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mail = request.POST.get('mail')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if password1 == password2 and firstname and lastname and mail and username and password1 and password2:
            user = User.objects.create_user(first_name=firstname,
                                last_name=lastname,
                                username=username,
                                email=mail,
                                password=password2)
            return redirect('index')
        elif password1 != password2:
            context['error'] = 'รหัสผ่านไม่ตรงกัน'
        else:
            context['error'] = 'กรุณากรอกข้อมูลให้ครบทุกช่อง'

        context['firstname'] = firstname
        context['lastname'] = lastname
        context['mail'] = mail
        context['username'] = username
        context['password1'] = password1
        context['password2'] = password2

    return render(request, template_name='register.html', context=context)