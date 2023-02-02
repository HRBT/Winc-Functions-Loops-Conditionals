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



#Day

def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')


#Night
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture \ntake cows back to pasture')


#Night plus not milking
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')



#Day + Slurry Tank

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')


#Night + Slurry Tank
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + Slurry Tank
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')




#Day + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')


#Night + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')


#Night plus not milking + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')



#Day + Slurry Tank + Location

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')


#Night + Slurry Tank + Location 
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Slurry Tank + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + Location
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'winter' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')





#Day + SEASON SPRING

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \n mow grass \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')


#Night + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \n mow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmow grass \take cows bach to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture \ntake cows back to pasture')


#Night plus not milking + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')



#Day + Slurry Tank + SEASON SPRING

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nmow grass \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')


#Night + Slurry Tank + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + Slurry Tank + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')




#Day + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')


#Night + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('mow grass')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')


#Night plus not milking + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('mow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')



#Day + Slurry Tank + Location + SEASON SPRING

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')


#Night + Slurry Tank + Location + SEASON SPRING 
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows \nmow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Slurry Tank + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('mow grass')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + Location + SEASON SPRING
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('mow grass')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')



#NUEVO OTRA VEZ

#Day + SEASON SPRING + GRASS FALSE

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')


#Night + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \ntake cows bach to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed \nfertilize pasture \ntake cows back to pasture')


#Night plus not milking + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('take cows to cowshed')



#Day + Slurry Tank + SEASON SPRING + GRASS FALSE

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')


#Night + Slurry Tank + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + Slurry Tank + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')


#Night plus not milking + Slurry Tank + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('take cows to cowshed')




#Day + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows \nfertilize pasture')


#Night + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('milk cows')




#Day plus not milking + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('fertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('fertilize pasture')


#Night plus not milking + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == True and \
                            Grass_status == False:
        return ('wait')



#Day + Slurry Tank + Location + SEASON SPRING + GRASS FALSE

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')


#Night + Slurry Tank + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('milk cows')




#Day plus not milking + Slurry Tank + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')


#Night plus not milking + Slurry Tank + Location + SEASON SPRING + GRASS FALSE
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'spring' and \
                        Slurry_tank == False and \
                            Grass_status == False:
        return ('wait')


# PENULTIMO NUEVO


#Day + SUMMER

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')


#Night + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture \ntake cows back to pasture')


#Night plus not milking + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')



#Day + Slurry Tank + SUMMER

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')


#Night + Slurry Tank + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + Slurry Tank + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')




#Day + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')


#Night + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')


#Night plus not milking + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')



#Day + Slurry Tank + Location + SUMMER

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')


#Night + Slurry Tank + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Slurry Tank + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + Location + SUMMER
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'summer' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')



#Day + FALL

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \nfertilize pasture \ntake cows back to pasture')


#Night + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed \nfertilize pasture \ntake cows back to pasture')


#Night plus not milking + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('take cows to cowshed')



#Day + Slurry Tank + FALL

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')


#Night + Slurry Tank + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed \nmilk cows')




#Day plus not milking + Slurry Tank + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'pasture' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('take cows to cowshed')




#Day + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows \nfertilize pasture')


#Night + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('fertilize pasture')


#Night plus not milking + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == True and \
                            Grass_status == True:
        return ('wait')



#Day + Slurry Tank + Location + FALL

#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')


#Night + Slurry Tank + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == True and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('milk cows')




#Day plus not milking + Slurry Tank + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'day' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')


#Night plus not milking + Slurry Tank + Location + FALL
#def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if Weather == 'rainy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'sunny' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'windy' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

    if Weather == 'neutral' and \
        Time_of_day == 'night' and \
            Cow_milking_status == False and \
                Location_of_the_cows == 'cowshed' and \
                    Season == 'fall' and \
                        Slurry_tank == False and \
                            Grass_status == True:
        return ('wait')

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

 