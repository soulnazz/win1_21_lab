from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .models import CustomerCL, OrderCL, ProductCL, TagCL
from .forms import OrderForm,CustomerForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages



class AllClothingListView(generic.ListView):
    model = ProductCL
    template_name = 'cloth/all_clothing_list.html'
    context_object_name = 'clothing'

    def get_queryset(self):
        return ProductCL.objects.all()

class UpperClothingListView(generic.ListView):
    model = ProductCL
    template_name = 'cloth/upper_clothing_list.html'
    context_object_name = 'clothing'

    def get_queryset(self):
        return ProductCL.objects.filter(tags__name='верхний')

class HeadwearClothingListView(generic.ListView):
    model = ProductCL
    template_name = 'cloth/headwear_clothing_list.html'
    context_object_name = 'clothing'

    def get_queryset(self):
        return ProductCL.objects.filter(tags__name='головной')

class LowerClothingListView(generic.ListView):
    model = ProductCL
    template_name = 'cloth/lower_clothing_list.html'
    context_object_name = 'clothing'

    def get_queryset(self):
        return ProductCL.objects.filter(tags__name='нижний')

class FootwearClothingListView(generic.ListView):
    model = ProductCL
    template_name = 'cloth/footwear_clothing_list.html'
    context_object_name = 'clothing'

    def get_queryset(self):
        return ProductCL.objects.filter(tags__name='обувь')






class OrderCreateView(CreateView):
    model = OrderCL
    form_class = OrderForm
    template_name = 'cloth/order_form.html'
    success_url = reverse_lazy('success-url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_form'] = CustomerForm()
        return context

    def form_valid(self, form):

        response = super().form_valid(form)


        customer_form = CustomerForm(self.request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()
            self.object.customer = customer
            self.object.save()

        return response

class CustomerCreateView(CreateView):
    model = CustomerCL
    form_class = CustomerForm
    template_name = 'cloth/customer_form.html'
    success_url = reverse_lazy('order-create')
    def form_valid(self, form):
        response = super().form_valid(form)

        return response

