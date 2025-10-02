def bmi(weight, height):
    if weight > 200 and height > 4:
        return "LOI"
    
    if weight <= 0 and height <= 0:
        return "LOI"
    
    bmi = weight / (height * height)

    if bmi < 18.5:
        return "THIEU CAN"
    elif 18.5 <= bmi < 24.9:
        return "BÌNH THƯỜNG"
    elif 25 <= bmi < 29.9:
        return "THUA CAN"
    elif 30 <= bmi < 39.9:
        return "BEO PHI"
    else:
        return "BEO PHI NANG"