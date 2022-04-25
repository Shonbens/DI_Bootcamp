/*
1) SELECT * FROM public.customer
2) SELECT  first_name, last_name, CONCAT(first_name, last_name) AS full_name
FROM public.customer;
3)select distinct create_date FROM public.customer
4)select * FROM public.customer order by first_name asc
5)SELECT film_id,title,description,release_year,rental_rate FROM public.film
order by rental_rate asc
6)SELECT address, phone FROM public.address where district = 'Texas'
7)select description FROM public.film where film_id in (50,150)
8)select * FROM public.film where title = 'Zorro Ark'
9)select * FROM public.film where title >= 'Zo'
10)select title FROM public.film order by rental_rate desc limit 10
11)select title FROM public.film order by rental_rate desc limit 20
12)SELECT customer_id as costomer_name
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id;

*/


