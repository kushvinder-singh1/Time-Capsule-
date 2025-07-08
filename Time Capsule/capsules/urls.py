from django.urls import path
from .views import CapsuleCreateView, CapsuleDashboardView, CapsuleDetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views import View

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('capsule_dashboard')
        return redirect('login')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('capsule/new/', CapsuleCreateView.as_view(), name='capsule_create'),
    path('dashboard/', CapsuleDashboardView.as_view(), name='capsule_dashboard'),
    path('capsule/<int:pk>/', CapsuleDetailView.as_view(), name='capsule_detail'),
] 