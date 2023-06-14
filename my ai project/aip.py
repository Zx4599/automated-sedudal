import random
import numpy as np
from deap import creator, base, tools, algorithms
import tkinter as tk
courses = [
    "ENCS4370 - COMPUTER ARCHITECTURE - Ayman Ali Mohammad Hroub",
    "ENCS5150 - ADVANCED COMPUTER SYSTEMS ENGINEERING LABORATORY - Yazan Jamal Ibrahim Abu Farha",
    "ENCS5300 - GRADUATION PROJECT - Adnan Hussein Mahmoud Yahya",
    "ENCS5322 - NETWORK SECURITY PROTOCOLS - Ahmad Saleh Ibrahim Alsadeh",
    "ENCS5332 - VLSI DESIGN - Khader Shehadeh Nassar Mohammad",
    "ENCS5341 - MACHINE LEARNING AND DATA SCIENCE - Yazan Jamal Ibrahim Abu Farha",
    "ENCS5399 - SP.TOP: VERIFICATION AND VALIDATION OF HARDWARE - Ayman Ali Mohammad Hroub",
    "ENEE2101 - BASIC ELECTRICAL ENGINEERING LAB - Jaser Abdel Mon'En Fayiz Sa'Ed",
    "ENEE2102 - CIRCUITS LAB - Jaser Abdel Mon'En Fayiz Sa'Ed",
    "ENEE2103 - CIRCUITS AND ELECTRONICS LABORATORY - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENEE2304 - CIRCUIT ANALYSIS - Jaser Abdel Mon'En Fayiz Sa'Ed",
    "ENEE2307 - PROBABILITY AND ENGINEERING STATISTICS - Mohammad Khaleel Issa Jubran",
    "ENEE2311 - NETWORK ANALYSIS 1 - Alhareth M. T. Zyoud",
    "ENEE2312 - SIGNALS AND SYSTEMS - Jamal Othman Hosen Seyam",
    "ENEE2360 - ANALOG ELECTRONICS - Nasser Abdel Jaleel Muhammad Ismail",
    "ENEE3101 - ELECTRICAL MACHINES LAB - Ali Hasan Moath Abdo",
    "ENEE3103 - ANALOG ELECTRONICS LAB  (FOR MECHATRONIC STUDENTS) - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENEE3112 - ELECTRONICS LAB - Nasser Abdel Jaleel Muhammad Ismail",
    "ENEE3302 - CONTROL SYSTEMS - Jamal Othman Hosen Seyam",
    "ENEE3304 - ELECTRONICS 2 - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENCS4370 - COMPUTER ARCHITECTURE - Aziz Mohammed Ahmad Qaroush",
    "ENCS5150 - ADVANCED COMPUTER SYSTEMS ENGINEERING LABORATORY - Mohammed Sami Abdul Karim Hussein",
    "ENEE2103 - CIRCUITS AND ELECTRONICS LABORATORY - Nasser Abdel Jaleel Muhammad Ismail",
    "ENEE2304 - CIRCUIT ANALYSIS - Hakam Suleiman Nu'Man Shehadeh",
    "ENEE2307 - PROBABILITY AND ENGINEERING STATISTICS - Alhareth M. T. Zyoud",
    "ENEE2311 - NETWORK ANALYSIS 1 - Ali Hasan Moath Abdo",
    "ENEE2360 - ANALOG ELECTRONICS - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENEE3103 - ANALOG ELECTRONICS LAB  (FOR MECHATRONIC STUDENTS) - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENEE3112 - ELECTRONICS LAB - Mohammad Jehad Mohammad A'Ta Husni Al Ju'Beh",
    "ENEE3305 - POWER ELECTRONICS - Muhammad Sharif Mustafa Abu-Khaizaran"
    ,"ENEE3307 - LIGHTING AND ACOUSTICS ENGINEERING - Hussein Awadallah Ibrahim Zeitawi, Hakam Suleiman Nu'Man Shehadeh"
    ,"ENEE3308 - ELECTROMECHANICAL PRINCIPLES AND APPLICATIONS - Hakam Suleiman Nu'Man Shehadeh"
    ,"ENEE3309 - COMMUNICATION SYSTEMS - Wael A. M. Hashlamoun, Ashraf Sulieman Awad Al-Rimawi, Qadri A. A. Mayyala"
    ,"ENEE3318 - ELECTROMAGNETICS - Ashraf Sulieman Awad Al-Rimawi"
    ,"ENEE4102 - FUNDAMENTALS OF ELECTRICAL MACHINES LAB. - Muhammad Sharif Mustafa Abu-Khaizaran, Ali Hasan Moath Abdo"
    ,"ENEE4104 - ENGINEERING SIMULATION LAB - Jamal Othman Hosen Seyam"
    ,"ENEE4105 - CONTROL AND POWER ELECTRONICS LAB - Hakam Suleiman Nu'Man Shehadeh"
    ,"ENEE4113 - COMMUNICATIONS LAB - Alhareth M. T. Zyoud, Ashraf Sulieman Awad Al-Rimawi, Qadri A. A. Mayyala, Wael A. M. Hashlamoun"
    ,"ENEE4300 - PRACTICAL TRAINING - Mahran S. R. Quraan"
    ,"ENEE4303 - ELECTRICAL MACHINES FUNDAMENTALS - Ali Hasan Moath Abdo"
    ,"ENEE5102 - POWER LAB - Hakam Suleiman Nu'Man Shehadeh"
    ,"ENEE5303 - ELECTRICAL MACHINE DRIVES AND SPECIAL MACHINES - Mahran S. R. Quraan"
    ,"ENEE5304 - INFORMATION AND CODING THEORY - Wael A. M. Hashlamoun"
    ,"ENEE5307 - RENEWABLE ENERGY AND PHOTOVOLTAIC POWER SYSTEMS - Nasser Abdel Jaleel Muhammad Ismail"]
time_slots =["8:00-9:20", "10:00-12:00", "9:20-10:40", "10:40-12:00", "12:00-1:20", "1:20-2:40", "2:40-4:00", "4:00-5:00"]
rooms = ["Masri107", "Masri302", "Masri407", "Masri207", "Masri504", "Masri406", "Masri306", "Masri202", "Masri304", "Masri110", "Masri108", "Aggad415", "WKS213", "Masri503", "Khoury112", "Bamieh105", "Bamieh206", "Masri404", "Bamieh101", "WKS215", "Bamieh104", "PNH303", "Masri206", "Masri203", "Aggad345", "Aggad307", "Bamieh205", "ALSADIK103", "Masri109", "Aggad341", "Bamieh204", "Masri303", "Aggad331/2"]

def create_schedule():
    schedule = []
    for course in courses:
        day = random.choice(["M", "T", "W", "R", "S"])
        time = random.choice(time_slots)
        room = random.choice(rooms)
        schedule.append((course, day, time, room))
    return schedule

def evaluate_schedule(schedule):
    score = 0
    unique_courses = len(set([x[0] for x in schedule]))
    score += unique_courses
    unique_times = len(set([x[2] for x in schedule]))
    score += unique_times
    unique_rooms = len(set([x[3] for x in schedule]))
    score += unique_rooms
    return (score,)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("schedule", create_schedule)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.schedule)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate_schedule)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Define the parameters for the GA
pop = toolbox.population(n=100)
NGEN = 50
CXPB = 0.8
MUTPB = 0.2

# Run the GA
best_schedule = None
best_score = 0
for g in range(NGEN):
    offspring = algorithms.varAnd(pop, toolbox, cxpb=CXPB, mutpb=MUTPB)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    pop = toolbox.select(offspring, k=len(pop))
    best_ind = tools.selBest(pop, k=1)[0]
    current_best_score = best_ind.fitness.values[0]
    if current_best_score > best_score:
        best_schedule = best_ind
        best_score = current_best_score

print("Final schedule:")
for course in best_schedule:
    print(course)
def get_final_output():
    for course in best_schedule:
      final_output = outputs = best_schedule

    return final_output
