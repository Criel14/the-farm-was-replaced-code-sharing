from common import harvest_all
from common import till_all
from common import move_to_pos
		
n = get_world_size()
size = n * n # positions数组长度

# 移动到指定坐标（不环绕）
def move_to(target_x, target_y):
	cur_x, cur_y = get_pos_x(), get_pos_y()
	step_x = abs(target_x - cur_x)
	step_y = abs(target_y - cur_y)
	
	if target_x > cur_x:
		dir_x = East
	else:
		dir_x = West
	if target_y > cur_y:
		dir_y = North
	else:
		dir_y = South
	
	# 先x
	if not can_move(dir_y):
		for i in range(step_x):
			if not move(dir_x):
				return False
		for i in range(step_y):
			if not move(dir_y):
				return False
	# 先y
	else:
		for i in range(step_y):
			if not move(dir_y):
				return False
		for i in range(step_x):
			if not move(dir_x):
				return False
	return True

if __name__ == "__main__":
	clear()
	move_to_pos(0, 0)
	index = 0
	change_hat(Hats.Straw_Hat)
	change_hat(Hats.Dinosaur_Hat)
	
	while True:
		(next_x, next_y) = measure()
		if not move_to(next_x, next_y):
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
		