import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv' , delimiter= ',' , skip_header=True)


#mean speed  =  dis/time       millsperhr

speed = taxi[:, 7] // (taxi[:, 8]/3600)

mean_speed = speed.mean()
print( "mean speed == ",mean_speed)

# number of rides taken in mongth of feb 2 month collumn

feb_rides = taxi[: , 1]

print("number of rides are == " , feb_rides[feb_rides == 2 ].shape[0])


more =  taxi[taxi[:, -3] > 50 , -3]

print("tip ammount greater then 50 is " , more.shape[0])

droploc =  taxi[taxi[:, 6] == 2, 6]

print("grop loc --< " , droploc.shape[0])
