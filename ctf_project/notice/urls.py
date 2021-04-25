from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeDeleteView
)
from . import views

urlpatterns = [
    path('', NoticeListView.as_view(), name='notice-home'),
    path('notice/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'),
    # create and update use the same template (notice_form.html)
    path('notice/create/', NoticeCreateView.as_view(), name='notice-create'),
    path('notice/update/<int:pk>/', NoticeUpdateView.as_view(), name='notice-update'),
    # delete use notice_confirm_delete.html for its template
    path('notice/delete/<int:pk>/', NoticeDeleteView.as_view(), name='notice-delete'),
    path('contact/', views.contact, name='notice-contact'),
]