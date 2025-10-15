n = 9
set_world_size(n)
set_execution_speed(4)

def next_step():
	(x, y) = (get_pos_x(), get_pos_y())
	if y == 0 and x > 0:
		move(West)
	elif x == 0 and y < n - 1:
		move(North)
	elif y == n - 1 and x < n - 1:
		move(East)
	else:
		move(South)

# 无人机执行逻辑
def drone_exec():
	while True:
		next_step()
		
# 主无人机
if __name__ == "__main__":
	change_hat(Hats.Golden_Pumpkin_Hat)
	while True:
		spawn_drone(drone_exec)
		next_step()
		