# python
# coding:utf-8

from collections import namedtuple
from decimal import Decimal

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
for each in out:
	print(str(each.x) + " " + str(each.y) + " " + str(each.z))


			