from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('error_404/', views.error_404, name='error_404'),
    path('explore/', views.explore, name='explore'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('signup/', views.signup, name='signup'),
    path('forgot_password',views.forget_password,name='forgot_password'),
    path('contacts/',views.contacts,name='contacts'),
    # path('view_details/',views.view_details,name='view_details'),
    path('showcart/',views.showcart,name='showcart'),
    path('checkout/',views.checkout,name='checkout'),

    # Update this path in urls.py
    path('view_details/<int:seed_id>/', views.view_details, name='view_details'),
    # Add these new paths
    path('add-to-cart/<int:seed_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]