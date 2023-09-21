from django.urls import path
from rest_framework import routers
from .views import *


'''router = routers.DefaultRouter()

router.register('cafe', CafeViewSet, basename='cafe')
router.register('menu', MenuViewSet, basename='menu')


urlpatterns = [
    
] + router.urls
'''

'''urlpatterns = [
    path('cafe/', CafeAPIView.as_view(), name='cafe'),
    path('cafe/<int:pk>', CafeDetailAPIView.as_view(), name='cafe_detail'),
    path('menu/', MenuAPIVeiw.as_view(), name='menu'),
    path('menu/<int:pk>', MenuDetailAPIView.as_view(), name='menu_detail'),
    path('food/', FoodAPIView.as_view(), name='food'),
    path('food/<int:pk>', FoodDetailAPIView.as_view(), name='food_detail'),
]'''

urlpatterns = [
    path('menu/', MenuAPI.as_view(), name='menu'),
    path('menu/<int:pk>', MenuDetailAPI.as_view(), name='menu_detail'),
    path('studycenter/', StudyCenterAPI.as_view(), name='studycenter'),
    path('studycenter/<int:pk>', StudyCenterDetailAPI.as_view(), name='studycenter_detail'),
    path('teacher/', TeacherAPI.as_view(), name='teacher'),
    path('teacher/<int:pk>', TeacherDetailAPI.as_view(), name='teacher_detail'),
    path('student/', StudentAPI.as_view(), name='student'),
    path('student/<int:pk>', StudentDetailAPI.as_view(), name='student_detail'),

]