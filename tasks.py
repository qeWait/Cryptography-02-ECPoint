from ECurve import ECurve, ECPoint
# За потребності можна зробити запит на ввід з клавіатури, але це тест, щоб ви могли зразу запустити

curve = ECurve(3, 4)
print(curve.EquationToString())
curve.PrintEquation()

baseGpoint = curve.BasePointGGet()
baseGpoint.PrintECPoint()

point1 = ECPoint(0, 2)
point1.PrintECPoint()
print(point1.ECPointToString(), "- точка яка належить еліптичній кривій" if point1.IsOnCurveCheck(curve) else "- точка яка не належить еліптичній кривій")

point2 = ECPoint(-1, 0)
point2.PrintECPoint()
print(point2.ECPointToString(), "- точка яка належить еліптичній кривій" if point2.IsOnCurveCheck(curve) else "- точка яка не належить еліптичній кривій")

point3 = curve.AddECPoints(point1, point2)
point3.PrintECPoint()
print(point3.ECPointToString(), "- точка яка належить еліптичній кривій" if point3.IsOnCurveCheck(curve) else "- точка яка не належить еліптичній кривій")

point4 = point3.DoubleECPoint(curve)
point4.PrintECPoint()
print(point4.ECPointToString(), "- точка яка належить еліптичній кривій" if point4.IsOnCurveCheck(curve) else "- точка яка не належить еліптичній кривій")

point5 = point3.ScalarMult(3)
point5.PrintECPoint()
print(point5.ECPointToString(), "- точка яка належить еліптичній кривій" if point5.IsOnCurveCheck(curve) else "- точка яка не належить еліптичній кривій")