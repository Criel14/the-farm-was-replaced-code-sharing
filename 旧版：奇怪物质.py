from common import harvest_and_till_all
from common import check_and_fertilize
from common import check_and_water
from common import move_to_pos	
		
if __name__ == "__main__":
	set_world_size(3)
	change_hat(Hats.Straw_Hat)
	harvest_and_till_all()
	n = get_world_size()
	while True:
		move_to_pos(0, 0)
		harvest()
		check_and_water()
		plant(Entities.Tree)
		check_and_fertilize()
		# 伴生植物
		pl, (x, y) = get_companion()
		move_to_pos(x, y)
		harvest()
		plant(pl)