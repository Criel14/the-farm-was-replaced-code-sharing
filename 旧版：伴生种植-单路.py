from common import harvest_and_till_all
from common import move_to_pos
from common import check_and_water
from common import check_and_plant
from common import check_and_fertilize

plants = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
# 随机获取一种植物
def get_random_plant():
	index = random() * len(plants) // 1  
	return plants[index]

if __name__ == "__main__":
	set_world_size(7)
	change_hat(Hats.Straw_Hat)
	harvest_and_till_all()
	n = get_world_size()
	move_to_pos(0, 0)

	# 种植顺序，positions[i]的半生植物位置是positions[i + 1】
	positions = [(get_pos_x(), get_pos_y())]
	pl = get_random_plant()
	while True:
		old_pl = pl
		plant(old_pl)
		if old_pl == Entities.Tree:
			check_and_fertilize()
		check_and_water()
		pl, (x, y) = get_companion()
		# 如果伴生植物位置存在于positions中，说明出现了环，则重新种植
		replant_count = 0
		while (x, y) in positions and replant_count < 4:
			harvest()
			plant(old_pl)
			if old_pl == Entities.Tree:
				check_and_fertilize()
			check_and_water()
			pl, (x, y) = get_companion()
			replant_count += 1
		# 重种次数过多或种满，则收获
		if replant_count >= 4 or len(positions) >= n * n :
			# print(len(positions))
			for pos in positions:
				move_to_pos(pos[0], pos[1])
				while not can_harvest():
					pass
				harvest()
			# 清空列表
			positions = [(get_pos_x(), get_pos_y())]
		else:
			positions.append((x, y))
			move_to_pos(x, y)
	