from django.urls import path
from tasks import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.TaskListView.as_view(), name="tasks-list"),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('comment-update/<int:pk>/', views.CommentUpdateView.as_view() ,name='comment-update' )
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)