from django.urls import path
from . import views
urlpatterns = [
    path('',views.startup),
    path('exam/phy',views.m_phy),
    path('exam/chem',views.m_chem),
    path('exam/math',views.m_math),
    path('exam/phy/<int:q>',views.m_phy),
    path('exam/chem/<int:q>',views.m_chem),
    path('exam/math/<int:q>',views.m_math),
    path('submitanswer',views.submitanswer),
    # the new 
    path('upload',views.up),
    path('send/<str:subj>/<int:q>',views.check),
    path('end_exam',views.FinalSubmission),
]

