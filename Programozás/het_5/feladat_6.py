marksSum = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
studentsPoints = []
mark = 0


while True:
    studentsPoint = int(input("A diákok pontjai: "))

    if studentsPoint > 0:
        studentsPoints.append(studentsPoint)
    else:
        print("A diák pontja nem lehet kevesebb, mint 1!")

    if len(studentsPoints) > 9:
        break

print(studentsPoints)

def pointsCalculator(points):
    if points >= 90:
        marksSum[5] += 1
        return 5
    elif points < 90 and points >= 80:
        marksSum[4] += 1
        return 4
    elif points < 80 and points >= 70:
        marksSum[3] += 1
        return 3
    elif points < 70 and points >= 60:
        marksSum[2] += 1
        return 2
    elif points < 60:
        marksSum[1] += 1
        return 1
    else:
        return 'Érvénytelen pontszám!'
    
for points in studentsPoints:
    mark = pointsCalculator(points)
    
    print(f"A diákok dolgozatai: {mark}")

print(marksSum)
