select count(*) FISH_COUNT
from fish_info a
join fish_name_info b
on b.FISH_TYPE = a.FISH_TYPE
where b.fish_name in ('BASS', 'SNAPPER')