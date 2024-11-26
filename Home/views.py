from Booking.models import TableBook
from Menu.models import MenuItems, MenuCategory
from django.views.generic import ListView


class IndexPageView(ListView):
    queryset = TableBook.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['meal_lists'] = MenuItems.objects.all()
        context['categories'] = MenuCategory.objects.all()
        return context
