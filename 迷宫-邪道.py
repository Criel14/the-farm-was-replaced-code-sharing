from common import move_to_pos

n = 5
set_world_size(n)
def drone_exec():
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			generate_maze()
		
def generate_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

if __name__ == "__main__":
	move_to_pos(0, 0)
	for i in range(n):
		for j in range(n):
			spawn_drone(drone_exec)
			if (get_pos_x(), get_pos_y()) == (n - 1, n - 1):
				generate_maze()
				drone_exec()
			move(North)
		move(East)