from django.urls import path
from .views import *


urlpatterns = [
    path('deshboad/', deshboard, name="deshboad"),
    path('add-blog/', AddFun, name='add'),
    path('<int:id>/delete-blog/', delete, name='delete'),
    path('update-blog/<int:id>/edit', update, name='update'),
    path('about/', aboutus, name='about'),
    # path('profile-Edit/', profileEdit, name='profileedit'),
    path('profile-Edit/<int:pk>/Edit', profileEdit, name='profileedit'),
]
