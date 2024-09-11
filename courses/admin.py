from django.contrib import admin



# Register your models here.
from .models import Courses
# from professions.models import Profession, ProfessionComment
# from business.models import Biznes, BiznesComment, BiznesProfession


# course admin paneli
@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
  list_display = ("title",
                  'image',
                  'short_discription',
                  'discription',
                  'plan',
                  'price',
                  'discount'
                    )
