
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.message_form,name='messageform'),#get aand post request for insert opertn
    path('<int:id>/', views.message_form,name="User_update"),#for update
    path('delete/<int:id>/',views.message_delete,name="User_delete"),
    path('list/',views.message_list,name='messagelist'),#to retrieve and display all data

]
