-- creating a data base

 CREATE DATABASE sgm
     WITH 
     OWNER = postgres
     ENCODING = 'UTF8'
     LC_COLLATE = 'Russian_Russia.1251'
     LC_CTYPE = 'Russian_Russia.1251'
     TABLESPACE = pg_default
     CONNECTION LIMIT = -1;

-- creatind the first table: seller_info

     create table seller_info (seller_id integer not NULL, 
                    fruit_id  integer not null,
                    fruit_weight integer,
               
                CONSTRAINT seller_fruit_pk PRIMARY KEY (seller_id, fruit_id));
              
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (1, 1, 30);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (1, 2, 40);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (2, 3, 25);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (2, 4, 40);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (2, 5, 10);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (3, 6, 24);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (3, 7, 56);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (4, 8, 35);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (4, 9, 25);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (4, 10, 10);
        insert into seller_info (seller_id, fruit_id, fruit_weight) values (5, 11, 16);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (5, 12, 20);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (5, 13, 15);
          insert into seller_info (seller_id, fruit_id, fruit_weight) values (5, 14, 30);
      
-- displaying the result from the first table

  select * from seller_info;

-- creating the second table: consumption_info

     create table consumption_info (
                   client_id integer not null,
                   seller_id integer not null,
                   fruit_id integer not null, 
                   quantity_purchased_fruit integer,
     
                 CONSTRAINT clien_pk PRIMARY KEY (client_id));
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (1, 1, 1, 3);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (2, 2, 3, 2);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (3, 2, 4, 3);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (4, 1, 1, 6);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (5, 1, 2, 4);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (6, 2, 5, 5);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (7, 4, 10, 2);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (8, 4, 9, 3);
           insert into consumption_info (client_id, seller_id, fruit_id, quantity_purchased_fruit) values (9, 4, 8, 4);     

-- displaying the result from the second table

 select * from consumption_info;

-- the first query: 'How many tons worth of fruit does an average seller have?'
   create table first_query as(
    select seller_id, avg(fruit_weight)
    from seller_info
    group by seller_id
    order by seller_id asc);

select * from first_query;
 
-- the second query: 'How many sellers have at least one client who purchased their fruit?'
 select count(distinct seller_id) as number_of_sellers_who_purchased from consumption_info;
