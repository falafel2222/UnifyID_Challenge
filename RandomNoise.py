import randomdotorg
import wave
import struct

r = randomdotorg.RandomDotOrg('UnifyID')
print r.get_quota()

# 8kHz * 8bit * 3 = ~= 200,000 bits

framerate = 8000
numFrames = 3 * framerate


outfile = wave.open('noise.wav', 'w')

outfile.setnchannels(1)
outfile.setsampwidth(1)
outfile.setframerate(framerate)
outfile.setnframes(numFrames)


data = []
for i in range(numFrames/200):
	data += r.randrange(0, 2**8, amount=200)
for datum in data:
	outfile.writeframesraw(struct.pack('<B', datum))

outfile.writeframes('')
outfile.close()
