from django.urls import path
from . import views
urlpatterns = [
    path('',views.startup),
    path('phy',views.phy),
    path('chem',views.chem),
    path('math',views.math),
    path('phy-<int:q>',views.phy),
    path('chem-<int:q>',views.chem),
    path('math-<int:q>',views.math),
    path('submitanswer',views.submitanswer)
]
