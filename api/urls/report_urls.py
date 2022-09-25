from django.urls import path

from api.views.tag_views import *

from api.views.report_views import get_all_reports

app_name = 'report'

urlpatterns = [
    path('all/',get_all_reports),
    # path('add/', add_tag),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]