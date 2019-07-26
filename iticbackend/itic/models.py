from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Nivel (models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Formacion_Academica(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    institucion = models.CharField(max_length=100,blank=True, null=True)
    abrebiacion = models.CharField(max_length=10, blank=True, null=True)
    nivel = models.ForeignKey(Nivel,on_delete=models.DO_NOTHING,default="1")
    def __str__(self):
        return self.nombre
class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    foto = models.FileField(upload_to="img/maestros/", blank=True, null=True)#barra despues
    formacion = models.ManyToManyField(Formacion_Academica,verbose_name=("Formacion Academica"),blank=True) 
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 2 __unicode__
        return self.email

class Tag(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True,auto_now=False)
    actualizado = models.DateField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.nombre

class New(models.Model):
    titulo = models.CharField(max_length=100,blank=True, null=True)
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name="Author", default=1)
    foto = models.FileField(upload_to="noticias/",blank=True, null=True)
    descripcion = HTMLField(max_length=300, blank=True, null=True)
    body = HTMLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=("Tags"))
    timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=True, null=True)
    actualizado = models.DateField(auto_now=True,auto_now_add=False,blank=True, null=True)
    def __str__(self):
        return self.titulo
class Archivo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    archivo = models.FileField(upload_to="files/", blank=True, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.nombre
        
class Proceso(models.Model):
    ESTADOS = ((1,"Si"),(2,"No"))
    TIPO =((1,"Residencias"),(2,"Servicio"))
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = HTMLField()
    color = models.CharField(max_length=15,blank=True, null=True)
    archivos= models.IntegerField(choices=ESTADOS,default=2,verbose_name=("Contiene Archivos"))
    tipo_proceso= models.IntegerField(choices=TIPO,default=1,verbose_name=("Tipo de Proceos"))
    archivo_proceso = models.ManyToManyField(Archivo, verbose_name=("archivos"),blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.nombre
class Semestre (models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    
class Matter (models.Model):
    clave = models.CharField(max_length=18,blank=True, null=False,primary_key=True, unique=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = HTMLField(max_length=300, blank=True, null=True)
    horas_practicas = models.IntegerField(blank=True, null=True)
    horas_escritas = models.IntegerField(blank=True, null=True)
    semestre = models.ForeignKey(Semestre,on_delete=models.DO_NOTHING,default=1)
    archivo = models.ForeignKey(Archivo,on_delete=models.DO_NOTHING,default=1)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.clave


