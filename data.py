# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:08:35 2022

@author: boogy
"""

import csv
import numpy as np
import matplotlib.pylab as plt




months = []
datarows = []
vehicle = []
buses = []
cars = []
gov = []
motor = []
RC = []
taxi = []


openfile = open("mvehpop_dataset.csv")
csvreader = csv.reader(openfile)

for row in csvreader:
     datarows.append(row)
#print(datarows)

ix = 1
while ix <= 12:
     months.append(datarows[0][ix])
     ix += 1
#print(months)

#[a] - list no., [b] - item no. in list 
#for range include + 1(for last value)
#for ix in range(1,13):
        #months.append(datarows[0][ix])
        #ix += 1
#print(months)

    
for a in range(1,7):
    vehicle.append(datarows[a][0])
    a += 1
#print(vehicle)


for b in range(1,13):
    buses.append(datarows[1][b])
    b += 1
    buses = [int(i) for i in buses] #using list comprehension
#print(buses)

for c in range(1,13):
    cars.append(datarows[2][c])
    c += 1
    cars = [int(i) for i in cars] #using list comprehension
#print(cars)

for gv in range(1,13):
    gov.append(datarows[3][gv])
    gv += 1
    gov = [int(i) for i in gov]  #using list comprehension
#print(gov)

for mt in range(1,13):
    motor.append(datarows[4][mt])
    mt += 1
    motor = [int(i) for i in motor]  #using list comprehension
#print(motor)

for rc in range(1,13):
    RC.append(datarows[5][rc])
    rc += 1
    RC = [int(i) for i in RC]  #using list comprehension
#print(RC)

for tx in range(1,13):
    taxi.append(datarows[6][tx])
    tx +=1
    taxi = [int(i) for i in taxi] #using list comprehension
#print(taxi)







#ShowMenu function def
def showMenu():
    print("="*70)
    print("Please choose one of the following options")
    print("A - Display Bus population for all months in 2012")
    print("B - Display mean of selected vehicle in 6-month span of Jul - Dec")
    print("C - Display months of selected vehicle in which vehicle population increased by less than 3% over previous month")
    print("D - Display plots")
    print("Q - Quit")
    print("="*70)
    #sel = input("Please select A, B, C, D, or Q: ")
    



#Function for option A
def dispBus():
    for ms,val in zip(months,buses):
        print(f"Vehicle Population for Buses in {ms} 2012 is {val}.")
#dispBus()
    
    
    
#Function for option B
def dispmeanveh(listname):
    mean_veh = 0
    mean_veh = sum(listname[6:])/6
    print(f"Mean of vehicle population in the 6-month span of Jul - Dec for selected vehicle is {mean_veh:.0f}.")
    
    for mt,val in zip(months[6:],listname[6:]):
        if val < mean_veh:
            print(f"Vehicle population in {mt} is {val} which is below the mean.")
        else:
            pass
#dispmeanveh()




#Function for option C
def dispinveh(listname):
    ic = 1
    months_list = []
    percent_change = []
    vehpop_list = []
    while ic < 12:
        months_list.append(months[ic])
        vehpop_list.append(listname[ic])
        percent_change.append((listname[ic] - listname[ic-1])/ (listname[ic-1]) * 100 )
        ic += 1

    for change,mt,veh in zip(percent_change, months_list, vehpop_list):
        if change < 3 and change > 0:
            print(f"Vehicle population in {mt} had increased by less than 3% over the previous month. The vehicle population in {mt} is {veh}.")
        else:
            pass
   
#dispinveh(taxi)


#Function for option D
def plotline():
    
#To create a list consisting of difference btw Taxi and Buses
    difference = []
    zip_diff = zip(taxi, buses)

    for taxi_i, buses_i in zip_diff:
        difference.append(taxi_i - buses_i)
    #print(difference)
#plotline()

#x-axis is months, y-axis is difference
    plt.plot(months, difference, marker = 'o', label = "Vehicle population difference")
    plt.title('Difference between Taxi and Buses vehicle population vs Month')
    plt.xlabel('Months')
    plt.ylabel('Difference between Taxi and Buses vehicle Population')
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()
    
#plotline()



def plotbar():
#use np.arange() to create range of values, X = no. of values for X_axis
#bars are shifted -0.2/ +0.2 units from the X values to avoid overlapping
#width of bars taken as 0.5 units
    X = np.arange(len(months))
    plt.bar(X - 0.2, buses, 0.5, label = 'Buses')
    plt.bar(X + 0.2, taxi, 0.5, label = 'Taxi')
    plt.xticks(X,months)
    plt.xlabel('Months')
    plt.ylabel('Vehicle population of Buses & Taxis')
    plt.title('Population of Buses & Taxi vs Month')
    plt.legend()
    plt.show()
    
#plotbar()









