from django.urls import path

from .views import list_koders, get_koder, list_mentors, list_Koders_ant
#  ruta  ->  http://127.0.0.1:8000/

urlpatterns = [
    path("koders/<int:koder_id>", get_koder),
    path("koders/",list_koders),
    path("mentors/", list_mentors),
    path("koder/",list_Koders_ant)
]