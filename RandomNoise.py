# import randomdotorg
import random
import wave
import struct

# r = randomdotorg.RandomDotOrg('UnifyID')
# print r.get_quota()

# 8kHz * 16bit * 3 = ~= 400,000 bits

framerate = 8000
numFrames = 3 * framerate


outfile = wave.open('noise.wav', 'w')

outfile.setnchannels(1)
outfile.setsampwidth(1)
outfile.setframerate(framerate)
outfile.setnframes(numFrames)

for i in range(numFrames):
	data = random.randrange(0, 2**8)
	outfile.writeframesraw(struct.pack('<B', data))

outfile.writeframes('')
outfile.close()
