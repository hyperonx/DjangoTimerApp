from django.urls import path, include

from  tasks.views import (
                        home_view,
                        addTask_view,
                        # completeTask_view,
                        # deleteCompleted_view,
                        deleteAll_view,
                        startTimer_view,
                        delete_view
                        
)

urlpatterns = [

    path("", home_view, name = "home"),
    path("add", addTask_view, name ="add"),
    path('start-timer/<task_id>',startTimer_view , name ="start-timer"),
    path('delete/<task_id>', delete_view, name ="delete"),

]