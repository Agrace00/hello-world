height = float(input('Enter the height from which the ball is dropped: '))
bounce_index = float(input('Enter the bounciness index of the ball: '))
num_bounces = int(input('Enter the number of times the ball is allowed to continue bouncing: '))
distance_traveled = height
while (num_bounces > 1):
    height = height * bounce_index
    distance_traveled = distance_traveled + (2 * height)
    num_bounces = num_bounces - 1
distance_traveled = distance_traveled + (height * bounce_index)
print('\nThe total distnace is : ' + str(distance_traveled) + ' units.')
