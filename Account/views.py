from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from Booking.models import TableBook
from .forms import CustomUserCreationForm, LoginForm, ProfileUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Account:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Account:profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    # Получаем все бронирования текущего пользователя
    bookings = TableBook.objects.filter(user=request.user)

    # Отправляем данные в шаблон
    return render(request, 'profile.html', {
        'bookings': bookings,
    })


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Account:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'profile_update.html', {'form': form})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(TableBook, id=booking_id, user=request.user)
    booking.delete()
    return redirect('Account:profile')


def logout_view(request):
    logout(request)
    return redirect('Home:index')
