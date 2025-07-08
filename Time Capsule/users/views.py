from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm, CustomSetPasswordForm
from .models import CustomUser
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.views import View

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True   # Auto-activate for development
            user.save()
            # self.send_verification_email(request, user)  # Skip email verification for now
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})

    def send_verification_email(self, request, user):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        url = request.build_absolute_uri(
            reverse_lazy('activate', kwargs={'uidb64': uid, 'token': token})
        )
        subject = 'Verify your Time Capsule account'
        message = render_to_string('users/email_verification.html', {'url': url, 'user': user})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

class ActivateView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account verified! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid or expired link.')
            return redirect('register')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'
    template_name = 'users/logout.html'
class CustomLogoutView(LogoutView):
    next_page = 'login'

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
