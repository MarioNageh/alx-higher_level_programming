-- ALL Cities
SELECT `id` , `name` from `cities` 
where `state_id` = (
    select `id` from `states` where `name` = "California"
)
ORDER BY id;