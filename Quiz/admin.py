from django.contrib import admin
from Quiz.models import phy,chem,math,QuestionView,FileDir,FileView
# Register your models here..

admin.site.register(FileDir,FileView)
admin.site.register(math,QuestionView)
admin.site.register(phy,QuestionView)
admin.site.register(chem,QuestionView)