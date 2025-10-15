# 全部耕地
def till_all():
	n = get_world_size()
	for i in range(n):
		for j in range(n):
			if not get_ground_type() == Grounds.Soil:
				till()
			move(North)
		move(East)
	
# 全部收获
def harvest_all():
	n = get_world_size()
	while True:
		num = 0 # 收获数量
		for i in range(n):
			for j in range(n):
				if can_harvest():
					num += 1
					harvest()
				move(North)
			move(East)
		# 如果没有收获，说明已全部清除
		if num == 0:
			move_to_pos(0, 0)
			break
			
# 全部收获和耕地
def harvest_and_till_all():
	n = get_world_size()
	for i in range(n):
		for j in range(n):
			harvest()
			if not get_ground_type() == Grounds.Soil:
				till()
			move(North)
		move(East)

# 全部浇水
def water_all():
	n = get_world_size()
	for i in range(n):
		for j in range(n):
			check_and_water()
			move(North)
		move(East)
		
# 检查并浇水
def check_and_water():
	while num_items(Items.Water) > 0 and get_water() <= 0.75:
		use_item(Items.Water)
		
# 检查并施肥
def check_and_fertilize():
	if num_items(Items.Fertilizer) > 0 and not can_harvest():
		use_item(Items.Fertilizer)
		return True
	return False
		
# 检查并收割和种植
def check_and_plant(entity):
	if can_harvest():
		harvest()
	plant(entity)
	
# 移动到指定坐标(环绕)
def move_to_pos(x_target, y_target):
	n = get_world_size()
	curX = get_pos_x()
	curY = get_pos_y()

	# 计算 x 方向的距离和方向（最短路径）
	dx = (x_target - curX) % n
	# dx 表示向“正向”（East）走 dx 步（如果 dx ≤ n/2），否则向 West 走 n - dx 步
	if dx <= n // 2:
		steps_x = dx
		dirX = East
	else:
		steps_x = n - dx
		dirX = West

	# 计算 y 方向的距离和方向
	dy = (y_target - curY) % n
	if dy <= n // 2:
		steps_y = dy
		dirY = North
	else:
		steps_y = n - dy
		dirY = South

	# 交错移动
	while steps_x > 0 or steps_y > 0:
		# 优先移动差距较大的方向（剩余步数更多的方向）
		if steps_x >= steps_y and steps_x > 0:
			move(dirX)
			steps_x -= 1
		elif steps_y > 0:
			move(dirY)
			steps_y -= 1

	
# 等待其他所有无人机完成
def wait_for_all_drones(drones_set):
	while len(drones_set) > 0:
		removed_drones = []
		for drone in drones_set:
			if has_finished(drone):
				removed_drones.append(drone)
		for removed_drone in removed_drones:
			drones_set.remove(removed_drone)
		
		
def till_line():
	n = get_world_size()
	for i in range(n):
		if get_ground_type() == Grounds.Grassland:
			till()
		move(North)
	
def till_all_lines():
	n = get_world_size()
	move_to_pos(0, 0) 
	for i in range(n):
		if not spawn_drone(till_line):
			till_line()
		move(East)
		
					

		

	
	
	
				
	