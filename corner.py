#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

if len(sys.argv) < 2:
	print "Inform image path"
	exit()

img = mpimg.imread(sys.argv[1])

threshold = 0.2

points = []
for u in range(1,img.shape[0]-1):
	for v in range(1,img.shape[1]-1):
		if sum(img[u,v])/img.shape[2] < 0.5 :
			n = 0
			s = sum(img[u][v])
			for i in range(3):
				for j in range(3):
					sn = sum(img[u+(i-1)][v+(j-1)])
					if sn <= s+threshold and sn >= s-threshold :
						n += 1
			if n == 4 :
				points.append([u,v])

plt.axis('off')
plt.imshow(img)
plt.scatter(x=[w[1] for w in points], y=[h[0] for h in points], c='r', s=20)
plt.show()
