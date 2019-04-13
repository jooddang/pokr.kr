-- $ psql -U postgres

create database pokr with owner = postgres encoding='utf8';
\c pokr;
create table person;
create table person (id bigserial primary key);
create table party (id bigserial primary key);
create table candidacy (id bigserial primary key);
create table election (id bigserial primary key);
alter table election add column age integer;
alter table candidacy add column election_id integer;
alter table candidacy add column person_id integer;
alter table candidacy add column party_id integer;
alter table candidacy add column region3 integer;
alter table candidacy add column region2 integer;
alter table candidacy add column region1 integer;
alter table person add column addr_city integer;
alter table person add column addr_country integer;
alter table person add column addr_county integer;
alter table person add column addr_detail integer;
create table experience (id bigserial primary key);
create table education (id bigserial primary key);
create table school (id bigserial primary key);
alter table school add column name varchar(100);
alter table person add column birth_county varchar(100);
alter table person add column birth_city varchar(100);
create table school (id bigserial primary key);
create table party_affiliation (id bigserial primary key);
alter table party_affiliation add column date date;
alter table election add column date varchar(20);
alter table person add column name varchar(20);
alter table person add column name_en varchar(50);

-- now, run 
-- $ alembic upgrade head
