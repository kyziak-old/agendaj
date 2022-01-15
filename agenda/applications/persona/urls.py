# Django
from django.urls import path, re_path

#Views
from applications.persona import views

# app name

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.PersonaListView.as_view(),
        name='persona'
    )
]
