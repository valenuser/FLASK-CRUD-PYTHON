drop database if exists userFLASK;

create database userFLASK;

use userFLASK;

create table user(
	id int auto_increment PRIMARY KEY,
    nombre varchar(100),
    user_foto varchar(300)
);
