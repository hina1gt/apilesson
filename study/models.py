from django.db import models

class StudyCenter(models.Model):
    name = models.CharField('Name', max_length=256)
    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):
    fullname = models.CharField('Full name', max_length=256)
    about = models.TextField('About', blank=True, null=True)
    experience = models.IntegerField('Experience', blank=True, null=True)
    study_center = models.ForeignKey(
        StudyCenter,
        on_delete=models.CASCADE,
        verbose_name='Study center'
    )
    phone_number = models.CharField('Phone number', max_length=13)

    def __str__(self):
        return f'{self.fullname}'
    
class Student(models.Model):
    fullname = models.CharField('Full name', max_length=256)
    about = models.TextField('About', blank=True, null=True)
    phone_number = models.CharField('Phone number', max_length=13)
    study_center = models.ForeignKey(
        StudyCenter,
        on_delete=models.CASCADE,
        verbose_name='Study center'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Teacher'
    )
    
    def __str__(self):
        return f'{self.fullname}'