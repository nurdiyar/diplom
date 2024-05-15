from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *

from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def homeView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})
    context = {
        'links': links
    }

    try:
        mens = Product.objects.filter(gender=Gender.objects.get(name='Men')).order_by('-id')[:10]
        for elem in mens:
            print(elem.id)
        womens = Product.objects.filter(gender=Gender.objects.get(name='Women')).order_by('-id')[:10]
        kids = Product.objects.filter(gender=Gender.objects.get(name='Kid')).order_by('-id')[:10]
        context.update({'mens': mens})
        context.update({'womens': womens})
        context.update({'kids': kids})
        return render(request, template_name='index.html', context=context)
    except ObjectDoesNotExist:
        return render(request, template_name='index.html', context=context)


def aboutView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    context = {
        'links': links
    }
    return render(request, template_name='about.html', context=context)


def contactView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            {'name': 'contact us', 'url': 'contact_url', 'active': 'active'},
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            {'name': 'Контакты', 'url': 'contact_url', 'active': 'active'},
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    context = {
        'links': links
    }
    return render(request, template_name='contact.html', context=context)


def menView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': 'active'},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': 'active'},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    products = Product.objects.filter(gender=Gender.objects.get(name='Men'))
    categories = set()
    for product in products:
        categories.add(product.category)

    selected_category = 'All'
    if 'category' in request.GET:
        if request.GET.get('category') != 'All':
            category = Category.objects.get(id=request.GET.get('category'))
            selected_category = category.name
            products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        page_obj = paginator.page(1)
    except EmptyPage:
        page_num = paginator.num_pages
        page_obj = paginator.page(paginator.num_pages)

    pages = []
    for i in range(1, paginator.num_pages + 1):
        if i == page_num:
            pages.append({
                'num': i,
                'url': 'men_url',
                'active': 'active'
            })
        else:
            pages.append({
                'num': i,
                'url': 'men_url',
                'active': ''
            })

    context = {
        'links': links,
        'pages': pages,
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category
    }

    return render(request, template_name='products.html', context=context)


def womenView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': 'active'},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': 'active'},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    products = Product.objects.filter(gender=Gender.objects.get(name='Women'))
    categories = set()
    for product in products:
        categories.add(product.category)

    selected_category = 'All'
    if 'category' in request.GET:
        if request.GET.get('category') != 'All':
            category = Category.objects.get(id=request.GET.get('category'))
            selected_category = category.name
            products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        page_obj = paginator.page(1)
    except EmptyPage:
        page_num = paginator.num_pages
        page_obj = paginator.page(paginator.num_pages)

    pages = []
    for i in range(1, paginator.num_pages + 1):
        if i == page_num:
            pages.append({
                'num': i,
                'url': 'women_url',
                'active': 'active'
            })
        else:
            pages.append({
                'num': i,
                'url': 'women_url',
                'active': ''
            })

    context = {
        'links': links,
        'pages': pages,
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category
    }

    return render(request, template_name='products.html', context=context)


def kidView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': 'active'},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': 'active'},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    products = Product.objects.filter(gender=Gender.objects.get(name='Kid'))
    categories = set()
    for product in products:
        categories.add(product.category)

    selected_category = 'All'
    if 'category' in request.GET:
        if request.GET.get('category') != 'All':
            category = Category.objects.get(id=request.GET.get('category'))
            selected_category = category.name
            products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        page_obj = paginator.page(1)
    except EmptyPage:
        page_num = paginator.num_pages
        page_obj = paginator.page(paginator.num_pages)

    pages = []
    for i in range(1, paginator.num_pages + 1):
        if i == page_num:
            pages.append({
                'num': i,
                'url': 'kid_url',
                'active': 'active'
            })
        else:
            pages.append({
                'num': i,
                'url': 'kid_url',
                'active': ''
            })

    context = {
        'links': links,
        'pages': pages,
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category
    }

    return render(request, template_name='products.html', context=context)


def accessoryView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': 'active'},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': 'active'},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    products = Product.objects.filter(gender=Gender.objects.get(name='Accessory'))
    categories = set()
    for product in products:
        categories.add(product.category)

    selected_category = 'All'
    if 'category' in request.GET:
        if request.GET.get('category') != 'All':
            category = Category.objects.get(id=request.GET.get('category'))
            selected_category = category.name
            products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_num = 1
        page_obj = paginator.page(1)
    except EmptyPage:
        page_num = paginator.num_pages
        page_obj = paginator.page(paginator.num_pages)

    pages = []
    for i in range(1, paginator.num_pages + 1):
        if i == page_num:
            pages.append({
                'num': i,
                'url': 'accessories_url',
                'active': 'active'
            })
        else:
            pages.append({
                'num': i,
                'url': 'accessories_url',
                'active': ''
            })

    context = {
        'links': links,
        'pages': pages,
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category
    }

    return render(request, template_name='products.html', context=context)


def productDetailView(request, pk):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'profile', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'logout', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'login', 'url': 'login_url', 'active': ''})
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
        ]
        if request.user.is_authenticated:
            links.append({'name': 'Профиль', 'url': 'profile_url', 'active': ''})
            links.append({'name': 'Выход', 'url': 'logout_url', 'active': ''})
        else:
            links.append({'name': 'Вход', 'url': 'login_url', 'active': ''})

    product = get_object_or_404(Product, id=pk)
    context = {
        'links': links,
        'product': product
    }

    return render(request, template_name='product_detail.html', context=context)


def loginView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile_url')
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'login', 'url': 'login_url', 'active': ''}
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Вход', 'url': 'login_url', 'active': ''}
            ]

        context = {
            'links': links,
            'error': request.session.get('error')
        }
        return render(request, template_name='login.html', context=context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if 'error' in request.session.keys():
                del request.session['error']
            return redirect('profile_url')
        else:
            request.session.update({'error': 'Email and/or password incorrect. Try again'})
            return redirect('login_url')


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home_url')


def profileView(request):
    if request.user.is_authenticated:
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'logout', 'url': 'logout_url', 'active': ''},
                {'name': 'profile', 'url': 'profile_url', 'active': 'active'}
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Выход', 'url': 'logout_url', 'active': ''},
                {'name': 'Профиль', 'url': 'profile_url', 'active': 'active'}
            ]
        context = {
            'links': links
        }
        return render(request, template_name='profile.html', context=context)
    return redirect('login_url')


def favouritesView(request):
    if request.user.is_authenticated:
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'logout', 'url': 'logout_url', 'active': ''},
                {'name': 'profile', 'url': 'profile_url', 'active': ''}
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Выход', 'url': 'logout_url', 'active': ''},
                {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
            ]
        context = {
            'links': links,
            'products': request.user.favourites.all()
        }
        return render(request, template_name='products.html', context=context)
    return redirect('login_url')


def registerView(request):
    if request.user.is_authenticated:
        return redirect('home_url')

    if request.method == 'GET':
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'logout', 'url': 'logout_url', 'active': ''},
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Выход', 'url': 'logout_url', 'active': ''},
            ]
        context = {
            'links': links,
            'error': request.session.get('error')
        }

        return render(request, template_name='register.html', context=context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(CustomUser.objects.filter(email=email)) > 0:
            request.session.update({'error': 'This email already taken!'})
            return redirect('register_url')
        if 'error' in request.session.keys():
            del request.session['error']
        user = CustomUser.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('profile_url')


class AddFavouritesApiView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        if request.user.is_authenticated:
            product_id = request.data.get('product_id').split('_')[-1]
            if product_id is None or product_id == '':
                return Response(status=status.HTTP_400_BAD_REQUEST)
            product = Product.objects.get(id=product_id)
            if product in request.user.favourites.all():
                request.user.favourites.remove(product)
            else:
                request.user.favourites.add(product)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class AddCartApiView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        if request.user.is_authenticated:
            cart = Cart(request)
            product_id = request.data.get('product_id').split('_')[-1]

            if product_id is None or product_id == '':
                return Response(status=status.HTTP_400_BAD_REQUEST)
            product = Product.objects.get(id=product_id)

            for key, value in cart.cart.items():
                if product_id == value.get('product_id'):
                    break
            else:
                cart.add(product=product)
                return Response(status=status.HTTP_200_OK)

            cart.remove(product=product)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required(login_url="login_url")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login_url")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login_url")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login_url")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login_url")
def cart_detail(request):
    cart = Cart(request)
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'logout', 'url': 'logout_url', 'active': ''},
            {'name': 'profile', 'url': 'profile_url', 'active': ''}
        ]
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'Выход', 'url': 'logout_url', 'active': ''},
            {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
        ]

    total = 0
    for key, value in cart.cart.items():
        total += int(value.get('price'))

    context = {
        'links': links,
        'total': total
    }
    return render(request, template_name='cart_detail.html', context=context)


@csrf_exempt
def ticketView(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('login_url')
        if not request.user.is_staff:
            return redirect('home_url')
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'logout', 'url': 'logout_url', 'active': ''},
                {'name': 'profile', 'url': 'profile_url', 'active': ''}
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Выход', 'url': 'logout_url', 'active': ''},
                {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
            ]
        tickets = Ticket.objects.filter(is_open=True)
        context = {
            'links': links,
            'tickets': tickets,
        }
        return render(request, template_name='tickets.html', context=context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        text = request.POST.get('text')
        if email is not None and text is not None:
            ticket = Ticket(email=email, text=text)
            ticket.save()
            response = {
                'id': ticket.pk,
                'msg': 'Ticket successfully created and opened'
            }
            return JsonResponse(data=response, status=status.HTTP_200_OK)
        response = {
            'msg': 'Email and/or text is not correct'
        }
        return JsonResponse(data=response, status=status.HTTP_400_BAD_REQUEST)


def ticketDetailView(request, id):
    if request.method == 'GET':
        if request.LANGUAGE_CODE == 'en':
            links = [
                {'name': 'men', 'url': 'men_url', 'active': ''},
                {'name': 'women', 'url': 'women_url', 'active': ''},
                {'name': 'kid', 'url': 'kid_url', 'active': ''},
                {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'logout', 'url': 'logout_url', 'active': ''},
                {'name': 'profile', 'url': 'profile_url', 'active': ''}
            ]
        else:
            links = [
                {'name': 'Мужской', 'url': 'men_url', 'active': ''},
                {'name': 'Женский', 'url': 'women_url', 'active': ''},
                {'name': 'Детский', 'url': 'kid_url', 'active': ''},
                {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
                
                {'name': 'Выход', 'url': 'logout_url', 'active': ''},
                {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
            ]
        ticket = Ticket.objects.get(id=id)
        context = {
            'links': links,
            'ticket': ticket
        }
        return render(request, template_name='ticket_detail.html', context=context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        is_open = request.POST.get('is_open')
        if is_open is not None and id is not None:
            ticket = Ticket.objects.get(id=id)
            ticket.is_open = bool(int(is_open))
            ticket.save()
        return redirect('tickets_url')


def checkoutView(request):
    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'logout', 'url': 'logout_url', 'active': ''},
            {'name': 'profile', 'url': 'profile_url', 'active': ''}
        ]
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'Выход', 'url': 'logout_url', 'active': ''},
            {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
        ]

    cart = Cart(request).cart
    total = 0
    for key, value in cart.items():
        total += int(value.get('price'))

    context = {
        'links': links,
        'total': total
    }
    return render(request, template_name='checkout.html', context=context)


def buyView(request):
    if not request.user.is_authenticated:
        return redirect('login_url')

    cart = Cart(request).cart
    total = 0
    order = Order(customer=request.user, total=total, status='Accepted')
    order.save()
    for key, value in cart.items():
        product = Product.objects.get(id=key)
        quantity = int(value.get('quantity'))
        item = OrderItem(product=product, quantity=quantity, total=int(product.price) * quantity)
        item.save()
        order.items.add(item)
        order.save()
        total += int(value.get('price'))
    order.total = total
    order.save()
    cart.clear()
    return redirect('profile_url')


def historyView(request):
    if not request.user.is_authenticated:
        return redirect('login_url')

    if request.LANGUAGE_CODE == 'en':
        links = [
            {'name': 'men', 'url': 'men_url', 'active': ''},
            {'name': 'women', 'url': 'women_url', 'active': ''},
            {'name': 'kid', 'url': 'kid_url', 'active': ''},
            {'name': 'accessories', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'logout', 'url': 'logout_url', 'active': ''},
            {'name': 'profile', 'url': 'profile_url', 'active': ''}
        ]
    else:
        links = [
            {'name': 'Мужской', 'url': 'men_url', 'active': ''},
            {'name': 'Женский', 'url': 'women_url', 'active': ''},
            {'name': 'Детский', 'url': 'kid_url', 'active': ''},
            {'name': 'Акксессуары', 'url': 'accessories_url', 'active': ''},
            
            {'name': 'Выход', 'url': 'logout_url', 'active': ''},
            {'name': 'Профиль', 'url': 'profile_url', 'active': ''}
        ]
    orders = Order.objects.filter(customer=request.user)
    context = {
        'links': links,
        'orders': orders
    }
    return render(request, template_name='history.html', context=context)
