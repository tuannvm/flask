-- UPDATE
UPDATE items set price=10.00 where name = '';

-- DELETE
Delete from items where id = 4;

-- WILDCARD
select * from customers where last_name like '%t%'; -- anything have t char in the middle
select * from customers where last_name like '%t_'; -- anything have t char in the middle, and exacly one char after

-- JOIN
select * from customers inner join orders on customers.id = orders.customer_id; -- intersection like set, take the records which occur in both tables, most common

select * from customers left join orders on customers.id = orders.customer_id; -- list all record on the left table even it doesn not match data on the right table (left blank), most common

select * from customers right join orders on customers.id = orders.customer_id; -- list all record on the right table even it doesn not match data on the left table (left blank)

select * from customers full join orders on customers.id = orders.customer_id; -- list all record on the both tables even it doesn not match data of each other (left blank)

select customers.first_name, customers.last_name, items.name, items.price from customers inner join purchases on customers.id = purchases.customer_id
inner join items on purchases.item_id = items.id; --  join 3 tables together, display selected columns

-- SUM, GROUP BY, COUNT
select customers.first_name, customers.last_name, sum(items.price), count(customers.id) from customers inner join purchases on customers.id = purchases.customer_id
inner join items on purchases.item_id = items.id group by customers.id; --  join 3 tables, calculate how much money 1 customer spend, how many items each customer bought

select sum(items.price) from items inner join purchases on items.id = purchases.item_id; --  calculate total money spent

-- ORDER BY
select customers.first_name, customers.last_name, sum(items.price) as total_spent from customers inner join purchases on customers.id = purchases.customer_id
inner join items on purchases.item_id = items.id group by customers.id order by total_spent; -- notice ORDER BY keyword


--  Create table
create table public.videos (
id int4,
customer_id int4,
name character varying(255) not null,
constraint videos_pkey primary key (id),
constraint fk_videos_customers foreign key (customer_id) references public.customers(id)
);

-- INSERT
INSERT into public.users values (1, 'jose');


-- AUTO INCREMENT
create sequence users_id_seq start 2; -- create auto increment variable

alter table public.users
alter column id
set default nextval('users_id_seq'); --  change users.id next value by using variable just created

alter sequence users_id_seq owned by public.users.id; -- create a dependency between sequence and id, so deleting id cause the same result on sequence

-- SERIAL: easier to use than sequence
create table public.test(
    id serial primary key,
    name character varying(255)
)



-- INDEX (help boosting query)
create index users_name_index on public.users(name); -- create index on single field

create index index_name on public.videos(id, user_id); -- helpful when ofen use 2 condition query (AND)

reindex index users_name_index; -- fixing corrupted index
reindex database learning; -- fixing corrupted database

-- DROP
drop table public.users cascade; -- remove the foreign key relationship between current table and others (2 WAYS), data is untouched


-- VIEW
create view total_spent_by_customer as
select customers.first_name, customers.last_name, sum(items.price) as total_spent from customers 
inner join purchases on customers.id = purchases.customer_id
inner join items on purchases.item_id = items.id 
group by customers.id order by total_spent; # we can use view to shorten the query,making it much more easier to revisit the full-length query, CAN NOT INSERT to view because "group by" contained

drop view total_spent_by_customer; # drop query

create view expensive_items as
select * from items where price >= 100 with local check option; #will affect the insert later on, need to obey the check

insert into expensive_items(name, id, price) values ('book', 7, 7); -- Failed, because price = 7 < 100 local check option --> can not insert

create view unluxury_items as
select * from expensive_items where price >= 1000 with local check option; -- create view from another view


-- Built-in functions

-- -- AVG, SUM, COUNT
select avg(items.price) from items;

-- -- MAX
select max(items.price) from items inner join purchases on items.id = purchases.item_id; -- can not select item.name or else when using max function

-- HAVING
select customers.first_name, customers.last_name, count(purchases.id) as item_count from customers inner join purchases on customers.id = purchases.customer_id group by customers.id having count(purchases.id) > 2; -- similiar to WHERE, which can not be used in this case (already grouped), always use having to check condition when querying with GROUP BY

-- TYPE
create type mood as enum('angry', 'sad', 'okay', 'happy', 'horny'); -- create new custom mood

create table public.students (
    name character varying(255),
    current_mood mood
) -- how to create table with custom data type

select * from students where current_mood > 'okay'; -- which return 'happy' and 'horny'

-- Nested select 
-- -- select * from items where price > avg(price) --> FAILED
select * from items where price > (select avg(price) from items); -- price larger than average price

select items.name, items.price - (select avg(price) from items) from items; -- price diff

select items.name, items.price - (select avg(price) from items where price > 200) from items where price > 200; # price diff of the item price > 200

