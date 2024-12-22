from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

def send_confirmation_email(user):
    # Generate token
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(str(user.pk).encode('utf-8'))

    # Create the confirmation link
    activation_link = f"http://{get_current_site(None).domain}/activate/{uid}/{token}/"

    # Prepare the email
    subject = "Activate your account"
    message = render_to_string('accounts/activation_email.html', {
        'user': user,
        'activation_link': activation_link,
    })

    # Send the email
    send_mail(
        subject,
        message,
        'no-reply@example.com',  # Replace with your email or SMTP sender
        [user.email],
    )
