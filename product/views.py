from django.db.models import Q
from django.views import generic
from product import models
# Create your views here.


class ProductListView(generic.ListView):
    template_name = "gallery.html"

    def get_queryset(self):
        query = Q()
        for k,v in self.request.GET.items():
            if v:
                query &= Q(**{f"{k}__icontains": v})
        return models.Product.objects.filter(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_names"] = self.get_field_names(exclude=["id", "title", "image", "description"])
        return context

    def get_field_names(self,exclude=None):
        fields = models.Product._meta.get_fields()
        field_names = []
        for field in fields:
            if exclude:
                if field.name in exclude:
                    continue
            field_names.append((field.name, field.verbose_name))
        return field_names
