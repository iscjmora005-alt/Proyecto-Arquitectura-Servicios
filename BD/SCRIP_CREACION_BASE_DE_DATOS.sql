-- 1. creación de la base de datos
create database if not exists gestion_salas_itesz;
use gestion_salas_itesz;

-- 2. tabla departamentos 
create table departamentos (
    id_departamento int auto_increment primary key,
    nombre varchar(100) not null
);

-- 3. tabla salas (tabla maestra)

create table salas (
    id_sala int auto_increment primary key,
    nombre varchar(100) not null,
    capacidad int not null,
    estatus char(1) default 'd', -- 'd' para disponible, 'm' mantenimiento, etc.
    id_departamento int,
    constraint fk_sala_departamento 
        foreign key (id_departamento) references departamentos(id_departamento)
        on delete set null on update cascade
);

-- 4. tabla equipamiento
-- vinculada estrictamente a una sala
create table equipamiento (
    id_equipamiento int auto_increment primary key,
    numerodeserie varchar(50) unique not null,
    estado varchar(50),
    cantidad int not null,
    caracteristicas text,
    id_sala int not null,
    constraint fk_equipamiento_sala 
        foreign key (id_sala) references salas(id_sala)
        on delete cascade on update cascade
);

-- 5. tabla mobiliario
-- vinculada a una sala
create table mobiliario (
    id_mobiliario int auto_increment primary key,
    nombre varchar(100) not null,
    descripcion text,
    tipo varchar(50),
    id_sala int not null,
    constraint fk_mobiliario_sala 
        foreign key (id_sala) references salas(id_sala)
        on delete cascade on update cascade
);

-- 6. creación de vistas (requerimiento de la unidad 3) 
-- esta vista facilita consultar qué equipos hay en cada sala sin hacer joins manuales
create view vista_inventario_salas as
select 
    s.nombre as sala,
    s.capacidad,
    e.numerodeserie as serie_equipo,
    e.estado as estado_equipo,
    e.cantidad as cantidad_equipo,
    d.nombre as departamento
from salas s
join departamentos d on s.id_departamento = d.id_departamento
left join equipamiento e on s.id_sala = e.id_sala;
