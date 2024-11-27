from django.urls import path
from . import views

app_name = 'fin'
urlpatterns = [
     path('save-deposit-products/', views.save_deposit_products),
     path('save-saving-products/', views.save_saving_products),
     path('recommend/deposit/', views.recommend_deposit_products),
     path('recommend/saving/', views.recommend_saving_products),
     path('deposit/likes/',views.get_liked_deposit_products),
     path('saving/likes/',views.get_liked_saving_products),
     path('deposit/<int:deposit_pk>/likes/',views.deposit_likes),
     path('saving/<int:saving_pk>/likes/',views.saving_likes),
     path('exchange/', views.exchange),
     path('send/deposit/', views.send_deposit),
     path('send/saving/', views.send_saving)
]


