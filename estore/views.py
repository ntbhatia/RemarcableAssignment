from .models import Product
from .forms import ProductFilterForm
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = (Product.objects
                        .select_related('category')
                        .prefetch_related('tags')
                    )
        
        self.form = ProductFilterForm(self.request.GET)

        if self.form.is_valid():
            queryset = queryset.filterByParams(**self.form.cleaned_data)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.copy()        
        query.pop('page', None)
        
        context['querystring'] = query.urlencode()
        context['form'] = self.form
        return context
