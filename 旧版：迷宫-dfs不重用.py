from common import harvest_and_till_all
from common import check_and_water
from common import move_to_pos	
		
# 记录各个方向	的反方向
negative_directions = {
	East: West,
	West: East,
	North: South,
	South: North
}

# 按照宝箱位置和当前位置，靠近的方向优先
def get_sorted_dirs():
	cur_x, cur_y = get_pos_x(), get_pos_y()
	target_x, target_y = measure()
	if target_x > cur_x:
		dir_x = East
	else:
		dir_x = West
	if target_y > cur_y:
		dir_y = North
	else:
		dir_y = South
	if abs(target_x - cur_x) < abs(target_y - cur_y):
		dirs = [dir_x, dir_y, negative_directions[dir_x], negative_directions[dir_y]]
	else:
		dirs = [dir_y, dir_x, negative_directions[dir_y], negative_directions[dir_x]]
	return dirs
	

# 返回是否已经找到宝箱
def dfs(visited):
	# 如果当前位置下方是宝藏，则收获
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	# 遍历4个方向
	dirs = get_sorted_dirs()
	for dir in dirs:
		# 移动并递归
		if move(dir):
			cur_pos = (get_pos_x(), get_pos_y())
			# 没被访问过则访问
			if cur_pos not in visited:
				visited.append(cur_pos)
				if dfs(visited):
					return True
			# 移动后回溯
			move(negative_directions[dir])
	# 没找到则返回False
	return False
		
# 地图大小太大会栈溢出
# 每次生成新迷宫，然后dfs找到宝藏
if __name__ == "__main__":
	# set_world_size(10)
	n = get_world_size()
	move_to_pos(0, 0)

	while True:
		# 生成迷宫
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		# 访问数组：数组元素是元组
		visited = [(get_pos_x(), get_pos_y())]
		# dfs
		dfs(visited)
		
		
		