from common import harvest_all
from common import till_all
from common import move_to_pos	
		
n = get_world_size()

# 在哈密顿回路中前进一步
# @return 返回是否移动成功
def next_step():
	cur_x, cur_y = get_pos_x(), get_pos_y()
	if cur_y == 0 and cur_x != n - 1:
		return move(East)
	elif cur_y == 1 and cur_x != 0 and cur_x % 2 == 0:
		return move(West)
	elif cur_y == n - 1 and cur_x % 2 == 1:
		return move(West)
	elif cur_x % 2 == 0:
		return move(South)
	elif cur_x % 2 == 1:
		return move(North)
		
# 贪吃蛇：如果边长为【偶数】，则直接走一个【哈密顿回路】即可
# 如果无人机试图移动到尾巴上，move()将失败并返回False
if __name__ == "__main__" and n % 2 == 0:
	clear()
	move_to_pos(0, 0)
	change_hat(Hats.Straw_Hat)
	change_hat(Hats.Dinosaur_Hat)
	while True:
		# 如果蛇已经占满整个农田，则清空，成功则前进一步
		if not next_step():
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)