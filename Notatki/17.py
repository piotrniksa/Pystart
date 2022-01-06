def rating(score: int) -> str:
    if score < 45:
        return 'niedostateczny'
    if score in range(45, 55):
        return 'dopuszczający'
    if score in range(55, 80):
        return 'dostateczny'
    if score in range(80, 90):
        return 'dobry'
    if score in range(90, 95):
        return 'bardzo dobry'
    if score in range(95, 101):
        return 'celujący'


print(rating(95))
