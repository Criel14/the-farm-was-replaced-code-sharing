from common import check_and_water
from common import move_to_pos
from common import wait_for_all_drones
from common import till_all_lines

n = get_world_size()
	
# 无人机执行逻辑
def drone_exec():
	x = get_pos_x()
	while True:
		plant_line()
		# 等待下方南瓜被收割，再开始新的一轮
		move_to_pos(x, 0)
		while get_entity_type() == Entities.Pumpkin:
			pass

# 种植直到这一行全部成熟
def plant_line():
	to_plant_positions = []
	for i in range(n):
		to_plant_positions.append((get_pos_x(), i))
	while len(to_plant_positions):
		next_round = []
		for pos in to_plant_positions:
			move_to_pos(pos[0], pos[1])
			if get_ground_type() == Grounds.Grassland:
				till()
			if get_entity_type() != Entities.Pumpkin:
				harvest()
			if not can_harvest():
				next_round.append(pos)
				check_and_water()
				plant(Entities.Pumpkin)
		to_plant_positions = next_round

if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	till_all_lines()
	
	move_to_pos(0, 0)
	# 无人机种植前31列
	for i in range(n):
		spawn_drone(drone_exec)
		move(East)
	while True:
		# 自己种植最后一列
		move_to_pos(n - 1, 0)
		plant_line()
		# 检查南瓜是否全部合并
		while True:
			move_to_pos(0, 0)
			if get_entity_type() == Entities.Pumpkin:
				id = measure()
				move_to_pos(n - 1, n - 1)
				if id == measure():
					harvest()
					break