create database dragon_ball;

use dragon_ball;

create table dragon_ball
(
	name varchar(15)not null,
	race varchar(30)not null,
	move varchar(30)not null,
	gender varchar(15)not null,
	age int
);

select * from dragon_ball;
desc dragon_ball;

insert into dragon_ball
(name,race,move,gender,age)
values
('Goku','Super Saiyan','Kamehameha','Male','42');

insert into dragon_ball
values
('Vegeta','Super Saiyan','Galick Gun','Male','46');

insert into dragon_ball
values
('Gohan','Half-Human/Half-Saiyan','Kamehameha','Male','21');

insert into dragon_ball
values
('Piccolo','Namekian','Special Beam Cannon','Male','25');

insert into dragon_ball
values
('Beerus','God of Destruction','Sphere of Destrcution','Male','200');

drop table dragon_ball;
drop database dragon_ball;
