from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('error_404/', views.error_404, name='error_404'),
    path('explore/', views.explore, name='explore'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('signup/', views.signup, name='signup'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('contacts/',views.contacts,name='contacts'),
    # path('view_details/',views.view_details,name='view_details'),
    path('showcart/',views.showcart,name='showcart'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile, name='profile'),
    
    path('login_for_feedback/',views.login_for_feedback, name='login_for_feedback'),


    path('login_for_adding_to_cart/<int:seed_id>/',views.login_for_adding_to_cart , name='login_for_adding_to_cart'),

    # Update this path in urls.py
    path('view_details/<int:seed_id>/', views.view_details, name='view_details'),
    # Add these new paths
    path('add_to_cart/<int:seed_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),




    path('cart/', views.showcart, name='showcart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),


    path('checkout/' , views.checkout , name='checkout'),
    path('order_confirmation/<int:order_id>' , views.order_confirmation , name='order_confirmation')


]