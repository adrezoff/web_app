from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from Booking.models import TableBook
from .forms import CustomUserCreationForm, LoginForm, ProfileUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            context = {
                'messages': 'Вы успешно зарегистрированы!',
                'message_type': 'success'
            }
            return redirect('Account:profile')  # Перенаправление на профиль после регистрации
        else:
            context = {
                'messages': 'Ошибка регистрации. Проверьте введенные данные.',
                'message_type': 'error',
                'form': form
            }
            return render(request, 'register.html', context)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            context = {
                'messages': 'Добро пожаловать!',
                'message_type': 'success'
            }
            return redirect('Account:profile')
        else:
            context = {
                'messages': 'Неверный логин или пароль.',
                'message_type': 'error',
                'form': form
            }
            return render(request, 'login.html', context)
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    bookings = TableBook.objects.filter(user=request.user)

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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            context = {
                'messages': 'Пароль успешно изменен!',
                'message_type': 'success'
            }
            return render(request, 'change_password.html', context)
        else:
            context = {
                'messages': 'Ошибка изменения пароля.',
                'message_type': 'error'
            }
            return render(request, 'change_password.html', context)
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})
