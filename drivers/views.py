from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver


def dashboard(request):
    total_drivers = Driver.objects.count()
    invited_count = Driver.objects.filter(status='invited').count()
    submitted_count = Driver.objects.filter(status='submitted').count()
    active_count = Driver.objects.filter(status='active').count()

    return render(request, 'dashboard.html', {
        'total_drivers': total_drivers,
        'invited_count': invited_count,
        'submitted_count': submitted_count,
        'active_count': active_count,
    })


def invite_driver(request):
    invite_link = None

    if request.method == 'POST':
        driver = Driver.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            status='invited'
        )
        invite_link = f"http://127.0.0.1:8000/onboard/{driver.invite_token}/"

    return render(request, 'invite_driver.html', {'invite_link': invite_link})


def onboard_driver(request, token):
    driver = get_object_or_404(Driver, invite_token=token)

    if request.method == 'POST':
        driver.first_name = request.POST.get('first_name')
        driver.middle_name = request.POST.get('middle_name')
        driver.last_name = request.POST.get('last_name')
        driver.date_of_birth = request.POST.get('date_of_birth')
        driver.phone = request.POST.get('phone')
        driver.email = request.POST.get('email')
        driver.ni_number = request.POST.get('ni_number')
        driver.utr_number = request.POST.get('utr_number')

        driver.status = 'submitted'
        driver.save()

        return render(request, 'success.html')

    return render(request, 'onboard_driver.html', {'driver': driver})


def drivers_list(request):
    query = request.GET.get('q', '')
    drivers = Driver.objects.all()

    if query:
        drivers = drivers.filter(first_name__icontains=query) | drivers.filter(last_name__icontains=query)

    return render(request, 'drivers_list.html', {'drivers': drivers, 'query': query})


def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'driver_detail.html', {'driver': driver})


# 🔥 NEW ACTIONS

def mark_active(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    driver.status = 'active'
    driver.save()
    return redirect(f'/drivers/{driver.id}/')


def reject_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    driver.status = 'rejected'
    driver.save()
    return redirect(f'/drivers/{driver.id}/')