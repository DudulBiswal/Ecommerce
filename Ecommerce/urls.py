"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cart.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ProductView,name='product'),
    path('view/<int:id>/',View),
    path('cart/',view_cart,name='cart'),
    path('add_cart/<int:id>/',add_to_cart),
    path('del/<int:id>/',delete),
    path('inc/<int:id>/',inc),
    path('dec/<int:id>/',dec),
    path('register/',Register),
    path('login/',Login),
    path('home/',Home,name='home'),
    path('search/',Search,name='search'),
    path('logout/',Logout),
    path('add/',Addproduct),


    path('seller/',sellerindex),
    path('sellersignup/',sellerregister),
    path('sellerlogin/',SellerLogin)
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

