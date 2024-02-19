from .views import RegisterView,LoginView,add_category,add_product,CreateInvoiceView,get_products_by_category,get_category,GetInvoicesView
from django.urls import path

urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('register/<int:id>',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('category/',add_category.as_view()),
    path('product/',add_product.as_view()),
    path('invoice/',CreateInvoiceView.as_view()),
    path('categories/',get_category.as_view()),
    path('product/<str:category>',get_products_by_category.as_view()),
    path('invoices/',GetInvoicesView.as_view()),
    path('invoices/<str:orderstatus>',GetInvoicesView.as_view())
]