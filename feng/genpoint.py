# python
# coding:utf-8

from collections import namedtuple
from decimal import Decimal
from math import sqrt

Point = namedtuple('Point', ['x', 'y', 'z'])

A = Point(Decimal("0.0"), Decimal("0.5"), Decimal("0.0"))
B = Point(Decimal("0.5"), Decimal("0.5"), Decimal("0.5"))
C = Point(Decimal("0.5"), Decimal("0.0"), Decimal("0.0"))

points = [A, B, C]
out = []

step = 100

# begin
for i in range(0, len(points)-1):
	P1 = points[i] 
	P2 = points[i+1]
	out.append(P1)
	P = P1

	for j in range(1,step):
		if( P2.x != P1.x ):
			P = P._replace( x = P.x + ( P2.x - P1.x ) / step )
		if( P2.y != P1.y ):
			P = P._replace( y = P.y + ( P2.y - P1.y ) / step )
		if( P2.z != P1.z ):
			P = P._replace( z = P.z + ( P2.z - P1.z ) / step )
		out.append(P)

out.append(points[len(points)-1])


# out
dist = Decimal("0.0")
index = 1
for each in out:
	print(str(index) + " " + str(round(dist,7)) + " " + \
		str(round(each.x,7)) + " " + str(round(each.y,7)) + " " + str(round(each.z,7)))

	if( index != len(out) ):
		dist += Decimal( sqrt( + (out[index].x-out[index-1].x)**2 + \
			(out[index].y-out[index-1].y)**2 + (out[index].z-out[index-1].z)**2 ) )
		index += 1
