from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Capsule
from .forms import CapsuleForm
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class CapsuleCreateView(View):
    def get(self, request):
        form = CapsuleForm()
        return render(request, 'capsules/capsule_form.html', {'form': form})

    def post(self, request):
        form = CapsuleForm(request.POST, request.FILES)
        if form.is_valid():
            capsule = form.save(commit=False)
            capsule.user = request.user
            capsule.status = 'locked'
            capsule.save()
            messages.success(request, 'Time capsule created!')
            return redirect('capsule_dashboard')
        return render(request, 'capsules/capsule_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CapsuleDashboardView(View):
    def get(self, request):
        filter_date = request.GET.get('date')
        now = timezone.now()
        locked_capsules = Capsule.objects.filter(user=request.user, unlock_datetime__gt=now)
        unlocked_capsules = Capsule.objects.filter(user=request.user, unlock_datetime__lte=now)
        if filter_date:
            locked_capsules = locked_capsules.filter(unlock_datetime__date=filter_date)
            unlocked_capsules = unlocked_capsules.filter(unlock_datetime__date=filter_date)
        return render(request, 'capsules/dashboard.html', {
            'locked_capsules': locked_capsules,
            'unlocked_capsules': unlocked_capsules,
            'filter_date': filter_date,
        })

@method_decorator(login_required, name='dispatch')
class CapsuleDetailView(View):
    def get(self, request, pk):
        capsule = get_object_or_404(Capsule, pk=pk, user=request.user)
        if not capsule.is_unlocked():
            messages.error(request, 'This capsule is still locked!')
            return redirect('capsule_dashboard')
        return render(request, 'capsules/capsule_detail.html', {'capsule': capsule})
