from django.shortcuts import render
from .models import TableBook
from datetime import datetime


def TableBooking(request):
    if request.method=="POST":
        date=request.POST['date']
        date=datetime.strptime(date,'%d %B %Y')
        time=request.POST['time']
        person=request.POST['person']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        occasion=request.POST['occasion']
        special_request=request.POST['special_request']
        table_book=TableBook(date=date,time=time,person=person,
                    name=name,email=email,phone=phone,
                    occasion=occasion,special_request=special_request)
        table_book.save()
        context={'messages':'Thank you for your reservation.'}
        return render(request,'table.html',context)
    else:
        return render(request,'table.html',{})
