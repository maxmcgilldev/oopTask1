
#  The following is a template of the design.
#  you will need to complete the definition of each class, including class attributes,
# instance attributes, and instance methods. However, please do not change the class 
# names provided below.

# IMPORTANT: In order to get your program pass the test, make sure your class constructors 
# use exactly the same parameter names as in the test examples provided at the end of this template. 

# ================Your codes start here=============
class Boat:
#  pass

class Engine:    
# pass  
		
class Motorboat:
 # pass

class Pedalboat:
#  pass

class Eboat:
 # pass

# ============ End of your codes here ==================






# ============No modification beyond here =============
# the following is a list of test instances, please do not modify them
if __name__ == '__main__':
  # arguments: co - color, br - brand, yr - year, tech - technology used in engine
  boat1=Boat(co='Black', br='Trek', yr=2012)
  engine1=Engine(tech='gas')
  print(engine1.get_engine_speed())

  # arguments: co - color, br - brand, yr - year, ps - pedal speed
  pedalboat1=Pedalboat(co='Red', br='GIANT', yr=2015, ps=15)
  pedalboat2=Pedalboat(co='Red', br='GIANT', yr=2015, ps=30)
  print(pedalboat1.get_pedal_speed())
  print(pedalboat2.get_pedal_speed())
  print(pedalboat1.cal_travel_time(300))

  # arguments: co - color, br - brand, yr - year, ps - pedal speed, bt - battery time 
  eboat1=Eboat(co='Blue', br='Basis', yr=2018, ps=15, bt=10)
  print(eboat1.get_max_speed())
  print(eboat1.cal_travel_time(350))
  print(eboat1.cal_travel_time(650))

  # arguments: co - color, br - brand, yr - year, fl - fuel level, fe - fuel efficiency
  motorboat1=Motorboat(co='Silver', br='YAMAHA', yr=2013, fl=40, fe=12)
  print(motorboat1.get_max_speed())
  print(motorboat1.cal_travel_time(300))
  print(motorboat1.cal_travel_time(600))

  # get the age of all bikes created
  for b in Boat.all_boats:
    print(b.get_boat_age(2023))
