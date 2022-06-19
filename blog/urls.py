from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
   # path('article/<int:article_id>', views.article, name='article' )
    path('showEmployeeForm', views.showEmployeeForm, name="showEmployeeForm"),
    path('createEmpoyee', views.createEmployee, name="createEmployee"),
    path('editEmployeeForm/<int:employee_id>', views.editEmployeeForm, name="editEmployeeForm"),
    path('editEmployee', views.editEmployee, name="editEmployee"),
    path('deleteEmployee/<int:employee_id>', views.deleteEmployee, name="deleteEmployee")
]