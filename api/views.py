from rest_framework import generics, viewsets, mixins, response, status, permissions
from rest_framework.response import Response
from app.models import *
from study.models import *
from .serializers import *

'''class CafeList(generics.ListAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetail(generics.RetrieveAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafePost(generics.CreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafePut(generics.UpdateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDelete(generics.DestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer'''

'''class CafeAPIView(generics.ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class MenuAPIVeiw(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 

class FoodAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer'''

'''class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer'''

class MenuAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class MenuDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class StudyCenterAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = StudyCenter.objects.all()
    serializer_class = StudyCenterSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        studycenter = self.get_queryset().all()
        serializer = self.get_serializer(studycenter, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class StudyCenterDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = StudyCenter.objects.all()
    serializer_class = StudyCenterSerializer

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)       
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)     
      
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

class TeacherAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        teacher = self.get_queryset().all()
        serializer = self.get_serializer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class TeacherDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)       
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)     
      
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  

class StudentAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentrSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        student = self.get_queryset().all()
        serializer = self.get_serializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class StudentDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentrSerializer

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()] 
        return[]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)       
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)     
      
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  