--  (INSERTS)

-- Insertar Departamentos
INSERT INTO Departamentos (nombre) VALUES 
('Sistemas Computacionales'),
('Ingeniería Industrial');

-- Insertar Salas
INSERT INTO Salas (nombre, capacidad, estatus, id_departamento) VALUES 
('Laboratorio Mac', 30, 'D', 1),
('Sala de Redes Cisco', 25, 'D', 1),
('Aula Magna', 100, 'D', 2);

-- Insertar Equipamiento
INSERT INTO Equipamiento (numeroDeSerie, estado, cantidad, caracteristicas, id_sala) VALUES 
('MAC-2025-001', 'Funcional', 1, 'iMac M3 8GB RAM', 1),
('CISCO-R-005', 'En revisión', 2, 'Router Cisco 2911', 2),
('PROY-EPSON-12', 'Funcional', 1, 'Proyector Epson 4000 lúmenes', 3);

-- Insertar Mobiliario
INSERT INTO Mobiliario (nombre, descripcion, tipo, id_sala) VALUES 
('Mesa de trabajo compartida', 'Mesa de madera para 4 alumnos', 'Mesa', 1),
('Rack de servidores', 'Rack abierto de 42U', 'Estante', 2),
('Silla ergonómica', 'Silla de oficina con soporte lumbar', 'Silla', 1);