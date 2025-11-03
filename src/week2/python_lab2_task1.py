# Lab 3.1 – Simple Datasets and Aggregates


temperatures = [22, 24, 19, 23, 25, 21, 20]  # daily temperatures for a week
city_population = {
    "Riga": 632614,
    "Daugavpils": 82789,
    "Liepaja": 68199,
    "Jelgava": 55663,
    "Jurmala": 49500
}


average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]
total_population = sum(city_population.values())


print(f"Average temperature for the week: {average_temperature:.2f}°C")
print(f"Largest city: {largest_city} with a population of {largest_population}")
print(f"Total population of all cities: {total_population}")
