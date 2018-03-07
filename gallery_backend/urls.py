from django.contrib.auth.decorators import login_required
from django.urls import path
from gallery_backend import views
from django.views.generic import TemplateView


urlpatterns = [
    path('backend/', login_required(TemplateView.as_view(template_name="gallery_backend/backend.html")), name="backend"),
    path('backend/create/', views.ProductCreate.as_view(), name="backend-create"),
    path('backend/list/', views.ProductList.as_view(), name="backend-list"),
    path('backend/import/', views.ExcelImportView.as_view(), name="backend-import"),
    path('backend/<int:pk>/edit/', views.ProductUpdate.as_view(), name="backend-update"),
    path('backend/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

]
