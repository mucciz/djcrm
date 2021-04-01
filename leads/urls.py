from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('<pk>/', views.lead_detail, name='lead_detail')
]