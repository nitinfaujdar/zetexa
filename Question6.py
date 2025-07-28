Question 5:-

select u.user_id, u.name, u.email 
    from users u join(
        select user_id from orders group by user_id having count(*) > 5 and sum(total_amount) > 10000
        ) o on u.user_id = o.user_id