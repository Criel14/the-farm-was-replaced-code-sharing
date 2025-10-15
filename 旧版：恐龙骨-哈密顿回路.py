from common import harvest_all
from common import till_all
from common import move_to_pos	
		
n = get_world_size()
size = n * n # positions数组长度

# 构造一个【哈密顿回路】的位置数组
def build_positions():
	positions = [] # positions[i] = [第i步应该在的x坐标, 第i步应该在的y坐标]
	x = -1
	y = 0
	# 最下边(南边)走一行: 从West到East
	while x < n - 1:
		x += 1
		positions.append([x, y])
	# 往北走一格
	y += 1
	positions.append([x, y])
	# 蛇形移动: 奇数往北，偶数往南，移动完往西走一格
	while True:
		# 奇数往北
		if x % 2 == 1:
			while y < n - 1:
				y += 1
				positions.append([x, y])
		# 偶数往南
		else:
			while y > 1:
				y -= 1
				positions.append([x, y])
		# 往西走一格
		if x - 1 >= 0:
			x -= 1
			positions.append([x, y])
		else:
			break
	return positions
		
# 在哈密顿回路中前进一步
# @return 返回是否移动成功
def next_step(positions, cur_index):
	cur_x, cur_y = get_pos_x(), get_pos_y()
	next_index = (cur_index + 1) % size
	next_x, next_y = positions[next_index][0], positions[next_index][1]
	# 判断方向
	if next_x - cur_x > 0:
		direction = East
	elif next_x - cur_x < 0: 
		direction = West
	elif next_y - cur_y > 0:
		direction = North
	elif next_y - cur_y < 0:
		direction = South
	# 移动(返回是否移动成功，即蛇是否已经占满整个农田)
	return move(direction)
	

# 贪吃蛇：如果边长为【偶数】，则直接走一个【哈密顿回路】即可
# 如果无人机试图移动到尾巴上，move()将失败并返回False
if __name__ == "__main__" and n % 2 == 0:
	clear()
	move_to_pos(0, 0)
	positions = build_positions()
	index = 0
	change_hat(Hats.Straw_Hat)
	change_hat(Hats.Dinosaur_Hat)
	
	while True:
		# 如果蛇已经占满整个农田，则清空
		if not next_step(positions, index):
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
		# 成功则前进一步
		else:
			index = (index + 1) % size