from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('invite-driver/', views.invite_driver),
    path('drivers/', views.drivers_list),
    path('drivers/<int:driver_id>/', views.driver_detail),
    path('onboard/<uuid:token>/', views.onboard_driver),

    # 🔥 actions
    path('drivers/<int:driver_id>/activate/', views.mark_active),
    path('drivers/<int:driver_id>/reject/', views.reject_driver),
]