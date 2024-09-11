from django.urls import path

from courses.views import CourseInvoiceView, CourseListView, CourseDetailView

# from professions.views import (
#               ProfessionsView,
#               ProfessionDetailView,
#               ProfessionCreateProfileView,
#               ProfessionProfileView,
#               ProfessionProfileUpdatView,
              
#               ProfessionProfileDeleteView,
#               )


app_name = "courses"

urlpatterns = [
  path("", CourseListView.as_view(), name='course_list'),
  path("<int:id>/", CourseDetailView.as_view(), name='course_detail'),
  path("<int:pk>/invoice/", CourseInvoiceView.as_view(), name='course_invoice'),
  
#   path("", ProfessionsView.as_view(), name='p_list'),
#   path("<int:id>/", ProfessionDetailView.as_view(), name='p_detail'),
#   path("create/", ProfessionCreateProfileView.as_view(), name="p_profile_create"),
#   path("profile/", ProfessionProfileView.as_view(), name="p_profile"),
#   path("profile/edit", ProfessionProfileUpdatView.as_view(), name="p_profile_edit"),


  # path("profile/delete", ProfessionProfileDeleteView.as_view(), name="p_profile_delete"),
]