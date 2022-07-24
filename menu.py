# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 10:08:03 2022

@author: boogy
"""
import data as d

loop = True

while loop:
    #call showMenu function
    d.showMenu()
    #Read user selected option
    sel = input("Please select A, B, C, D, or Q: ")
    #Use if-elif-else...
    if sel == "A" or sel == "a":
        d.dispBus()
    
    elif sel == "B" or sel == "b":
        print("="*70)
        print("Buses")
        print("Cars")
        print("GOV")
        print("Motor")
        print("RC")
        print("Taxi")
        print("="*70)
        sel = input("Please select Buses, cars, GOV, motor, RC or Taxi: ")
        if sel == "Buses":
            d.dispmeanveh(d.buses)
        elif sel == "Cars":
            d.dispmeanveh(d.cars)
        elif sel == "GOV":
            d.dispmeanveh(d.gov)
        elif sel == "Motor":
            d.dispmeanveh(d.motor)
        elif sel == "RC":
            d.dispmeanveh(d.RC)
        elif sel == "Taxi":
            d.dispmeanveh(d.taxi)
        else:
            print("Sorry invalid selection. Try again!")
            
    elif sel == "C" or sel == "c":
        print("="*70)
        print("Buses")
        print("Cars")
        print("GOV")
        print("Motor")
        print("RC")
        print("Taxi")
        print("="*70)
        sel = input("Please select Buses, Cars, GOV, Motor, RC or Taxi: ")
        if sel == "Buses":
            d.dispinveh(d.buses)
        elif sel == "Cars":
            d.dispinveh(d.cars)
        elif sel == "GOV":
            d.dispinveh(d.gov)
        elif sel == "Motor":
            d.dispinveh(d.motor)
        elif sel == "RC":
            d.dispinveh(d.RC)
        elif sel == "Taxi":
            d.dispinveh(d.taxi)
        else:
            print("Sorry invalid selection. Try again!")
        
    elif sel == "D" or sel == "d":
        print("A - line plot of difference between Taxi and Buses population vs Month")
        print("B - bar chart of Buses & Taxi population vs Month")
        sel = input("Please select A or B: ")
        if sel == "A":
            d.plotline()
        elif sel == "B":
            d.plotbar()
        else:
            print("Sorry invalid selection. Try again!")
            
    elif sel == "Q" or sel == "q":
        loop = False
    else:
        print("Sorry invalid selection. Try again!")
        
        
