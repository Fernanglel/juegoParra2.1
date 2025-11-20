-- Base de Datos
CREATE DATABASE IF NOT EXISTS MarinoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE MarinoDB;

-- Tabla NivelJuego
CREATE TABLE NivelJuego (
    idNivel INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    umbralXP INT NOT NULL
) ENGINE=InnoDB;

-- Tabla Jugador
CREATE TABLE Jugador (
    idJugador INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    fechaAlta DATE NOT NULL,
    idioma VARCHAR(50),
    privacidadRanking BOOLEAN DEFAULT TRUE,
    idNivel INT,
    FOREIGN KEY (idNivel) REFERENCES NivelJuego(idNivel)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla Avatar
CREATE TABLE Avatar (
    idAvatar INT AUTO_INCREMENT PRIMARY KEY,
    idJugador INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    skin VARCHAR(100),
    accesorios TEXT,
    ultimaEdicion DATETIME,
    FOREIGN KEY (idJugador) REFERENCES Jugador(idJugador)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla EspecieMarina
CREATE TABLE EspecieMarina (
    idEspecie INT AUTO_INCREMENT PRIMARY KEY,
    nombreCientifico VARCHAR(255) NOT NULL,
    nombreComun VARCHAR(255),
    estadoUICN VARCHAR(50),
    descripcion TEXT,
    fuente VARCHAR(255),
    fechaFuente DATE
) ENGINE=InnoDB;

-- Tabla HabitatMarino
CREATE TABLE HabitatMarino (
    idHabitat INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    region VARCHAR(100),
    descripcion TEXT
) ENGINE=InnoDB;

-- Tabla Mision
CREATE TABLE Mision (
    idMision INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    idHabitat INT,
    dificultad INT,
    puntos INT,
    objetivosJSON JSON,
    FOREIGN KEY (idHabitat) REFERENCES HabitatMarino(idHabitat)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla RecursoEducativo
CREATE TABLE RecursoEducativo (
    idRecurso INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    tipo VARCHAR(50),
    url VARCHAR(255),
    licencia VARCHAR(100),
    fuente VARCHAR(255)
) ENGINE=InnoDB;

-- Tabla AmenazaMarina
CREATE TABLE AmenazaMarina (
    idAmenaza INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(50)
) ENGINE=InnoDB;

-- Tabla Contaminante
CREATE TABLE Contaminante (
    idContaminante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    peligrosidad VARCHAR(50)
) ENGINE=InnoDB;

-- Tabla ObjetoRecolectable
CREATE TABLE ObjetoRecolectable (
    idObjeto INT AUTO_INCREMENT PRIMARY KEY,
    idContaminante INT,
    nombre VARCHAR(100) NOT NULL,
    valorPuntos INT,
    FOREIGN KEY (idContaminante) REFERENCES Contaminante(idContaminante)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla Organizacion
CREATE TABLE Organizacion (
    idOrg INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    sitioWeb VARCHAR(255),
    pais VARCHAR(100)
) ENGINE=InnoDB;

-- Tabla AreaProtegida
CREATE TABLE AreaProtegida (
    idArea INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    pais VARCHAR(100),
    categoria VARCHAR(50),
    regulacion TEXT
) ENGINE=InnoDB;

-- Tabla ProyectoConservacion
CREATE TABLE ProyectoConservacion (
    idProyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    sitioWeb VARCHAR(255),
    idArea INT,
    FOREIGN KEY (idArea) REFERENCES AreaProtegida(idArea)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla EventoMarino
CREATE TABLE EventoMarino (
    idEvento INT AUTO_INCREMENT PRIMARY KEY,
    idProyecto INT,
    nombre VARCHAR(255) NOT NULL,
    fechaInicio DATE,
    fechaFin DATE,
    ubicacion VARCHAR(255),
    FOREIGN KEY (idProyecto) REFERENCES ProyectoConservacion(idProyecto)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla Logro
CREATE TABLE Logro (
    idLogro INT AUTO_INCREMENT PRIMARY KEY,
    idJugador INT,
    clave VARCHAR(100),
    descripcion TEXT,
    fecha DATE,
    FOREIGN KEY (idJugador) REFERENCES Jugador(idJugador)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tabla Recompensa
CREATE TABLE Recompensa (
    idRecompensa INT AUTO_INCREMENT PRIMARY KEY,
    idJugador INT,
    tipo VARCHAR(50),
    valor INT,
    fecha DATE,
    FOREIGN KEY (idJugador) REFERENCES Jugador(idJugador)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Tablas de relaciones M:N

-- JugadorMision
CREATE TABLE JugadorMision (
    idJugador INT,
    idMision INT,
    PRIMARY KEY (idJugador, idMision),
    FOREIGN KEY (idJugador) REFERENCES Jugador(idJugador)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idMision) REFERENCES Mision(idMision)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- EspecieAmenaza
CREATE TABLE EspecieAmenaza (
    idEspecie INT,
    idAmenaza INT,
    PRIMARY KEY (idEspecie, idAmenaza),
    FOREIGN KEY (idEspecie) REFERENCES EspecieMarina(idEspecie)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idAmenaza) REFERENCES AmenazaMarina(idAmenaza)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- EspecieHabitat
CREATE TABLE EspecieHabitat (
    idEspecie INT,
    idHabitat INT,
    PRIMARY KEY (idEspecie, idHabitat),
    FOREIGN KEY (idEspecie) REFERENCES EspecieMarina(idEspecie)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idHabitat) REFERENCES HabitatMarino(idHabitat)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- MisionContaminante
CREATE TABLE MisionContaminante (
    idMision INT,
    idContaminante INT,
    PRIMARY KEY (idMision, idContaminante),
    FOREIGN KEY (idMision) REFERENCES Mision(idMision)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idContaminante) REFERENCES Contaminante(idContaminante)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- MisionRecurso
CREATE TABLE MisionRecurso (
    idMision INT,
    idRecurso INT,
    PRIMARY KEY (idMision, idRecurso),
    FOREIGN KEY (idMision) REFERENCES Mision(idMision)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idRecurso) REFERENCES RecursoEducativo(idRecurso)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ProyectoOrganizacion
CREATE TABLE ProyectoOrganizacion (
    idProyecto INT,
    idOrg INT,
    PRIMARY KEY (idProyecto, idOrg),
    FOREIGN KEY (idProyecto) REFERENCES ProyectoConservacion(idProyecto)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idOrg) REFERENCES Organizacion(idOrg)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;
