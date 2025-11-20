from django.db import models

# Create your models here.

# -------------------
# Tablas principales
# -------------------
from django.db import models

from django.db import models

# -------------------
# Tablas principales
# -------------------



class Jugador(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    fechaAlta = models.DateField()
    idioma = models.CharField(max_length=50, blank=True)
    privacidadRanking = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre


class Avatar(models.Model):
    idJugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="avatars")
    nombre = models.CharField(max_length=100)
    skin = models.CharField(max_length=100, blank=True)
    accesorios = models.TextField(blank=True)
    ultimaEdicion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.idJugador.nombre})"


class EspecieMarina(models.Model):
    nombreCientifico = models.CharField(max_length=255)
    nombreComun = models.CharField(max_length=255, blank=True)
    estadoUICN = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField(blank=True)
    fuente = models.CharField(max_length=255, blank=True)
    fechaFuente = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombreComun or self.nombreCientifico


class HabitatMarino(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    especies = models.ManyToManyField(EspecieMarina, through='EspecieHabitat', related_name='habitats')

    def __str__(self):
        return self.nombre


class Mision(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    idHabitat = models.ForeignKey(HabitatMarino, on_delete=models.SET_NULL, null=True, blank=True)
    dificultad = models.IntegerField(default=1)
    puntos = models.IntegerField(default=0)
    objetivosJSON = models.JSONField(blank=True, null=True)
    jugadores = models.ManyToManyField(Jugador, through='JugadorMision', related_name='misiones')
    contaminantes = models.ManyToManyField('Contaminante', through='MisionContaminante', blank=True)
    recursos = models.ManyToManyField('RecursoEducativo', through='MisionRecurso', blank=True)

    def __str__(self):
        return self.titulo


class RecursoEducativo(models.Model):
    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    licencia = models.CharField(max_length=100, blank=True)
    fuente = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.titulo


class AmenazaMarina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=50, blank=True)
    especies = models.ManyToManyField(EspecieMarina, through='EspecieAmenaza', related_name='amenazas')

    def __str__(self):
        return self.nombre


class Contaminante(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, blank=True)
    peligrosidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre


class ObjetoRecolectable(models.Model):
    idContaminante = models.ForeignKey(Contaminante, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    valorPuntos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Organizacion(models.Model):
    nombre = models.CharField(max_length=255)
    sitioWeb = models.URLField(blank=True)
    pais = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class AreaProtegida(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100, blank=True)
    categoria = models.CharField(max_length=50, blank=True)
    regulacion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class ProyectoConservacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    sitioWeb = models.URLField(blank=True)
    idArea = models.ForeignKey(AreaProtegida, on_delete=models.SET_NULL, null=True, blank=True)
    organizaciones = models.ManyToManyField(Organizacion, through='ProyectoOrganizacion', blank=True)

    def __str__(self):
        return self.nombre


class EventoMarino(models.Model):
    idProyecto = models.ForeignKey(ProyectoConservacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    ubicacion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


class Logro(models.Model):
    idJugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    clave = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.clave} ({self.idJugador.nombre})"


class Recompensa(models.Model):
    idJugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    valor = models.IntegerField(default=0)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} ({self.idJugador.nombre})"


# -------------------
# Tablas intermedias M:N
# -------------------

class JugadorMision(models.Model):
    idJugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    idMision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idJugador', 'idMision')


class EspecieAmenaza(models.Model):
    idEspecie = models.ForeignKey(EspecieMarina, on_delete=models.CASCADE)
    idAmenaza = models.ForeignKey(AmenazaMarina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idEspecie', 'idAmenaza')


class EspecieHabitat(models.Model):
    idEspecie = models.ForeignKey(EspecieMarina, on_delete=models.CASCADE)
    idHabitat = models.ForeignKey(HabitatMarino, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idEspecie', 'idHabitat')


class MisionContaminante(models.Model):
    idMision = models.ForeignKey(Mision, on_delete=models.CASCADE)
    idContaminante = models.ForeignKey(Contaminante, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idMision', 'idContaminante')


class MisionRecurso(models.Model):
    idMision = models.ForeignKey(Mision, on_delete=models.CASCADE)
    idRecurso = models.ForeignKey(RecursoEducativo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idMision', 'idRecurso')


class ProyectoOrganizacion(models.Model):
    idProyecto = models.ForeignKey(ProyectoConservacion, on_delete=models.CASCADE)
    idOrg = models.ForeignKey(Organizacion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idProyecto', 'idOrg')
