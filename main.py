# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# Weather: rainy', 'sunny', 'windy', 'neutral'
# Time of day: 'day', 'night'
# Cow milking status: 'True', 'False'
# Location of the cows: 'pasture', 'cowshed'
# Season: 'winter', 'spring', 'summer', 'fall'
# Slurry tank: 'True', 'False'
# Grass status: 'True', 'False'


def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Location_of_the_cows == 'pasture' and Time_of_day == 'night':
        return('take cows to cowshed')
    if Location_of_the_cows == 'pasture' and Weather == 'rainy':
        return('take cows to cowshed')
    if Location_of_the_cows == 'cowshed':
        return('milk cows')
    if Location_of_the_cows == 'cowshed' and Slurry_tank == True and Weather != 'sunny':
        return('fertilize pasture')
    if Location_of_the_cows == 'cowshed' and Weather != 'windy':
        return('fertilize pasture')
    if Location_of_the_cows == 'pasture' and Cow_milking_status == True and Weather == 'sunny' and Time_of_day == 'day' and Season == 'spring' and Slurry_tank == False and Grass_status == True:
        #return('take cows to cowshed \nmilk cows \nmow grass \ntake cows back to pasture')
        
        #return('take cows to cowshed \nmilk cows \nmow grass') 
        #return('take cows back to pasture')

        #return('take cows to cowshed \nmilk cows \ntake cows back to pasture')

        return('take cows to cowshed \nmilk cows') 
        return('take cows back to pasture')

    if Location_of_the_cows == 'cowshed' and Grass_status == 'True' and Season == 'spring' and Weather == 'sunny':
        print('mow grass')
    else:
        print('wait')


farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

