from django.contrib import admin

# Register your models here.
from .models import CustomUser, OrthoAcademyData



# users admin paneli
@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
  list_display = ("username", 'last_name', 'first_name',)




# Ortho Academy admin paneli:
@admin.register(OrthoAcademyData)
class OrthoAcademy(admin.ModelAdmin):
  list_display = ("address", 'phone',)







# Mutaxasis admin paneli:
# @admin.register(Profession)
# class ProfessionAdmin(admin.ModelAdmin):
#   # qidirish paneli:
#   search_fields = ('profession',)#, 'last_name', 'first_name',)
#   # ko'rinish paneli:
#   # list_display = ("last_name", "first_name")
#   # filrelash paneli, o'ng tomonda:
#   list_filter = ('profession',)#, 'city', 'rank_profession',)

#   # def show_average(self, obj):
#   #   from django.db.models import Avg
#   #   result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
#   #   return result["grade__avg"]


# # Biznes admin paneli:
# @admin.register(Biznes)
# class BiznesAdmin(admin.ModelAdmin):
#   search_fields = ('name', 'speciality',)
#   # list_filter = ('speciality', 'city', 'rank_biznes',)


# # Mutaxasis komentlari admin paneli:
# @admin.register(ProfessionComment)
# class ProfessionCommentAdmin(admin.ModelAdmin):
#   search_fields = ('stars_give',)


# # Biznes komentlari admin paneli:
# @admin.register(BiznesComment)
# class BiznesCommenteAdmin(admin.ModelAdmin):
#   search_fields = ('stars_give',)





# 2- usuli: modelni admin panelda ko'rsatishni 
# class ForingKeyAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(BiznesProfession, ForingKeyAdmin)