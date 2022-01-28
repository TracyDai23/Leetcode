CREATE TABLE customer (
  customer_id INT,
  genre_interests text[]
);
INSERT INTO customer  VALUES (1, array['music','coding']);
INSERT INTO customer VALUES (2, array['coding','art']);
INSERT INTO customer VALUES (3, array['coding','art']);
INSERT INTO customer VALUES (4, array['a','b']);


CREATE TABLE sales (
  sales_id INT,
  customer_id INT,
  book_id INT,
  total_sales decimal
);

INSERT INTO sales  VALUES (1,1,1, 20.0);
INSERT INTO sales  VALUES (2,1,2, 15.5);
INSERT INTO sales  VALUES (3,1,1, 20.0);
INSERT INTO sales  VALUES (4,2,1, 20.0);
INSERT INTO sales  VALUES (5,3,3, 20.0);
INSERT INTO sales  VALUES (5,4,1, 20.0);

CREATE TABLE book (
  book_id INT,
  genre text,
  book_name text
);

INSERT INTO book  VALUES (1,'coding','SQL guide');
INSERT INTO book  VALUES (2,'art','oil paiting');
INSERT INTO book  VALUES (3,'music','bei');
INSERT INTO book  VALUES (4,'coding','JAVA guide');



-- Query portion
with c as(
SELECT customer_id, unnest(genre_interests) as genre
from customer
)

select count(distinct case when c.genre is not null then s.customer_id end) as genre_bought_customer,
count(distinct s.customer_id) as total_customer
from sales s
inner join book b on s.book_id = b.book_id
left join c 
on s.customer_id = c. customer_id
and c.genre = b.genre
