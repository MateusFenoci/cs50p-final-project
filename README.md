# Project: Pandora Box
#### Video Showcase:  <https://youtu.be/4tuppiueWew>
#### Description:
This program reads location data from a CSV file, processes the data, and finds the optimal route between a set of points. Here's a description of what the program does:

1. The program starts by importing the necessary libraries, including `pandas` for data handling and `random` for generating random choices.

2. In the `main` function, the program performs the following steps:
   - It reads location data from a CSV file named 'data.csv', specifying that the data is separated by semicolons and selecting the 'Lat' and 'Long' columns.
   - It converts the comma-separated decimal numbers in the 'Lat' and 'Long' columns to use dots as the decimal separator and then converts these values to floating-point numbers.
   - It combines the 'Lat' and 'Long' values into pairs and stores them in the `cords` list.
   - It removes any duplicate coordinates from the `cords` list.
   - It randomly selects a starting point from the cleaned `cords` list.
   - It calculates the optimal route by repeatedly finding the closest coordinate to the current point and adds it to the `routes` list while removing it from the `cords` list. This continues until all coordinates have been visited.
   - It prints the starting point and the calculated route.

3. The program defines several helper functions:
   - `remove_duplicates`: Removes duplicate coordinates from a list.
   - `distance_calculator`: Computes the Euclidean distance between two coordinates.
   - `route_tracer`: Finds the closest coordinate to a given point.
   - `route`: Computes the optimal route based on the starting point and the list of coordinates.

4. The program is structured as a set of functions, and the main logic is encapsulated within the `main` function.

5. Finally, the program runs when executed as the main script (`if __name__ == "__main__"`), which calls the `main` function.

Overall, this program reads geographical coordinates from a CSV file, processes the data, finds the best route to visit all coordinates, and prints the starting point and the optimal route. It's commonly used in applications like route optimization or tour planning.
