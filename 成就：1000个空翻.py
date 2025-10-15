def flip():
	while True:
		do_a_flip()
		
for i in range(32):
	if not spawn_drone(flip):
		flip()
	move(East)