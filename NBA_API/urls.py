from django.urls import path
from NBA_API import views
# from api import views

urlpatterns = [
    path('users/create', views.UserCreationAPIView.as_view(), name='user-creation'),
    path('users/all', views.AllUsersRetrievalAPIView.as_view(), name='user-retrieval'),
    path('users/<int:id>', views.UserRetrievalAPIView.as_view(), name='user-retrieval-by-id'),
]