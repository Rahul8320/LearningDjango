from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.all_chai, name='all_chai'),
    path('<int:chai_id>/', view=views.chai_details, name='chai_details'),
    path('store/', view=views.chai_stores, name="chai_stores")
]
