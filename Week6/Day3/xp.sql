/*
1) select *from customer;
2) select (first_name, last_name) as full_name from customer;
3) select create_date from customer;
4) select * from customer order by first_name DESC;
5) select film_id, title, description, release_year, rental_rate from film order by rental_rate ASC;
6) select address, address2, phone from address where district = 'Texas';
7) select * from film where film_id = 15 or film_id = 150;
8)select film_id, title, description, length, rental_rate from film where title = 'Metropolis Coma'
9)select film_id, title, description, length, rental_rate from film where title ilike 'me%';
10)select title, rental_rate from film where rental_rate<=1 limit 10;
11) select title, rental_rate from film where rental_rate<=1 and title NOT (select title, rental_rate from film where rental_rate<=1 limit 10) limit 10;
12) select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer inner join payment on payment.customer_id = customer.customer_id
13)select city.city, country.country_id, country.country from city inner join country on city.country_id = country.country_id;
*/
/*
1)select * from language;
2)select film.title, film.description,language.name from film inner join language on film.language_id = language.language_id;
3)select film.title,film.description,language.name from film left outer join language on film.language_id = language.language_id;
4)select film.title,film.description,language.name from film full join language on film.language_id = language.language_id
*/
/*
1)create table new_film(
2)new_film_id serial primary key,
3)new_id NUMERIC,
4)new_name VARCHAR(50));
*/
/*
1)insert into new_film(new_id,new_name)
2)values (1,'Harry potter'),(2,'Hunger games'),(3,'Thor')
select * from new_film
*/
-- create table customer_review(
-- review_id serial primary key,
-- film_id INTEGER references new_film(new_film_id) on delete cascade,
-- language_id INTEGER references language(language_id),
-- title VARCHAR,
-- score NUMERIC check (score>=0 and score < 11 ),
-- review_text VARCHAR,
-- last_update timestamp without time zone);
-- select * from customer_review
-- drop table new_film cascade
-- select * from customer_review
-- drop table customer_review cascade
-- drop table new_film cascade
-- select * from customer_review
-- delete from new_film where new_name = 'Thor'