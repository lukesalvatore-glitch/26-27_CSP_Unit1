days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
my_courses = ["Cyber_Security","Marketing_2", "APGOV", "APBIZZ","Photo","APCS","English"]

for d in days_of_week:
  print(d)

  for c in my_courses:
    print("  " + c)


    points = int(input("How many points would you like to grade? "))

    # Use this as a reference to the grading system
    if points >= 98:
        print("A+")
    elif points >= 94:
        print("A")
    elif points >= 90:
        print("A-")
    elif points >= 88:
        print("B+")
    elif points >= 85:
        print("B")
    elif points >= 83:
        print("B-")
    elif points >= 77:
        print("C+")
    elif points >= 75:
        print("C")
    elif points >= 70:
        print("C-")
    elif points >= 67:
        print("D+")
    elif points >= 65:
        print("D")
    elif points >= 60:
        print("D-")
    elif points <= 50:
        print("F")



