def predictMarks(subject_1, subject_2):

    b = [ 0.00274048,  0.09441056,  0.89189383]

    y = b[0] + b[1] * subject_1 + b[2] * subject_2

    return y