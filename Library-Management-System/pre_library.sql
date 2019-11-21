create database if not exists library;
use library;
start transaction;
set time_zone = "00:00";

#	admin_table	#

create table admin (id int,user_name varchar(255),password varchar(255));
insert into admin(id,user_name,password)values('1','pd',123);
select * from admin;

#	admin_login_details table	#

create table admin_login_detail (id int, login_time datetime);
insert into admin_login_detail(id,login_time) values(1,'2019-10-31 23:02:02');
select* from admin_login_detail;

#	book_details table	#

create table book_details
(book_code  varchar(255),book_name varchar(255),
author varchar(255),publisher varchar(255),
pages int,rack varchar(255),issued int);
insert into book_details 
(book_code,book_name,author,publisher,pages,rack,issued) 
VALUES('123', 'maths', 'ps', 'nk', 10, 'a23', 1);
select * from book_details;

#	issued_book	table	#

create table issued_books (
user_id varchar(255),book_code varchar(255),
issued_on varchar(255),return_date varchar(255));
INSERT INTO issued_books (user_id, book_code, issued_on, return_date)
 VALUES('pahul', '123', '12/10/19', '22/10/19');
 select * from issued_books;
 
 #		user_details table		#
 
 create table user_details
 (user_id varchar(255),name varchar(255),
 department varchar(255),phone varchar(255),
 password varchar(255));
 insert into user_details(user_id,name,department,phone,password)
 values('11701144_ce17','pahuldeep singh','cse',8146342693,1234);
 select * from user_details;
 
 #		user_login_details table	#
 
 CREATE TABLE user_login_details (user_id varchar(255),login_time datetime);
INSERT INTO user_login_details (user_id, login_time) 
VALUES('11701144_ce17', '2019-10-31 23:02:02');
select * from user_login_details;
 