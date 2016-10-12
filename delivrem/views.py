from .forms import (
        ProductForm,
        ProductEditForm
    )
from .models import Product

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import edit, DetailView, ListView, TemplateView



class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = "product_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super(ProductCreateView, self).form_valid(form)

product_new = login_required(ProductCreateView.as_view())

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = "product_update.html"

    #@method_decorator(login_required)
    #@method_decorator(staff_or_author_required(Product))
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

post_edit = ProductUpdateView.as_view()

class ProductDetailView(DetailView):
    template_name = "detail.html"
    model = Product
    """
    #TODO the retrun home button doesn't display all the Product list
    """


class  ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_confirm.html'

    #@method_decorator(login_required)
    #@method_decorator(staff_or_author_required(Product))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['back_page'] = reverse_lazy('delivrem:product-home')
        return context

    def get_success_url(self):
        return reverse_lazy('delivrem:product-home')

product_delete = ProductDeleteView.as_view()
