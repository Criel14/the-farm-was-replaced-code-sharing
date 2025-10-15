from common import move_to_pos	
from common import wait_for_all_drones
		
n = get_world_size()

# 冒泡排序某一方向
# @param 起始位置、方向(东或北)
def sort_line(start_x, start_y, direction):
	move_to_pos(start_x, start_y)
	for i in range(n):
		# 复位
		move_to_pos(start_x, start_y)
		swap_count = 0
		for j in range(n - 1 - i):
			if measure() > measure(direction):
				swap_count += 1
				swap(direction) 
			move(direction)
		if swap_count == 0:
			break

# 新无人机：种植一行，排序一行
def drone_plant_and_sort_row():
	(start_x, start_y) = (get_pos_x(), get_pos_y())
	for i in range(n):
		if get_ground_type() == Grounds.Grassland:
			till()
		harvest()
		plant(Entities.Cactus)
		move(East)
	sort_line(start_x, start_y, East)

# 新无人机：排序一列
def dronw_sort_line():
	sort_line(get_pos_x(), get_pos_y(), North)
	
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	
	while True:
		move_to_pos(0, 0)
		# 每行生成一架无人机去种植
		drones = set()
		for i in range(n):
			drone = spawn_drone(drone_plant_and_sort_row)
			if not drone:
				drone_plant_and_sort_row()
			else:
				drones.add(drone)
			move(North)

		# 等待其他无人机完成
		move_to_pos(0, 0)
		wait_for_all_drones(drones)
		
		# 再生成无人机去排序列
		for i in range(n):
			drone = spawn_drone(dronw_sort_line)
			if not drone:
				dronw_sort_line()
			else:
				drones.add(drone)
			move(East)
		
		# 等待其他无人机完成后收割
		wait_for_all_drones(drones)
		harvest()