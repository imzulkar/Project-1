from django.contrib import admin
from product import models as p_model
# Register your models here.
admin.site.register(p_model.Variant)
admin.site.register(p_model.Product)
admin.site.register(p_model.ProductImage)
admin.site.register(p_model.ProductVariant)
admin.site.register(p_model.ProductVariantPrice)