from django.conf.urls import url
from . import views

app_name = 'ElmaApp'

urlpatterns = [

    url(r'^AccountingSolutions/$', views.AccountingSolutionView.as_view(),name='AccountingSolutions'),
    url(r'^Development/$',views.DevelopmentView.as_view(),name='Development'),
    url(r'^SoftwareSolutions/$',views.SoftwareSolutioins.as_view(),name='SoftwareSolutions'),
    url(r'^ICTSolutions/$', views.ICTSolutioins.as_view(), name='ict'),
    url(r'^Training/$', views.Training.as_view(), name='training'),
    url(r'^Support/$', views.Support.as_view(), name='support'),
    url(r'^Quote/$', views.Qform.as_view(), name='quote'),
    url(r'^Products/$', views.ProductsView.as_view(), name='products'),

]