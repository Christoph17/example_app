
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from . import views as example_app_views
from dim_accounts import views as dim_accounts_views

urlpatterns = [
    
    url('dim_accounts/logout/', dim_accounts_views.logout_view, name="dim_accounts/logout/"),
    url('^django_plotly_dash/', include('django_plotly_dash.urls')),
    url('example_app', example_app_views.base, name='example_app'),

]
 