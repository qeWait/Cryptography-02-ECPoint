import ECPoint as ECP

point1 = ECP.ECPoint(0, 2)
point1.PrintECPoint()
print(point1.ECPointToString(), "- точка яка належить еліптичній кривій" if point1.IsOnCurveCheck() else "- точка яка не належить еліптичній кривій")

point2 = ECP.ECPoint(-1, 0)
point2.PrintECPoint()
print(point2.ECPointToString(), "- точка яка належить еліптичній кривій" if point2.IsOnCurveCheck() else "- точка яка не належить еліптичній кривій")

point3 = ECP.AddECPoints(point1, point2)
point3.PrintECPoint()
print(point3.ECPointToString(), "- точка яка належить еліптичній кривій" if point3.IsOnCurveCheck() else "- точка яка не належить еліптичній кривій")

point4 = point3.DoubleECPoint()
point4.PrintECPoint()
print(point4.ECPointToString(), "- точка яка належить еліптичній кривій" if point4.IsOnCurveCheck() else "- точка яка не належить еліптичній кривій")

point5 = point3.ScalarMult(3)
point5.PrintECPoint()
print(point5.ECPointToString(), "- точка яка належить еліптичній кривій" if point5.IsOnCurveCheck() else "- точка яка не належить еліптичній кривій")