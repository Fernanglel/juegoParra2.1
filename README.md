# 🌊 ODS 14 - Vida Submarina | Agenda 2030 🌎

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-0C4B33?logo=django)
![HTML5](https://img.shields.io/badge/HTML5-Ready-E34F26?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Responsive-1572B6?logo=css3)
![Unity](https://img.shields.io/badge/Unity-WebGL%20Game-000000?logo=unity)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

**ODS 14: Conservar y utilizar sosteniblemente los océanos, los mares y los recursos marinos para el desarrollo sostenible.**

Este proyecto es un **sitio web educativo interactivo** con el propósito de **fomentar la conciencia ambiental** sobre la protección de la vida submarina. Forma parte de una iniciativa académica inspirada en los **Objetivos de Desarrollo Sostenible (ODS)** de las Naciones Unidas. El sitio está implementado con **Django**, estilos modulares en CSS y contiene un **minijuego WebGL (Unity)** para educación interactiva.

---

## 🧭 Objetivo del proyecto

Difundir información verificada y accesible sobre:
- El estado de los océanos y ecosistemas marinos.
- Los desafíos ambientales (contaminación, sobrepesca, acidificación, pérdida de biodiversidad, calentamiento).
- Soluciones basadas en ciencia, políticas y participación ciudadana.
- Promover la acción mediante materiales, herramientas y un videojuego educativo.

---

## 📘 Resumen técnico

- **Framework principal:** Django  
- **Base de datos:** SQLite (`db.sqlite3`) — usado para desarrollo/local  
- **Frontend:** HTML5, CSS3 (modular), Font Awesome (íconos), Bootstrap (local)  
- **Interactividad / Juego:** Unity WebGL build en `static/Web/`  
- **Plantillas:** `templates/` (index, challenges, solutions, resources, take-action)  
- **Estilos:** `static/styles/` (`baseStyle.css`, `layout.css`, `resources.css`)  
- **Bootstrap (local):** `static-storage/bootstrap4/`

---

## 📂 Estructura principal del repositorio

manage.py
db.sqlite3
requirements.txt
demo/ # configuración del proyecto (settings, urls, wsgi/asgi)
home/ # aplicación Django principal
templates/
├─ index.html
├─ challenges.html
├─ solutions.html
├─ resources.html
└─ take-action.html
static/
├─ styles/
│ ├─ baseStyle.css
│ ├─ layout.css
│ ├─ index.css
│ └─ resources.css
├─ images/ # imágenes usadas en las páginas (challenges, solutions, recursos)
└─ Web/ # Build Unity WebGL (Build/, TemplateData/)
static-storage/
└─ bootstrap4/ # Bootstrap local

> **Nota:** `db.sqlite3` se incluye para desarrollo local; en producción se recomienda no subir archivos de base de datos y usar algun motor de base de datos.

---

## ⚙️ Requisitos

- Python 3.10+ (recomendado 3.11/3.12)  
- pip  
- (Opcional) Entorno virtual `venv`  
- Navegador moderno con soporte WebGL (para ejecutar el build de Unity)

---

## 🚀 Instalación y ejecución (Windows - cmd.exe)

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Proyecto-ProgramacionWeb-V2.git
   cd Proyecto-ProgramacionWeb-V2

2. Crear y activar entorno virtual (opcional pero recomendado):
   ```bash
    python -m venv venv
    venv\Scripts\activate

3. Instalar dependencias:
   ```bash
    pip install -r requirements.txt

4. Ejecutar migraciones (si es necesario):
    ```bash
    python manage.py migrate

5. Crear superusuario (opcional):
    ```bash
    python manage.py createsuperuser

6. Iniciar servidor de desarrollo:
    ```bash
    python manage.py runserver

7. Abrir en el navegador:
    http://127.0.0.1:8000/

---

## 🔧 Configuración para producción (recomendaciones)
- Usar una base de datos robusta (Postgres, MySQL) — no `sqlite3`.
- Establecer `DEBUG = False` y configurar `ALLOWED_HOSTS` en `demo/settings.py`.
- Servir archivos estáticos con un servidor dedicado (nginx, CDN o S3).
- Ejecutar `python manage.py collectstatic` antes de desplegar.
- Configurar variables de entorno seguras (SECRET_KEY, DB credentials).

---

## 🧩 Contenido y páginas del sitio
- Inicio
    - Introducción al ODS 14, cifras clave y resumen de la importancia de los océanos.
- Desafios
    - Contaminación marina (plásticos, microplásticos, redes fantasma), sobrepesca, acidificación, pérdida de biodiversidad, calentamiento oceánico, eutrofización y destrucción de hábitats.
- Soluciones
    - Áreas marinas protegidas (AMPs), pesca sostenible, economía circular, políticas internacionales, restauración de manglares y praderas marinas, energías renovables para reducir CO₂, educación y gobernanza.
- Recursos
    - Materiales educativos, informes (FAO, ONU, UNESCO), documentales, herramientas interactivas (Global Fishing Watch, NASA Earth Data), campañas y participación ciudadana.
    - Contiene enlaces externos, iframes de video y tarjetas escolares descargables.
- Toma Accion
    - Minijuego educativo “Guardianes del Océano” (Unity WebGL).
    - Objetivo: enseñar de forma lúdica conceptos del ODS 14 mediante misiones de limpieza, restauración y protección.

---

## 🎮 Videojuego educativo — Guardianes del Océano
- Descripción breve:
    - Minijuego orientado a la enseñanza y concientización sobre la vida submarina.
    - Estado: build WebGL incluido integrado para desarrollo.

- Cómo probar el build localmente:
    - Asegúrate de que esté accesible y las rutas en las plantillas apunten correctamente.
    - Accede desde la plantilla que carga el `index.html` del build o abre el endpoint que sirve la página del juego.

---

## 🎨 Diseño y organización de estilos
- CSS modular:
    - `baseStyle.css` — variables globales (colores, tipografías).
    - `layout.css` — header y footer.
    - `resources.css` — grid y tarjetas de la página Recursos.
- Uso de Font Awesome para íconos.
- Grid responsive para tarjetas y secciones.
- Estética: paleta de azules oceánicos, buena accesibilidad y contraste.

---

## 📘 Fuentes verificadas y referencias
El contenido se ha contrastado con fuentes oficiales y científicas, entre ellas:
- UNEP – Programa de las Naciones Unidas para el Medio Ambiente
- UNESCO – Ocean Decade / Ocean Literacy
- FAO – The State of World Fisheries and Aquaculture
- ONU – World Ocean Assessment
- NASA Earth Data
- Otras iniciativas: The Ocean Cleanup, Ghost Gear Initiative, Ocean Conservancy.

---

# 🧪 Pruebas y desarrollo
- Revisa `home/views.py` para entender las vistas principales y rutas.
- Edita plantillas en `templates/` y estilos en `static/styles/`.
- Usa DevTools en el navegador para depurar CSS y verificar la carga (códigos 200/304/404 en logs).
- Para probar el juego, abre la ruta que lo carga en la plantilla o navega al archivo index del build.

---

## 🧑‍💻 Créditos
- Autor / Mantenedor: Diego Cruz Patiño, Luz Maria Bautista Trejo, Fernando , Josue Samael Arenas Herrera, Leonardo 
- Carrera: Ingeniería en Sistemas
- Universidad: Instituto Tecnologico de Tijuana
- Año: 2025
- Agradecimientos: Naciones Unidas, UNESCO, FAO, UNEP, NASA, The Ocean Cleanup, Ocean Conservancy y otras organizaciones que publican datos e iniciativas sobre conservación marina.

---
## 📫 Contacto y Contribuciones

- GitHub: https://github.com/DiegotsCodeHub
- Issues / Colaboración: Abre un issue en el repositorio o envía un email para coordinar contribuciones.
    1. Haz fork del repositorio.
    2. Crea una rama:
        ```bash
        git checkout -b feature/nueva-funcionalidad
    3. Realiza cambios y commits claros.
    4. Abre un Pull Request describiendo los cambios, pruebas realizadas y motivación.
    5. Mantén el estilo de código y la estructura de carpetas del proyecto.

---

## 📜 Licencia
Este proyecto se distribuye bajo la Licencia MIT — uso, modificación y distribución permitidos con fines educativos y de divulgación ambiental.

---

“Proteger los océanos es proteger la vida misma. Cada acción cuenta.” 🌍💙
— Diego Cruz Patiño | Proyecto ODS 14 - Vida Submarina
