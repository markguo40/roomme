"""roome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import matching.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^questions', views.questions, name='questions'),
    url(r'^login', views.login, name='login'),
    url(r'^userpage', views.userpage, name='userpage'),
    url(r'^swipe-supply', views.swipeSupply, name='swipe_supply'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^matches-dashboard', views.matchesDashboard, name='matches_dashboard'),
    url(r'^swipe-demand', views.swipeDemand, name='swipe_demand'),
    url(r'^swipe-refreshed', views.swipeDemandRefreshed, name='swipe_demand_refreshed'),
]
