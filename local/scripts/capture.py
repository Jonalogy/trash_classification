from time import time
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

index = [ '', 'paper', 'plastic', 'metal', 'glass', 'other' ]

#categories
# 1 - Paper
# 2 - Plastic
# 3 - Metal
# 4 - Glass
# 5 - Other

while True:
	inp = int(input(''))
	material = index[inp]

	counter = 0
	with open(f'../images/{material}/.counter.txt', 'r') as f:
		for line in f:
			counter = int(line) + 1

	with open(f'../images/{material}/.counter.txt', 'w') as f:
		f.write(str(counter))

	path = f'../images/{material}/{material}{counter}.jpg'
	camera.capture(path)

#images can be scp'ed for later training
