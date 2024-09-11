from datetime import date
import logging
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
import re
from django.views import View
from django.utils.functional import SimpleLazyObject
# from django.urls import reverse_lazy



from courses.models import Courses
from users.forms import  UserCreateForm, UserUpdateForm
from users.models import CustomUser, Dashboard


# Create your views here.

# user register page uchun
class RegisterView(View):
  def get(self, request):
    create_form = UserCreateForm()
    context = {
      "form": create_form,
    }
    return render(request, "users/register.html", context=context)

  def post(self, request):
    create_form = UserCreateForm(data=request.POST)

    if create_form.is_valid():
      # creat user account
      create_form.save()
      return redirect("users:login")
    else:
      context = {
                "form": create_form,
            }
      return render(request, "users/register.html", context=context)


# User login pager uchun
class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        # login_form = CustomAuthenticationForm()
        
        return render(request, "users/login.html", {"login_form": login_form})

    def post(self, request, pk=None):
        login_form = AuthenticationForm(data=request.POST)
        # login_form = CustomAuthenticationForm(data=request.POST)

        if login_form.is_valid():
            # log in the user
            user = login_form.get_user()
            # userga sesiya ochib id sini cookiga qo'yadi
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli tizimga kirdingiz.")

            # login qilmagan user kurs xarid qilmoqchi bo'sa, login qilib invoic ga yo'naltiramiz
            whear_from = request.META.get('HTTP_REFERER')
            if re.findall(r"\/\d+\/invoice\/", whear_from):
                pk = pk
                return render(request, 'courses/course_invoice.html', {"course": pk})
            else:
                return redirect("users:dashboard")
            

            # referer = request.META.get('HTTP_REFERER')
            # return render(request, 'my_template.html', {'referer': referer})
        else:
            return render(request, "users/login.html", {"login_form": login_form})


# User profil page uchun
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        # LoginRequiredMixin - shu klass o'zi userni login qilganini tekshirib beradi
        # if not request.user.is_authenticated:
        #   return redirect("users:login")
        # else:
        #   return render(request, "users/profile.html", {"user": request.user})


        user_id = request.user.id
        # biznes = Biznes.objects.get(user_account_id=user_id)
        # professi = Profession.objects.get(user_account_id=user_id)
        # biznes = Biznes.objects.all()
        # professi = Profession.objects.all()

        return render(request, "users/profile.html", {"user": request.user})#, "busines": biznes, "profession": professi})


# profil edit page uchun
class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
            user_update_form = UserUpdateForm(instance=request.user)

            return render(request, "users/edit_profile.html", {"form": user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(
        instance=request.user,
        data=request.POST,
        files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "Siz profilingizni muvaffaqiyatli yangiladingiz.")

            return redirect("users:profile")

        return render(request, "users:edit_profile.html", {"form": user_update_form})





class PasswordsChangeView(PasswordChangeView):
    # password_update_form = PasswordChangeForm
    # success_url = reverse_lazy('landing_page')

    def get(self, request):
        password_update_form = PasswordChangeForm(user=request.user)

        return render(request, "users/password_change_form.html", {"form": password_update_form})
    
    def post(self, request):
        password_update_form = PasswordChangeForm(
                    user=request.user,
                    data=request.POST,
                    files=request.FILES
        )

        if password_update_form.is_valid():
            password_update_form.save()
            message = messages.success(request, "Parolingizni muvaffaqiyatli yangiladingiz! Saytga yangi parol bilan kirishingiz mumkin.")

            login_form = AuthenticationForm()
            return render(request, "users/login.html", {"message": message, "login_form": login_form})
            # return redirect("users:login", {"message": message})
            # return redirect("users:password_change_done")

        return render(request, "users/password_change_form.html", {"form": password_update_form})






# Logout metodi
class LogoutView(LoginRequiredMixin, View):
  # logout metodi
  def get(self, request):
    logout(request)
    messages.info(request, "You have successfully logged out.")

    return redirect("landing_page")








# Dashboard page uchun
class UserDashboardView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        # Получаем объект Dashboard для текущего пользователя
        dashboards = Dashboard.objects.filter(user=request.user)

        # if id:
        #     course = get_object_or_404(Courses, id=id)
        #     user = get_object_or_404(CustomUser, id=user.id)

        #     dashboard_entry = Dashboard(
        #         buy_date=date.today(),
        #         progres=0,
        #         course=course.id,
        #         user=user.id
        #     )
        #     dashboard_entry.save()

        # print(request.COOKIES['example_cookie'])
        # print(request.user.is_authenticated)    # user login qilgannini aniqlaydi

        # user_courses = enumerate(Courses.objects.filter(id=request.user.id))
        # progres = {}  # Пример: {course_id: progress_value}

        # # Например, если progres содержит список, преобразуй его в словарь
        # for i, course in user_courses:
        #     dashboard = Dashboard.objects.get(user_id=request.user.id, course_id=id)
        #     progres[course.id] = int( ( 100 / course.count_videos ) * dashboard.progres )  # где some_calculated_progress — значение прогресса для данного курса

        # context = {
        #     'user_courses': user_courses,
        #     'progres': progres,
        # }



        # Получаем список курсов, связанных с этим Dashboard
        user_courses = [(i, dashboard.course) for i, dashboard in enumerate(dashboards)]
        
        # Прогресс может быть рассчитан отдельно, если требуется
        # progres = {dashboard.course.id: dashboard.progres for dashboard in dashboards}

        progres = {}
        for dashboard in dashboards:
            course_id = dashboard.course.id
            progres_value = dashboard.progres
            course = Courses.objects.get(id=course_id)
            progres[course.id] = int( ( 100 / course.count_videos ) * progres_value )


            logging.info(user_courses)
            logging.info(dashboards)
            logging.info(progres)

        context = {
            'user_courses': user_courses,
            'progres': progres,
        }
        return render(request, 'users/dashboard.html', context)





# Course progres page uchun
class CourseProgresView(LoginRequiredMixin, View):
    def get(self, request, id, num=1):
        course = get_object_or_404(Courses, id=id)

        # Убедитесь, что request.user оценивается
        user = request.user
        if isinstance(user, SimpleLazyObject):
            user = user._wrapped
        
        dashboard = Dashboard.objects.get(user_id=user.id, course_id=id)
        # progres = int((100 / course.count_videos) * dashboard.progres)
        if num == 1:
            progres = int((100 / course.count_videos) * 0)
        else:
            progres = int((100 / course.count_videos) * (num - 1))

        words = [
                "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
                "Twenty_One", "Twenty_Two", "Twenty_Three", "Twenty_Four", "Twenty_Five", "Twenty_Six", "Twenty_Seven", "Twenty_Eight", "Twenty_Nine", "Thirty",
                "Thirty_One", "Thirty_Two", "Thirty_Three", "Thirty_Four", "Thirty_Five", "Thirty_Six", "Thirty_Seven", "Thirty_Eight", "Thirty_Nine", "Forty",
                "Forty_One", "Forty_Two", "Forty_Three", "Forty_Four", "Forty_Five", "Forty_Six", "Forty_Seven", "Forty_Eight", "Forty_Nine", "Fifty"
            ]

        video_range = range(1, course.count_videos + 1)

        try:
            dashboard.progres = num - 1
            dashboard.save()

            logging.info(f"Данные успешно сохранены: {dashboard}")
        except Exception as e:
            logging.error(f"Ошибка сохранения данных: {e}")

        context = {
            'course': course,
            'blocktitles': {i: word for i, word in enumerate(words[ : 3])},
            'blockitems': video_range,
            'len': len(video_range),
            'progres': progres,
            'id': num
        }

        return render(request, 'users/course_progres.html', context)