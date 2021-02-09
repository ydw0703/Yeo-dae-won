-- desc city;

-- desc country;

-- select * 
-- from city
/*row you wanted*/
-- where population > 8000000;
-- where CountyCode = 'KOR';
-- where NAME IN('Seoul','New York');
-- where name like 'Tel %';
-- where population > ANY(=SOME),ALL = where을 만족하는 값을 모두 보여라! (select population
	-- 					from city
    --                  where District = 'New York');
-- order by population desc, CountryCode asc
-- select * 
-- from country
-- order by SurfaceArea desc;

-- select distinct CountryCode
-- From city;

-- select CountryCode,min(population) as 'max pop'
-- from city
-- group by CountryCode
-- having max(population) > 8000000; -- 집계 함수에 대해서 조건 제한하는 개념

-- select *
-- from city
-- join country on city.CountryCode = country.Code

-- select locate('abc','cadasdfacabc');

-- select count(*)
-- from city;

-- select floor(10.95), ceil(10.1), round(1.25)
-- select sqrt(4), pow(2,3)(2의 세제곱), exp(3)(e의 세제곱), log(3)

-- select abs(-3), rand(), round(rand()*100,0);

-- select now(), curdate(),curtime(),date(now()),second(now()),dayname(now()),monthname(now())
-- dayofyear(),dayofweek(),dayofmonth()

-- select date_format(now(),'%D %y %a %d %m %n %j');
-- create database daewon;
-- desc test; 

-- alter table test;
-- /*(drop,modify)*/ADD col4 int null;

-- desc test;

-- alter table test
-- modify col4 varchar(20) null;

-- create unique index Col2Idx
-- on test(col2);
-- show index from test;

-- use world

-- CREATE VIEW allView as 
-- select city.name, country.SurfaceArea, city.Population, countrylanguage.Language
-- from city
-- join country on city.CountryCode = country.Code
-- join countrylanguage on city.CountryCode = countrylanguage.CountryCode
-- where city.countryCode = 'KOR';

-- select * from allView;


INSERT INTO test
value(1,1,1);

select * from test;

insert into test2 select *from test;

select * from test2;

desc test;

-- where을 써주지 않으면 모든 데이터가 삭제될 수 있으니 주의바람!
update test
set col1=1, col2=5
where id = 1;

select * from test;

-- 복구 가능 데이터 삭제
delete from test
where id =1;

select * from test;

-- 복구 불가 데이터 삭제
-- truncate table  test
-- where id =1;

-- select * from test;

-- 테이블 삭제
-- drop table test

-- select * from test;

drop database daewon
