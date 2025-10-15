from common import harvest_and_till_all
from common import move_to_pos
from common import check_and_water
from common import check_and_plant

plants = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
# 随机获取一种植物
def get_random_plant():
	index = random() * len(plants) // 1  
	return plants[index]

if __name__ == "__main__":
	change_hat(Hats.Straw_Hat)
	harvest_and_till_all()
	n = get_world_size()
	move_to_pos(0, 0)
	
	# 伴生植物位置和种类
	pos_entity = {}
	while True:
		# 边种边统计伴生植物的位置
		for i in range(n):
			for j in range(n):
				# 收割上一轮的作物
				if can_harvest():
					harvest()
				# 如果当前位置是伴生植物的位置，则种植伴生植物，否则种植随机植物
				cur_pos = (get_pos_x(), get_pos_y()) 
				if cur_pos in pos_entity:
					plant(pos_entity[cur_pos])
				else:
					plant(get_random_plant())
				check_and_water()
				# 获取当前作物的伴生作物信息
				pl, (x, y) = get_companion()
				pos_entity[(x, y)] = pl
				move(North)
			move(East)