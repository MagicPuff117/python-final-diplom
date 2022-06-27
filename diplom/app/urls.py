
from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from . import views


contact_viewset = views.ContactViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'post': 'create',
    'delete': 'destroy'
})

app_name = 'shop'
urlpatterns = [
    path('partner/update', views.PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', views.PartnerState.as_view(), name='partner-state'),
    path('partner/orders', views.PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', views.RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', views.ConfirmAccount.as_view(),
         name='user-register-confirm'),
    path('user/details', views.AccountDetails.as_view(), name='user-details'),
    path('user/contact', contact_viewset, name='user-contact'),
    path('user/login', views.LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm,
         name='password-reset-confirm'),
    path('categories', views.CategoryView.as_view(), name='categories'),
    path('shops', views.ShopView.as_view(), name='shops'),
    path('products', views.ProductInfoView.as_view(), name='shops'),
    path('basket', views.BasketView.as_view(), name='basket'),
    path('order', views.OrderView.as_view(), name='order'),

]