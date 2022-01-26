from django.urls import path 
from polls.views import IndexListView, CreateView

urlpatterns = [ 
	path('', IndexListView.as_view(), name='index'),
 	path('create/', CreateView.as_view(), name='create'),  
]