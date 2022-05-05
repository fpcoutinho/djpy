from django.urls import path
from . import views

app_name = 'compromisso'

urlpatterns = [
    path('', views.compromisso_list, name="list"),
    path('compromisso/<int:comp_id>/', views.compromisso_visualiza, name="visualiza"),
    path('delete/<int:comp_id>/', views.compromisso_deleta, name="deleta"),
    path('edita/<int:comp_id>/', views.compromisso_edita, name="edita"),
    path('criar/', views.compromisso_cria, name="cria"),
]
