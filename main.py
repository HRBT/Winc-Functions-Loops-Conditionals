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
    if Location_of_the_cows == 'pasture' and Time_of_day == 'night' or Weather == 'rainy':
        return('take cows to cowshed')
    if Location_of_the_cows == 'cowshed' and Time_of_day == 'day' and Cow_milking_status == True:
        return('milk cows')
    elif Location_of_the_cows == 'pasture' and Time_of_day == 'day' and Cow_milking_status == True:
        return('take cows to cowshed\nmilk cows\ntake cows back to pasture')
        #print('take cows to cowshed')
        #print('milk cows')
        #print('take cows back to pasture')
    if Location_of_the_cows == 'cowshed' and Time_of_day == 'day' and Slurry_tank == True and Weather != 'sunny':
        return('fertilize pasture')
    elif Location_of_the_cows == 'pasture' and Time_of_day == 'day' and Slurry_tank == True and Weather != 'sunny':
        return('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
        #print('take cows to cowshed')
        #print('fertilize pasture')
        #print('take cows back to pasture')
    if Location_of_the_cows == 'cowshed' and Time_of_day == 'day' and Slurry_tank == True and Weather != 'windy':
        return('fertilize pasture')
    elif Location_of_the_cows == 'pasture' and Time_of_day == 'day' and Slurry_tank == True and Weather != 'windy':
        return('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
        #print('take cows to cowshed')
        #print('fertilize pasture')
        #print('take cows back to pasture')
    if Location_of_the_cows == 'cowshed' and Time_of_day == 'day' and Grass_status == True and Season == 'spring' and Weather == 'sunny':
        return('mow grass') 
    elif Location_of_the_cows == 'pasture' and Time_of_day == 'day' and Grass_status == True and Season == 'spring' and Weather == 'sunny':
        return('take cows to cowshed\nmow grass\ntake cows back to pasture')
        #print('take cows to cowshed')
        #print('mow grass')
        #print('take cows back to pasture')
    #elif Location_of_the_cows == 'cowshed' and Time_of_day =='day' and Cow_milking_status == False and Slurry_tank == False and Grass_status == False:
     #   return('take cows back to pasture')
    else:
        return('wait')

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

