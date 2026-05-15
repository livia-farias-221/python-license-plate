USE placas_db;
 CREATE TABLE placas_carros ( id_placa int AUTO_INCREMENT PRIMARY KEY, placa VARCHAR(7) UNIQUE NOT NULL, data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
 SELECT * FROM placas_carros;

