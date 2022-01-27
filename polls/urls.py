from django.urls import path 
from polls.views import IndexListView, CreateView, UpdateView, DeleteView

urlpatterns = [ 
	path('', IndexListView.as_view(), name='index'),
 	path('create/', CreateView.as_view(), name='create'),  
        path('update/<int:pk>/', UpdateView.as_view(), name='update'), 
        path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
]