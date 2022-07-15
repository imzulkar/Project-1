from dataclasses import field
from django.views import generic
from rest_framework import generics as rest_gen, serializers, permissions
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
    paginate_by = 4  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        extra_context={
        'product': True}
        return context

class ProductListFilterSer(serializers.ModelSerializer):
    class Meta:
        model = product_model.Product
        fields = '__all__'

# class ProductListFilterView(rest_gen.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ProductListFilterSer
#     def get_queryset(self):
#         title = self.request.query_peram.get('title')
#         color = self.request.query_peram.get('color')
#         range = self.request.query_peram.get('range')
#         queryset = product_model.Product.objects.filter(Q(title__icontains=title)|(product_varient__))
#         return queryset