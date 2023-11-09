def marksAvarage(*marks):
    avarage = 0
    if len(marks) > 6:
        return 'Max 6 grades!'
    else:
        avarage = sum(marks) / len(marks)
        kreditMarks = marks * 5
        kreditAvarage = sum(kreditMarks) / len(marks)
    return avarage, kreditAvarage
    
print(marksAvarage(5, 4, 3, 2, 1, 5))