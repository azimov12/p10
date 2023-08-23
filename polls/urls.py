from django.urls import path
from .views import func1, func2, func3

urlpatterns = [
    path('func1/', func1),
    path('func2/', func2),
    path('func3/', func3),
]