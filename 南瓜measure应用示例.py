from common import check_and_water
from common import move_to_pos
		
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	set_world_size(6)
	n = get_world_size()
	move_to_pos(0, 0)
	
	id_0 = 0
	while True:
		for i in range(n):
			for j in range(n):
				# 获得左下角南瓜的id
				if (i, j) == (0, 0) and get_entity_type() == Entities.Pumpkin:
					id_0 = measure()
				# 获得右上角南瓜的id
				elif (i, j) == (n - 1, n - 1) and get_entity_type() == Entities.Pumpkin:
					if measure() == id_0:
						harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)
				move(North)
			move(East)