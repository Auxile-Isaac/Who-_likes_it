def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        like = str(names[0]) + " and " + str(names[1]) + " like this"
        return like
    elif len(names) == 3:
        like = str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
        return like
    elif len(names) >= 4:
        others = len(names) - 2
        like = str(names[0]) + ", " + str(names[1]) + " and " + str(others) + " others like this"
        return like


print(likes(["Alex", "Jacob", "Mark", "Max"]))
