from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-emp', views.allEmp, name='all-emp'),
    path('add-emp', views.addEmp, name='add-emp'),
    path('remove-emp', views.removeEmp, name='remove-emp'),
    path('remove-emp/<int:empID>', views.removeEmp, name='remove-emp'),
    path('filter-emp', views.filterEmp, name='filter-emp'),
    path('emp/update-emp/', views.updateEmp, name='update-emp'),
    path('edit-emp/', views.updateEmp, name='update_emp'),
    path('edit-emp/<int:emp_id>/', views.updateEmp, name='update_emp'),



]
