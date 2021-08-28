"""
Street has 0 through n stops that passengers can arrive and queue at.

 If a passenger arrives at stop s ⊆ n then weirdly they will want to be 
 dropped off at stop d ⊆ n where d ≠ s
 
 Each passenger will arrive starting at t=0 and then linearly increasing 
 
 Input:
 
1) Time taken to move from stop to stop constant across all stops
2) Number of stops
3) UUID, arrival time, arrival stop, and destination of a passenger

eg)
1
10
[(1, 0, 1, 3), (2, 10, 4, 5), (3, 11, 2, 5), (4, 11, 2, 3), (5, 11, 4, 1)]

loadPassenger
driveToDestination
unloadPassenger
"""

class Passenger():
  def __init__(self,uuid = None, arrivalTime = None, arrivalStop = None, destination = None):
    self.uuid = uuid
    self.arrivalTime = arrivalTime
    self.arrivalStop = arrivalStop
    self.destination = destination
    
    
class Taxi:
  def __init__(self,taxi_no = None,position = None,time = 0):
    self.taxi = taxi_no
    self.loaded = False
    self.position = position
    self.time = time
    
  def loadPassenger(self,passenger):
    self.loaded = True
    #(passenger)
    if self.position == passenger.arrivalStop:
      return
    else:
      self.time += abs(passenger.arrivalStop - self.position)    
      self.position = passenger.arrivalStop
      
    
    
  def driveToDestination(self,passenger):
    self.time += abs(passenger.destination - self.position)
    self.position = passenger.destination
    
  def unloadPassenger(self):
    self.loaded = False
    
    
    

def main(input_array):
  time = 0
  taxi = Taxi(time = time,position = 0)
  passengers = []
  temp = input_array.pop(0)
  passenger = Passenger(temp[0],temp[1],temp[2],temp[3])
  passengers.append(passenger)
  
  while passengers:
    if len(passengers)> 1:
      minLen = 1000
      close_pass_idx = None
      for i in len(passengers):
        if minLen < abs(taxi.position - passengers[i].arrivalStop):
          minLen = abs(taxi.position - passengers[i].arrivalStop)
          close_pass_idx = i
      cur_passenger = passenger.pop(close_pass_idx)            
    else:
      cur_passenger = passengers.pop(0)
    taxi.loadPassenger(cur_passenger)
    taxi.driveToDestination(cur_passenger)
    taxi.unloadPassenger()
    for i in range(len(input_array)):
      if taxi.time > input_array[i][1]:
        passenger = Passenger(input_array[0],input_array[1],input_array[2],input_array[3])
        passengers.append(passenger)
        

main([(1, 0, 1, 3), (2, 10, 4, 5), (3, 11, 2, 5), (4, 11, 2, 3), (5, 11, 4, 1)])