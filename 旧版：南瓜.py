from common import check_and_water
from common import move_to_pos
		
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	set_world_size(10)
	n = get_world_size()
	move_to_pos(0, 0)
	
	while True:
		# 生成需要种植的位置：初始为所有位置
		to_plant_positions = []
		for i in range(n):
			for j in range(n):
				to_plant_positions.append([i, j])
		# 遍历to_plant_positions
		while True:
			# 记录下一轮未成熟的位置
			next_round = []
			# 如果不成熟就尝试播种，成熟了则从to_plant_positions中删除
			for pos in to_plant_positions:
				move_to_pos(pos[0], pos[1])
				if get_ground_type() == Grounds.Grassland:
					till()
				if get_entity_type() != Entities.Pumpkin:
					harvest()
				if not can_harvest():
					# check_and_water()
					plant(Entities.Pumpkin)
					next_round.append(pos)
			# 赋值下一轮
			to_plant_positions = next_round
			# 全部被删除(全部成熟)则收获，并结束循环
			if len(to_plant_positions) == 0:
				harvest()
				break