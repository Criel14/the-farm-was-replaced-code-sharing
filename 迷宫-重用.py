from common import harvest_and_till_all
from common import check_and_water
from common import move_to_pos	
		
set_world_size(16)
n = get_world_size()		

# 循环队列
_buf = None        # 用于存放队列元素的列表
_front = 0         # 指向队头元素的下标
_rear = 0          # 指向下一个插入位置的下标
_size = 0          # 当前队列中元素个数
_capacity = 0      # 队列容量

# 初始化队列
def init_queue(capacity):
	global _buf
	global _front
	global _rear
	global _size
	global _capacity
	_buf = []
	for i in range(capacity):
		_buf.append(None)
	_capacity = capacity
	_front = 0
	_rear = 0
	_size = 0

# 入队
def q_add(x):
	global _buf
	global _front
	global _rear
	global _size
	global _capacity
	_buf[_rear] = x
	_rear = (_rear + 1) % _capacity
	_size += 1

# 出队
def q_poll():
	global _buf
	global _front
	global _rear
	global _size
	global _capacity
	x = _buf[_front]
	_buf[_front] = None
	_front = (_front + 1) % _capacity
	_size -= 1
	return x

# 获取队列当前大小
def q_size():
	global _size
	return _size

# 记录各个方向	的反方向
negative_directions = {
	East: West,
	West: East,
	South: North,
	North: South
}

# 宝箱位置
(next_x, next_y) = (-1, -1)

dirs_pos = {
	East: (1, 0),
	West: (-1, 0),
	North: (0, 1),
	South: (0, -1)
}

# 绘制邻接表
def dfs_draw(visited, neighbors):
	# 记录移动前的位置
	cur_pos = (get_pos_x(), get_pos_y())
	# 遍历移动
	for dir in negative_directions:			
		# 如果能移动（没有墙）
		if can_move(dir):
			moved_x = (cur_pos[0] + dirs_pos[dir][0]) % n
			moved_y = (cur_pos[1] + dirs_pos[dir][1]) % n
			moved_pos = (moved_x, moved_y)
			# 能移动但已经访问过
			if moved_pos in visited:
				# 更新邻接表
				if cur_pos not in neighbors:
					neighbors[cur_pos] = set()
				neighbors[cur_pos].add(moved_pos)
				if moved_pos not in neighbors:
					neighbors[moved_pos] = set()
				neighbors[moved_pos].add(cur_pos)
			# 未访问过
			else:
				move(dir)
				visited.append(moved_pos)
				# 递归
				dfs_draw(visited, neighbors)
				# 移动后回溯
				move(negative_directions[dir])
				
# bfs搜索，用循环队列O(1)出入队
def bfs_find(neighbors, cur_x, cur_y, target_x, target_y):
	visited = set()
	init_queue(n * n + 1)
	q_add((cur_x, cur_y))
	visited.add((cur_x, cur_y))
	# 记录前驱节点（用 dict 存：child_pos → parent_pos）
	pre_step = {}

	found = False
	while q_size() > 0:
		(x, y) = q_poll()
		if (x, y) == (target_x, target_y):
			found = True
			break
		for pos in neighbors[(x, y)]:
			if pos not in visited:
				visited.add(pos)
				q_add(pos)
				pre_step[pos] = (x, y)

	if not found:
		# 没找到路径
		return []

	# 回溯构造路径（从目标到起点）
	path = [(target_x, target_y)]
	cur = (target_x, target_y)
	while cur != (cur_x, cur_y):
		cur = pre_step[cur]
		path.append(cur)

	# 反转 path 列表
	rev = []
	for i in range(len(path) - 1, -1, -1):  # 从最后一个到第 0 个
		rev.append(path[i])
	return rev

def move_one_step(pos):
	if pos[0] > get_pos_x():
		move(East)
	elif pos[0] < get_pos_x():
		move(West)
	elif pos[1] > get_pos_y():
		move(North)
	elif pos[1] < get_pos_y():
		move(South)

# 先不考虑：每次宝藏移动时，迷宫中可能会随机移除一堵墙。重复使用的迷宫可以包含循环；
# 因为是移除墙，所以我们当作是不变就可以了，一样能找到路径，只不过不是当前最短路径
if __name__ == "__main__":

	while True:
		clear()
		(next_x, next_y) = (-1, -1)
		move_to_pos(0, 0)
		# 生成迷宫
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		next_x, next_y = measure()
		
		rebuild_count = 301
		# 重新绘制的收益越来越小，所以延长重绘间隔
		redraw_rounds = set((0, 58))
		for i in range(rebuild_count):
			# 每隔一定次数绘制一次表格（第0次会先绘制一次）
			if i in redraw_rounds:
				# 访问数组：数组元素是元组
				visited = [(get_pos_x(), get_pos_y())]
				# 邻接表<(x, y), set<(x, y)>>
				neighbors = {}
				# dfs绘制邻接表，并找到宝箱的初始位置
				dfs_draw(visited, neighbors)
			
			# 搜索从起点到终点的路径
			res_path = bfs_find(neighbors, get_pos_x(), get_pos_y(), next_x, next_y)
			
			# 沿着路径走到宝箱的位置
			for pos in res_path:
				move_one_step(pos)
							
			if i < rebuild_count - 1:
				# 重用迷宫
				use_item(Items.Weird_Substance, substance)
				# 测量下一个宝藏的位置
				next_x, next_y = measure()
			else:
				# 最后一次则收割
				harvest()