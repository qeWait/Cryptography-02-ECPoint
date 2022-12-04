import ECPoint as ECP

point1 = ECP.ECPoint(0, 2)
point1.PrintECPoint()

point2 = ECP.ECPoint(-1, 0)
point2.PrintECPoint()

point3 = ECP.AddECPoints(point1, point2)
point3.PrintECPoint()

point4 = point3.DoubleECPoint()
point4.PrintECPoint()

point5 = point3.ScalarMult(3)
point5.PrintECPoint()

print(point1.IsOnCurveCheck(), point2.IsOnCurveCheck(), point3.IsOnCurveCheck(), point4.IsOnCurveCheck(), point5.IsOnCurveCheck())