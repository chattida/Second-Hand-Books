from django.urls import path
from . import views

urlpatterns = [
    path('sell/', views.add_sell_page, name='sell'),
    path('buy/', views.add_buy_page, name='buy'),
    path('<int:id>', views.detail_page, name='detail'),
    path('close/<int:id>/', views.close_post, name='close')
]