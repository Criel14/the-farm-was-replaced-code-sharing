from common import check_and_water
from common import check_and_fertilize
from common import check_and_plant
from common import move_to_pos
from common import wait_for_all_drones

n = get_world_size()


def plant_line():
	while True:
		# 种植一列
		for i in range(n):
			if get_ground_type() == Grounds.Grassland:
				till()
			elif get_entity_type() != Entities.Sunflower:
				harvest()
			else:
				harvest()
			check_and_water()
			plant(Entities.Sunflower)
			move(North)

# 直接种，不知道为什么工作太久游戏就会卡，然后执行速度变慢
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	move_to_pos(0, 0)
	# 生成无人机种植
	drones = set()
	for i in range(n):
		drone = spawn_drone(plant_line)
		if not drone:
			plant_line()
		else:
			drones.add(drone)
		move(East)
			