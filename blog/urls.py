from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
   # path('article/<int:article_id>', views.article, name='article' )
    path('showEmployeeForm', views.showEmployeeForm, name="showEmployeeForm"),
    path('createEmpoyee', views.createEmployee, name="createEmployee")
]