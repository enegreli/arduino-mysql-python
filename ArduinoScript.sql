CREATE DATABASE IF NOT EXISTS ClimaWeb;

USE ClimaWeb;

CREATE TABLE IF NOT EXISTS DadosClimaticos(
	id int auto_increment,
    temperatura float not null,
    umidade float not null,
    data_hora timestamp default current_timestamp,
    primary key(id)
);

Select * from DadosClimaticos;