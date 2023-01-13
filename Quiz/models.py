from django.db import models
from django.contrib import admin

class FileView(admin.ModelAdmin):
    list_display=('sub','Fileloc')
    radio_fields = {'sub':admin.HORIZONTAL}
    # radio_fields = {'sub':admin.VERTICAL}


class FileDir(models.Model):
    Fileloc = models.CharField(max_length=25)
    SUB_CHOICES = (
    ('math','math'),
    ('phy','phy'),
    ('chem','chem')
    )
    sub = models.CharField(max_length=25,choices=SUB_CHOICES,default='math')


    def __str__(self) -> str:
        return f"{self.Fileloc},{self.sub}"

class QuestionView(admin.ModelAdmin):
    list_display = ('id',"question", 'option1','option2','option3','option4','answer')
    fieldsets = [
        ['Questions', {
            'fields': ['id','question']
        }],
        ['Options', {
            'fields': [('option1','option2'),('option3','option4')],
        }],
        ['Answer',{
            'classes': ['collapse'],
            'fields':['answer']
        }]
    ]
    ordering = ['id']


class phy(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=10,default=0)

    def __str__(self):
        return f"{self.id}.{self.question}"


class math(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=10,default=0)

    def __str__(self):
        return f"{self.id}.{self.question}"

class chem(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=10,default=0)

    def __str__(self):
        return f"{self.id}.{self.question}"
