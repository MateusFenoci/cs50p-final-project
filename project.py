import pandas as pd
import random as rd

def main():
    data = pd.read_csv('data.csv', delimiter=';', usecols=['Lat', 'Long'], nrows=84)
    data['Lat'] = data['Lat'].str.replace(',', '.')
    data['Long'] = data['Long'].str.replace(',', '.')
    data['Lat'] = data['Lat'].astype(float)
    data['Long'] = data['Long'].astype(float)
    cords = list(zip(data['Lat'], data['Long']))
    cords = remove_duplicates(cords)
    first_point = rd.choice(cords)
    routes = route(first_point, cords)
    print(f'Starting at the point {first_point}')
    print(routes)


def remove_duplicates(cords:list):
    newCords = []
    for cord in cords:
        if cord not in newCords:
            newCords.append(cord)
    return newCords

def distance_calculator(x1, x2):
    distance = float(((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2) ** 0.5)
    return distance


def route_tracer(first_point, cords):
    smallest_distance = float('inf')
    closest_point = None

    for cord in cords:
        distance = distance_calculator(first_point, cord)
        if distance < smallest_distance:
            smallest_distance = distance
            closest_point = cord
    return closest_point

def route(first_point, cords):
    routes = []
    while cords:
        closest_point = route_tracer(first_point, cords)
        first_point = closest_point
        routes.append(closest_point)
        cords.remove(closest_point)
    return routes

if __name__ == "__main__":
    main()