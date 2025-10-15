from common import harvest_and_till_all
from common import check_and_water
from common import move_to_pos	
		
dirs = [East, South, West, North]
dirs_index = {East: 0, South: 1, West: 2, North: 3}

def get_right_dir(dir):
	return dirs[(dirs_index[dir] + 1) % 4]

def get_left_dir(dir):
	return dirs[(dirs_index[dir] - 1) % 4]

# 每次生成新迷宫，然后dfs找到宝藏
if __name__ == "__main__":
	# set_world_size(10)
	clear()
	n = get_world_size()
	move_to_pos(0, 0)

	while True:
		# 生成迷宫
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		# 沿着墙走
		dir = North
		while True:
			# 能往右走就往右
			if can_move(get_right_dir(dir)):
				dir = get_right_dir(dir)
				move(dir)
			else:
				dir = get_left_dir(dir)
			if get_entity_type() == Entities.Treasure:
				harvest()
				break