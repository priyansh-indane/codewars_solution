def better_than_average(class_points, your_points):
    total_points = sum(class_points) + your_points
    total_people = len(class_points) + 1
    average = total_points / total_people
    
    return your_points > average
