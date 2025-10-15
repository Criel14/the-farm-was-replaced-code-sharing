from common import check_and_water
from common import check_and_fertilize
from common import check_and_plant
from common import move_to_pos
from common import wait_for_all_drones

n = get_world_size()

# 种植一列
def plant_line():
	for i in range(n):
		if get_ground_type() == Grounds.Grassland:
			till()
		elif get_entity_type() != Entities.Sunflower:
			harvest()
		check_and_water()
		plant(Entities.Sunflower)
		move(North)

# 给无人机用：当前需要收集的花瓣数
cur_petal = 15
# 收割一列中花瓣数为cur_petal的
def check_harvest_line():
	for i in range(n):
		if get_entity_type() == Entities.Sunflower and measure() == cur_petal:
			# 等待收割：没成熟的施肥，减少等待时间
			if not can_harvest():
				check_and_fertilize()
			while not can_harvest():
				pass
			harvest()
		move(North)

# 种植一列 → 收集花瓣为15的...收集花瓣为7的
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
		
	# 开始
	while True:
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
		
		cur_petal = 15
		while cur_petal >= 7:
			# 生成无人机采摘
			move_to_pos(0, 0)
			drones = set()
			for i in range(n):
				drone = spawn_drone(check_harvest_line)
				if not drone:
					check_harvest_line()
				else:
					drones.add(drone)
				move(East)
			# 等待无人机
			wait_for_all_drones(drones)
			cur_petal -= 1
		
			