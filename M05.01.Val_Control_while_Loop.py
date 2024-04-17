# MovieGuide.py - This program allows each theater patron to enter a value from 0 to 4
# indicating the number of stars that the patron awards to the Guide's featured movie of the
# week. The program executes continuously until the theater manager enters a negative number to
# quit. At the end of the program, the average star rating for the movie is displayed.

#Get input.
totalStars = 0  # total of star ratings
numPatrons = 0  # keep track of number of patrons

print("Enter the number of stars (0-4) each patron awards the movie, or a negative number to quit.")
#Write while loop here
while True:
    rating = input("Enter rating: ")  # prompt for input
    try:
        rating = int(rating)  # convert rating to an integer
        if rating < 0:  # negative number exits the loop
            break
        if 0 <= rating <= 4:  # valid rating range
            totalStars += rating
            numPatrons += 1
        else:
            print("Invalid input. Please enter a number from 0 to 4.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Calculate average star rating
if numPatrons > 0:
    averageStars = totalStars / numPatrons  # calculate average rating
else:
    averageStars = 0

print("Average Star Value:", averageStars)







