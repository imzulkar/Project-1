from django.views import generic
from time import timezone
from product import models as product_model


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = product_model.Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


# class ProductList(generic.ListCre)
class ProductList(generic.ListView):
    template_name='products/list.html'
    model = product_model.Product
    context_object_name = 'products'
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        extra_context={
        'product': True}
        return context