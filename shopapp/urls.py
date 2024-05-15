from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', homeView, name='home_url'),
    path('about_us', aboutView, name='about_url'),
    path('contact_us', contactView, name='contact_url'),
    path('men', menView, name='men_url'),
    path('women', womenView, name='women_url'),
    path('kid', kidView, name='kid_url'),
    path('accessories', accessoryView, name='accessories_url'),
    path('product/<int:pk>', productDetailView, name='product_detail_url'),
    path('login', loginView, name='login_url'),
    path('profile', profileView, name='profile_url'),
    path('logout', logoutView, name='logout_url'),
    path('favourites', favouritesView, name='favourites_url'),
    path('registration', registerView, name='register_url'),
    path('tickets', ticketView, name='tickets_url'),
    path('ticket/<int:id>', ticketDetailView, name='ticket_url'),
    path('checkout', checkoutView, name='checkout_url'),
    path('buy', buyView, name='buy_url'),
    path('history', historyView, name='history_url'),

    path('api/add_favourites', AddFavouritesApiView.as_view(), name='add_favourites_api_url'),
    path('api/add_cart', AddCartApiView.as_view(), name='cart_add'),
]

urlpatterns += [
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
]
