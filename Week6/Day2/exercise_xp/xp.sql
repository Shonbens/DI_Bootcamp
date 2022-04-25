/*
1) select * from items order by price asc
2) select * from items where price >= 80 order by price desc
3) SELECT * FROM COSTUMERS WHERE ID IN (1, 2, 3) order by person asc
select last_name from costumers order by last_name desc
CREATE TABLE purchases(
id integer PRIMARY KEY,
costumer_id integer,
item_id integer,
quantity_purchased integer,
FOREIGN KEY (costumer_id) REFERENCES costumers (id),
FOREIGN KEY (item_id) REFERENCES items (id)
);

4) INSERT INTO purchases (id, costumer_id, item_id, quantity_purchased) VALUES
	 (1,(SELECT id from costumers where person = 'Scott' AND last_name = 'Scott')
	 ,(SELECT id from items where item = 'Fan'), 1 )

INSERT INTO purchases (id, costumer_id, item_id, quantity_purchased) VALUES
	(2,(SELECT id from costumers where person = 'Melanie' AND last_name = 'Johnson')
	,(SELECT id from items where item = 'Large Desk'), 10 );
	
	INSERT INTO purchases (id, costumer_id, item_id, quantity_purchased) VALUES
	(3,(SELECT id from costumers where person = 'Greg' AND last_name = 'Jones')
	,(SELECT id from items where item = 'Small Desk'), 2 );
	
part 2

1)select * from purchases
3)select * from purchases where costumer_id = 5
4)select * from purchases where item_id = 2 and item_id = 3

select costumers.person, costumers.last_name
from costumers
inner join purchases
on costumers.id = purchases.id

*/


	
