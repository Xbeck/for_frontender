import datetime
import logging
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.paginator import Paginator

from courses.models import Courses
from users.models import CustomUser, Dashboard, OrthoAcademyData
from paycomuz import Paycom


# Create your views here.
# Course page uchun
class CourseListView(View):
    def get(self, request):
        # LoginRequiredMixin - shu klass o'zi userni login qilganini tekshirib beradi

        # user_id = request.user.id
        # biznes = Biznes.objects.get(user_account_id=user_id)
        # professi = Profession.objects.get(user_account_id=user_id)
        course_objs = Courses.objects.all().order_by('id')

        page_size = request.GET.get("page_size", 10)
        paginator = Paginator(course_objs, page_size)

        page_num = request.GET.get("page", 1) # default 1 - page chiqadi
        page_object = paginator.get_page(page_num)

        # try:
        #     dashboards = Dashboard.objects.get(user=request.user)  # Пример фильтрации по текущему пользователю
        # except Dashboard.DoesNotExist:
        #     dashboards = None

        ortho_academy = OrthoAcademyData.objects.get(id=1)

        context = {
                    "page_obj": page_object,
                    "user": request.user,
                    "courses": course_objs,
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

        return render(request, "courses/course_list.html", context)


#   def get(self, request):
#     professions = Profession.objects.all().order_by('id')
#     comments = ProfessionComment.objects.all()
#     custom_users = CustomUser.objects.all()

#     page_size = request.GET.get("page_size", 2)
#     paginator = Paginator(professions, page_size)

#     page_num = request.GET.get("page", 1) # default 1 - page chiqadi
#     page_object = paginator.get_page(page_num)

#     if professions:
#       if comments:
#         # return render(request, "professions/p_list.html", {"professions": professions})
#         return render(request, "professions/p_list.html", {"professions": professions, "comments": comments})
#       else:
#         return render(request, "professions/p_list.html", {"professions": professions})
#     else:
#       return render(request, "professions/p_list.html")
#     return render(request, "professions/p_list.html", {"page_obj": page_object, "comments": comments, "customuser": custom_users})






class CourseDetailView(View):
    def get(self, request, id):
        course = Courses.objects.get(id=id)  # Замените 1 на нужный ID курса
        # user = CustomUser.objects.get(id=request.user.id)  # Замените 1 на нужный ID пользователя
        user = request.user

        # dashboard = get_object_or_404(Dashboard, user_id=request.user.id, course_id=id)
        # dashboard = Dashboard.objects.filter(user=user.id, course=id)
        # dashboard = Dashboard.objects.get(user, course)

        try:
            # dashboard = Dashboard.objects.get(user=request.user, course=course)
            dashboard = Dashboard.objects.get(user_id=user.id, course_id=id)
        except Dashboard.DoesNotExist:
            dashboard = None

        print(dashboard)
        logging.info(dashboard)

        # if user.id != dashboard.user.id and id != dashboard.course.id:
        if dashboard == None:
            if course.price == 0:

                dashboard_entry = Dashboard(
                    buy_date=datetime.date.today(),
                    progres=0,
                    course=course,
                    user=user)
                dashboard_entry.save()
            else:
                # redirekt to invoise page
                pass
        return render(request, "courses/course_detail.html", {"user": user, "course": course})



class CourseInvoiceView(LoginRequiredMixin, View):
    def get(self, request, pk):
        # LoginRequiredMixin - shu klass o'zi userni login qilganini tekshirib beradi
        # course_obj = Courses.objects.get(id=id)

        # add course to DB
        # buy_time = datetime.datetime.now()
        # user_id = request.user.id
        # course_id = pk

        # new_obj = Dashboard(buy_data=buy_time, progres=0, course=course_id, user=user_id)
        # new_obj.save()


        amount = 100000
        order_id = '123456789'

        paycom = Paycom()

        url = paycom.create_initialization(amount=amount,
                                           order_id=order_id,
                                           return_url='https://orthoacademy.com/payment/success/')
        print(url)

        return render(request, url, {"user": request.user})
    
    # def get(self, request, pk):
    #     course = get_object_or_404(Courses, pk=pk)
    #     # Your logic here
    #     return HttpResponse(f"Invoice for course: {course.name}")



