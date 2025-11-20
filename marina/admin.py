from django.contrib import admin
from .models import (
    Jugador, Avatar, EspecieMarina, HabitatMarino,
    Mision, RecursoEducativo, AmenazaMarina, Contaminante, ObjetoRecolectable,
    Organizacion, ProyectoConservacion, AreaProtegida, EventoMarino,
    Logro, Recompensa,
    JugadorMision, EspecieAmenaza, EspecieHabitat,
    MisionContaminante, MisionRecurso, ProyectoOrganizacion
)

# -------------------
# Modelos principales
# -------------------

from django.contrib import admin
from .models import Jugador

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fechaAlta', 'idioma', 'privacidadRanking')
    search_fields = ('nombre', 'email')


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'idJugador', 'skin', 'ultimaEdicion')
    search_fields = ('nombre', 'idJugador__nombre')


@admin.register(EspecieMarina)
class EspecieMarinaAdmin(admin.ModelAdmin):
    list_display = ('nombreComun', 'nombreCientifico', 'estadoUICN')
    search_fields = ('nombreComun', 'nombreCientifico')


@admin.register(HabitatMarino)
class HabitatMarinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'descripcion')
    search_fields = ('nombre', 'region')


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'idHabitat', 'dificultad', 'puntos')
    search_fields = ('titulo',)


@admin.register(RecursoEducativo)
class RecursoEducativoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'url')
    search_fields = ('titulo', 'tipo')


@admin.register(AmenazaMarina)
class AmenazaMarinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')


@admin.register(Contaminante)
class ContaminanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'peligrosidad')
    search_fields = ('nombre', 'categoria')


@admin.register(ObjetoRecolectable)
class ObjetoRecolectableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'idContaminante', 'valorPuntos')
    search_fields = ('nombre',)


@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sitioWeb', 'pais')
    search_fields = ('nombre', 'pais')


@admin.register(AreaProtegida)
class AreaProtegidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'categoria')
    search_fields = ('nombre', 'pais', 'categoria')


@admin.register(ProyectoConservacion)
class ProyectoConservacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sitioWeb', 'idArea')
    search_fields = ('nombre',)


@admin.register(EventoMarino)
class EventoMarinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'idProyecto', 'fechaInicio', 'fechaFin', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')


@admin.register(Logro)
class LogroAdmin(admin.ModelAdmin):
    list_display = ('clave', 'idJugador', 'fecha')
    search_fields = ('clave', 'idJugador__nombre')


@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'idJugador', 'fecha')
    search_fields = ('tipo', 'idJugador__nombre')


# -------------------
# Tablas intermedias M:N
# -------------------

@admin.register(JugadorMision)
class JugadorMisionAdmin(admin.ModelAdmin):
    list_display = ('idJugador', 'idMision')
    search_fields = ('idJugador__nombre', 'idMision__titulo')


@admin.register(EspecieAmenaza)
class EspecieAmenazaAdmin(admin.ModelAdmin):
    list_display = ('idEspecie', 'idAmenaza')
    search_fields = ('idEspecie__nombreComun', 'idAmenaza__nombre')


@admin.register(EspecieHabitat)
class EspecieHabitatAdmin(admin.ModelAdmin):
    list_display = ('idEspecie', 'idHabitat')
    search_fields = ('idEspecie__nombreComun', 'idHabitat__nombre')


@admin.register(MisionContaminante)
class MisionContaminanteAdmin(admin.ModelAdmin):
    list_display = ('idMision', 'idContaminante')
    search_fields = ('idMision__titulo', 'idContaminante__nombre')


@admin.register(MisionRecurso)
class MisionRecursoAdmin(admin.ModelAdmin):
    list_display = ('idMision', 'idRecurso')
    search_fields = ('idMision__titulo', 'idRecurso__titulo')


@admin.register(ProyectoOrganizacion)
class ProyectoOrganizacionAdmin(admin.ModelAdmin):
    list_display = ('idProyecto', 'idOrg')
    search_fields = ('idProyecto__nombre', 'idOrg__nombre')
