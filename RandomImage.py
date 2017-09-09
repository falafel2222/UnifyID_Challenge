# import randomdotorg
import random
from PIL import Image
import numpy as np

# r = randomdotorg.RandomDotOrg('UnifyID')
# print r.get_quota()

# 128*128*8*3 ~= 400,000 bits

imgSize = 128

imgData = np.zeros((imgSize, imgSize, 3), dtype=np.uint8)
for i in range(imgSize):
	for j in range(imgSize):
		for color in range(3):
			imgData[i][j][color] = random.randrange(0, 255)


noisyImg = Image.fromarray(imgData, 'RGB')

noisyImg.save('noise.png')
noisyImg.show()