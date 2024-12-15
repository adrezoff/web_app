from datetime import datetime, time as dt_time, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import TableBook, Table


@login_required
def TableBooking(request):
    if request.method == "POST":
        try:
            date = request.POST['date']
            date = datetime.strptime(date, '%d.%m.%Y').date()

            time = request.POST['time']
            time = dt_time.fromisoformat(time)

            person = int(request.POST['person'])
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            special_request = request.POST.get('special_request', '')

            available_tables = Table.objects.filter(capacity__gte=person)
            time_delta = timedelta(hours=2)

            for table in available_tables:
                base_datetime = datetime.combine(date, time)

                overlapping_bookings = TableBook.objects.filter(
                    table=table,
                    date=date,
                    time__gte=(base_datetime - time_delta).time(),
                    time__lt=(base_datetime + time_delta).time()
                )
                if not overlapping_bookings.exists():
                    table_book = TableBook(
                        user=request.user, date=date, time=time, person=person, table=table,
                        name=name, email=email, phone=phone, special_request=special_request
                    )
                    table_book.save()
                    context = {'messages': f'Столик №{table.number} зарезервирован!',
                               'message_type': 'success'}
                    return render(request, 'table.html', context)

            context = {'messages': 'К сожалению, на это время нет доступных столиков.',
                       'message_type': 'error'}
            return render(request, 'table.html', context)

        except ValueError as e:
            context = {'messages': f'Ошибка в формате ввода: {e}'}
            return render(request, 'table.html', context)
    else:
        return render(request, 'table.html', {})
