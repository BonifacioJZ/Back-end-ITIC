from rest_framework import routers
from .viewsets import (TeacherViewSet,NivelViewSet,FormacionAcademicaViewSet,
NewViewSet,UserViewSet,TagViewSet,ArchivoViewSet,ProcesoViewSet,MatterViewSet)


router = routers.SimpleRouter()
router.register('usuarios',UserViewSet)
router.register('teachers',TeacherViewSet)
router.register('niveles',NivelViewSet)
router.register('formacion',FormacionAcademicaViewSet)
router.register('news',NewViewSet)
router.register('tags',TagViewSet)
router.register('archivos',ArchivoViewSet)
router.register('procesos',ProcesoViewSet)
router.register('matters',MatterViewSet)
urlpatterns = router.urls
