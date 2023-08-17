-- Cities By Join
SELECT `ci`.`id`, `ci`.`name`, `s`.`name`
FROM `cities` AS `ci`
INNER JOIN `states` AS `s` ON `ci`.`state_id` = `s`.`id`
ORDER BY `ci`.`id`;
