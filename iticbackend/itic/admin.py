from django.contrib import admin

#Imports models
from .models import (Archivo, Proceso, Teacher,Nivel,
                    Formacion_Academica,Tag,Formacion_Academica,New,
                    Matter)

# Register your models here.


class AdminProceso(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Proceso

class AdminArchivo(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Archivo
class AdminTeacher(admin.ModelAdmin):
    list_display = ["name","timestamp"]
    class Meta:
        modle = Teacher

class AdminNivel(admin.ModelAdmin):
    list_display  = ["nombre"]
    class Meta:
        modle = Nivel
class AdminFormacionAcademica(admin.ModelAdmin):
    list_display = ["nombre","institucion"]
    class Meta:
        modle = Formacion_Academica
class AdminTag(admin.ModelAdmin):
    list_display =  ["nombre"]

    class Meta:
        modle = Tag
class AdminNew(admin.ModelAdmin):
    list_display = ["titulo"]

    class Meta:
        modle = New
class AdminMatter(admin.ModelAdmin):
    list_display =["clave","name"]
    
    class Meta:
        modle = Matter

admin.site.register(Teacher,AdminTeacher)
admin.site.register(Nivel,AdminNivel)
admin.site.register(Formacion_Academica,AdminFormacionAcademica)
admin.site.register(Tag,AdminTag)
admin.site.register(New,AdminNew)
admin.site.register(Proceso,AdminProceso)
admin.site.register(Archivo,AdminArchivo)
admin.site.register(Matter,AdminMatter)