from common import harvest_and_till_all
from common import check_and_water
from common import check_and_fertilize
from common import check_and_plant
from common import move_to_pos

# set_world_size()
n = get_world_size()

# 计数排序
def sort_powers(powers):
	# 创建计数数组，power范围是7-15，共9个可能值
	count = []  # 索引0对应power7，索引8对应power15
	for i in range(9):
		count.append([])
	
	# 统计每个power值对应的坐标
	for i in range(len(powers)):
		item = powers[i]
		x = item[0]
		y = item[1]
		power = item[2]
		index = power - 7  # 将power值映射到数组索引
		count[index].append([x, y])
	
	# 按power降序重新构建powers数组
	sorted_powers = []
	# 从高到低遍历（power 15到7）
	for i in range(8, -1, -1):
		# 将当前power级别的所有坐标添加到结果中
		for j in range(len(count[i])):
			sorted_powers.append(count[i][j])
	
	return sorted_powers

# 种植-排序-降序采摘
if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
		
	# 开始
	while True:
		# powers[i] = [x坐标, y坐标, power值】
		powers = []
		# 种植，同时获取每株向日葵的能量
		for i in range(n):
			for j in range(n):
				if get_ground_type() == Grounds.Grassland:
					till()
				elif get_entity_type() != Entities.Sunflower:				
					plant(Entities.Sunflower)
					#check_and_water()
				powers.append([get_pos_x(), get_pos_y(), measure()])
				move(North)
			move(East)
		# 按照能量降序排序
		sorted_powers = sort_powers(powers)
		# 遍历按照能量从大到小收割
		for power in sorted_powers:
			x = power[0]
			y = power[1]
			move_to_pos(x, y)
			# 等待收割：没成熟的施肥，减少等待时间
			if not can_harvest():
				check_and_fertilize()
			while not can_harvest():
				pass
			harvest()