'''1. 

    select p.post_id, p.title, p.created_at, count(comment_id) as comment_count
        from post p
        left join comments c on p.post_id = c.post_id
        group by p.post_id, p.title, p.created_at
        order by p.created_at desc limit 5;

2. 

    select u.user_id, u.name, u.email
        from join posts p on u.user.id = p.user_id
        where p.post_id is null
'''

