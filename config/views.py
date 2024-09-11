import re
from django.shortcuts import redirect, render
from django.views import View
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from django.contrib.auth import login

from courses.models import Courses
from users.models import Dashboard, OrthoAcademyData
# from professions.models import Profession





# Courses obj ni landing page ga uzatamiz
class LandingView(View):
    # def landing_page(request):
    def get(self, request, course_id=None):
        courses = Courses.objects.all().order_by('id')
        # dashboards = Dashboard.objects.all()
        ortho_academy = OrthoAcademyData.objects.get(id=1)


        # try:
        #     dashboards = Dashboard.objects.get(user=request.user)  # Пример фильтрации по текущему пользователю
        # except Dashboard.DoesNotExist:
        #     dashboards = None

        context = {
                    "user": request.user,
                    "courses": courses,
                    "ortho_academy": ortho_academy
                    }

        # course_id_list = []
        # if dashboards:
        #     if type(dashboards) == 'list':
        #         for obj in dashboards:
        #             course_id = obj.course.id
        #             course_id_list.append(course_id)
        #     else:
        #         course_id_list.append(dashboards.course.id)

        #     context['dashboard_course_ids'] = course_id_list





        # if dashboard:
        #     context = {"user": request.user,
        #               "courses": courses,
        #               "dashboards": dashboards}
        # else:
        #     context = {"user": request.user,
        #               "courses": courses}
            
        # biznes = Biznes.objects.get(user_account_id=user_id)
        # professi = Profession.objects.get(user_account_id=user_id)
        # biznes = Biznes.objects.all()
        # professi = Profession.objects.all()


        return render(request, "landing.html", context)#, {"busines": biznes, "profession": professi})




# class AdminPanelLoginView(View):
#     def get(self, request):
#         admin_login_form = AuthenticationForm()
#         # admin_login_form = CustomAuthenticationForm()
#         return render(request, "admin_login.html", {"admin_login_form": admin_login_form})
    
    

        
#     def post(self, request, pk=None):
#         admin_login_form = AuthenticationForm(data=request.POST)
        
#         if admin_login_form.is_valid():
#             # log in the user
#             user = admin_login_form.get_user()
#             # userga sesiya ochib id sini cookiga qo'yadi
#             login(request, user)
#             messages.success(request, "Siz muvaffaqiyatli Admin panelga kirdingiz.")

#             # return redirect("admin_login")
  
#         else:
#             return render(request, "admin_login.html", {"admin_login_form": admin_login_form})
