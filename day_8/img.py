from collections import defaultdict
with open("in.txt", "r") as f:
    test = [int(x) for x in f.read()]
# test = [1,2,0,4,5,6,1,1,1,0,1,2,1,1,1,1,2,2]
width,height = 25,6
layerL,layerC,layers = ((len(test) // (width * height))), 1, defaultdict()
while layerC <= layerL:
    layers[layerC] = [0,0,0]
    for i in range(height):
        for j in range(width):
            temp = test.pop(0)
            if temp is 0: layers[layerC ][0] +=  1
            elif temp is 1: layers[layerC][1] += 1
            elif temp is 2: layers[layerC][2] += 1  
    layerC += 1

mix = layerL
mixV = layers[layerL][0]
for key, x in layers.iteritems():
    if x[0] <= mixV:
        mix = key
        mixV = x[0]
print layers[mix][1] * layers[mix][2]