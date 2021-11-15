from django.urls import path

from commentApp import views
from commentApp.views.commentView import CommentCreateView, CommentView, CommentDeleteView,\
                         CommentUpdateView

urlpatterns = [
    path('comment/',views.CommentCreateView.as_view()),
    path('comment/<int:post>/',views.CommentView.as_view()),
    path('comment/delete/<int:user>/<int:pk>/',views.CommentDeleteView.as_view()),
    path('comment/update/<int:user>/<int:pk>/',views.CommentUpdateView.as_view()),
]
