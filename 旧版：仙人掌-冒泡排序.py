from common import harvest_and_till_all
from common import check_and_water
from common import check_and_plant
from common import move_to_pos	
		
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
			
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	harvest_and_till_all()

	while True:
		# 种植
		for i in range(n):
			for j in range(n):
				plant(Entities.Cactus)
				move(North)
			move(East)
		# 对每一行冒泡排序
		for i in range(n):
			sort_line(i, 0, North)
		# 对每一列冒泡排序
		for i in range(n):
			sort_line(0, i, East)
		# 收获
		harvest()