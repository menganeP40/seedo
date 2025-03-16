# creating a function to send mails 

from django.core.mail import send_mail 
from django.template.loader import render_to_string 
from django.conf import settings 

def send_order_success_email(order , user_email):
    subject = "Order Confirmation - Seedo"

    order_items = order.objects.all()

    #now django will render the order_success.html page 
    html_message = render_to_string('order_success.html' , {'order' : order , 'order_items' : order_items})


    #plain text version message that you want to convey 
    plain_message = f"Thank you for your order #{order.id}. Your order has been confirmed and is currently {order.status}. Total amount: ${order.total_amout}"


    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        html_message=html_message,
        fail_silently=False,
    )
