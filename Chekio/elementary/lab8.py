"""
left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"
kortezh -> строку через запятую
right -> left
""" 
import re

def left_join(fofofo):
#	b = []
	for item in fofofo:
		 nitem = re.sub("right", "left", item)
		 b.append(nitem)
	string = ",".join(b)
	return string
print (left_join(("left", "right", "left", "stop")))
print (left_join(("bright aright", "ok"))) 
print (left_join(("brightness wright",)))
print (left_join(("enough", "jokes"))) 