def bmi(weight, height):
    if weight > 200 and height > 4:
        return "LOI"
    
    if weight <= 0 and height <= 0:
        return "LOI"
    
    bmi = weight / (height * height)

    if bmi < 18.5:
        return "THIEU CAN"
    elif 18.5 <= bmi <= 24.9:
        return "BINH THUONG"
    elif 25 <= bmi <= 29.9:
        return "THUA CAN"
    else:
        return "BEO PHI"