from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name = 'user_view'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name = 'user_view'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]