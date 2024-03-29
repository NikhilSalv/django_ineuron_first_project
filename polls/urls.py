from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    path('',views.index, name = 'index'),
    path('<int:question_id>/details',views.details, name = 'detail'),
    path('<int:question_id>/result',views.result, name = 'result'),
    path('<int:question_id>/vote',views.vote, name = 'vote'),

]

# urlpatterns = [

#     path('',views.IndexView.as_view(), name = 'index'),
#     path('<int:pk>/',views.DetailView.as_view(), name = 'detail'),
#     path('<int:pk>/result',views.ResultView.as_view(), name = 'result'),
#     path('<int:question_id>/vote',views.vote, name = 'vote'),

# ]