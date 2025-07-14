
from django.contrib import admin
from django.urls import path, include

# third-party
from rest_framework.routers import DefaultRouter

# apps
from tutorial.todos.views import TodoViewSet
from tutorial.homework.views import StudentViewSet, TeacherViewSet

router = DefaultRouter(trailing_slash=False)
router.register('todos', TodoViewSet, basename='todo')
router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    
]