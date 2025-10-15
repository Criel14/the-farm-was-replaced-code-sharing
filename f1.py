clear()
n = 8
set_world_size(n)
num = 0

# 无人机执行逻辑
def drone_exec():
	print(num)
	return num * num
	
# 主无人机
if __name__ == "__main__":
	while True:
		# 无人机返回结果汇总
		result = [] 
		# 无人机集合
		drones = set() 
		for i in range(n):
			drone = spawn_drone(drone_exec)
			# 无人机用完，则主无人机执行
			if not drone:
				result = drone_exec()
			else:
				drones.add(drone)
			num += 1
			move(North)
			
		# 汇总无人机返回结果
		for drone in drones:
			res = wait_for(drone)
			result.append(res)
		print(result)
		
		# sleep
		for i in range(20000):
			pass
	
	
