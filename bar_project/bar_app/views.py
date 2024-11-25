from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .forms import BookingForm
from .models import Table, Booking, Category
from django.contrib.auth.decorators import login_required

from bar_project import settings


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        table_id = request.POST.get('table_id')

        if table_id:
            table = Table.objects.get(id=table_id)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.table = table

                if Booking.is_table_available(
                    table=table,
                    date=booking.date,
                    time=booking.time
                ):
                    booking.save()

                    try:
                        send_mail(
                            subject='Table Booking Confirmation',
                            message=(
                                f'Dear {booking.name},\n\n'
                                f'Your table booking is confirmed!\n'
                                f'Table: {table.number}\n'
                                f'Date: {booking.date}\n'
                                f'Time: {booking.time}\n\n'
                                'Thank you for choosing us!'
                            ),
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[booking.email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        return JsonResponse({'success': True, 'message': f'Table booked, but email not sent: {str(e)}'})

                    return JsonResponse({'success': True, 'message': 'Table booked successfully! Confirmation email sent.'})
                else:
                    return JsonResponse({'success': False, 'message': 'This table is already booked for the selected time.'})

            return JsonResponse({'success': False, 'message': 'Invalid form data.'})

        if form.is_valid():
            guest_count = form.cleaned_data['guest_count']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            available_tables = Table.objects.filter(
                capacity__gte=guest_count
            ).exclude(
                id__in=[
                    booking.table.id for booking in Booking.objects.filter(
                        date=date
                    ) if not Booking.is_table_available(
                        booking.table, date, time
                    )
                ]
            )

            if available_tables.exists():
                tables = [
                    {"id": table.id, "number": table.number, "capacity": table.capacity}
                    for table in available_tables
                ]
                return JsonResponse({'success': True, 'tables': tables})
            else:
                return JsonResponse({'success': False, 'message': 'No tables available for the selected date and time.'})
        return JsonResponse({'success': False, 'message': 'Invalid form data.'})
    else:
        form = BookingForm()
    return render(request, 'bar_app/book_table.html', {'form': form})


@login_required
def booking_manager(request):
    bookings = Booking.objects.order_by('-date', '-time')
    return render(request, 'bar_app/booking_manager.html', {'bookings': bookings})


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(email=request.user.email).order_by('-date', '-time')
    return render(request, 'bar_app/user_bookings.html', {'bookings': bookings})


def menu_view(request):
    categories = Category.objects.prefetch_related('drinks').all()
    return render(request, 'bar_app/menu.html', {'categories': categories})

