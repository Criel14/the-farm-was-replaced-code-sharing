from common import harvest_and_till_all
from common import check_and_fertilize
from common import check_and_water
from common import move_to_pos	

def plant_one():
	(start_x, start_y) = (get_pos_x(), get_pos_y())
	while True:
		move_to_pos(start_x, start_y)
		if get_ground_type() == Grounds.Grassland:
			till()
		while get_entity_type() == Entities.Carrot and not can_harvest():
			pass
		harvest()
		plant(Entities.Carrot)
		check_and_water()
		check_and_fertilize()
		# 伴生植物
		if get_companion() != None:
			pl, (x, y) = get_companion()
			if x != start_x:
				move_to_pos(x, y)
				if get_ground_type() == Grounds.Grassland:
					till()
				harvest()
				plant(pl)

if __name__ == "__main__":
	clear()
	n = get_world_size()
	
	positions = [[0, 0], [4, 3], [8, 0], [12, 3], [16, 0], [20, 3], [24, 0], [28, 3], 
				 [0, 6], [4, 9], [8, 6], [12, 9], [16, 6], [20, 9], [24, 6], [28, 9],
				 [0, 12], [4, 15], [8, 12], [12, 15], [16, 12], [20, 15], [24, 12], [28, 15],
				 [0, 18], [4, 21], [8, 18], [12, 21], [16, 18], [20, 21], [24, 18], [28, 21]]
	
	for pos in positions:
		move_to_pos(pos[0], pos[1])
		if not spawn_drone(plant_one):
			plant_one()