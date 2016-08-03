from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from .models import Car
from .forms import CarCreateForm


class CarCreateView(CreateView):
    form_class = CarCreateForm
    template_name = 'cars/car_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car_update.html'

    def delete_car(self):
        self.object.delete()


class CarDetailView(DetailView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        return context


class CarListView(ListView):
    model = Car
    context_object_name = 'car_list'
    # paginate_by = 10
    template_name = 'cars/car_list.html'

    def get_queryset(self):
        qs = super(CarListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q is not None:
            return Car.objects.filter(Q(series__icontains=q) |
                                      Q(mark__icontains=q) |
                                      Q(body__icontains=q) |
                                      Q(cost__icontains=q) |
                                      Q(engine__name__icontains=q) |
                                      Q(color__colour__icontains=q) |
                                      Q(wheels__brand__icontains=q) |
                                      Q(cost__icontains=q) |
                                      Q(manufacturer_country__icontains=q) |
                                      Q(options__icontains=q))
        sort_by = self.request.GET.get('by')
        if sort_by is not None:
            sort_by = self.request.GET.get('in') + sort_by.lower()
            return Car.objects.order_by(sort_by)
        return qs


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
