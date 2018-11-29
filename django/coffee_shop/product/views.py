from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView

from .exceptions import InsuficientStock
from .forms import ContactForm
from .models import Product
from .services import ProductService


# FBVs
def list_products(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})


def buy_product(request, pk):
    # product = Product.objects.get(pk=pk)
    # if not product.stock:
    #    messages.error(request, 'Produto com estoque insuficiente!')
    # else:
    #    product.stock -= 1
    #    product.save()
    try:
        ProductService().buy_product(pk)
    except InsuficientStock:
        messages.error(request, 'Produto com estoque insuficiente!')

    return redirect(reverse('list-2'))


def contract_form_action(request):
    form = ContactForm(request.POST)
    products = Product.objects.all()

    if form.is_valid():
        messages.success(request, 'E-mail enviado com sucesso!')

    return render(request, 'product/product_list.html', {'form': form, 'object_list': products})


# CBVs
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(stock__gt=0).order_by('-stock')

    # def get_queryset(self):
    #    return Product.objects.all().order_by('-price')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = ContactForm()
        return context
