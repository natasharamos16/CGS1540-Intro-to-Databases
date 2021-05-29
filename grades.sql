create database week11;
use week11;

create table grades
(SName varchar(10), Assgn varchar(15), Grade INT);

drop table grades;
load data local infile 'C:/Users/tasha/Downloads/Week11/grades.csv'
into table grades
fields terminated by ',' escaped by '\\'
lines terminated by '\r\n'
ignore 1 lines;

select * from grades;

select Assgn from grades;

select SName from grades;

update grades 
set Assgn=CONCAT('HW',right(Assgn,1));

update grades 
set SName=concat(upper(LEFT(SName, 1)),right(Lower(substring(SName,7,3)-1)));

select * from grades;
alter table grades
add column id int not null auto_increment first,
add primary key (id);

alter table grades
    Add column sids int not null after id;

update grades
set sids=(case 
	when SName = Jesse then '1'
	when SName = Julio then '2'
	when SName = Percy then '3'
	when SName = Samantha then '4'
	else sids
end);

select sids from grades;

select SName, count(*), sum(grade), avg(grade), sum(grade)/count(*) from grades group by SName;

update grades 
set Grade = 0 
where Grade IS null;

select Grade from grades;

select Assgn, avg(Grade), Min(Grade), Max(Grade) from grades group by Grade desc;

 SELECT Grade,
            (case when Grade >= 90 then 'A'
                  when Grade >= 80 then 'B'
                  when Grade >= 70 then 'C'
                  else 'F'
             end) as Grade
     FROM grades;


