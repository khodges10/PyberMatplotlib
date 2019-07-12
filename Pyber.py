%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
city_data = pd.read_csv(city_data_to_load)
ride_data = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
pyber_data = pd.merge(ride_data, city_data, how= "left", on= "city")

# Display the data table for preview
pyber_data.head()

# Put each city type in dataframe
urban_city = pyber_data[pyber_data["type"] == "Urban"].groupby([pyber_data["city"]])
rural_city = pyber_data[pyber_data["type"] == "Rural"].groupby([pyber_data["city"]])
suburban_city = pyber_data[pyber_data["type"] == "Suburban"].groupby([pyber_data["city"]])

# Obtain the x and y coordinates for each of the three city types
x_urban = urban_city["ride_id"].count()
y_urban = urban_city["fare"].mean()
s_urban = urban_city["driver_count"].mean()

x_rural = rural_city["ride_id"].count()
y_rural = rural_city["fare"].mean()
s_rural = rural_city["driver_count"].mean()

x_suburban = suburban_city["ride_id"].count()
y_suburban = suburban_city["fare"].mean()
s_suburban = suburban_city["driver_count"].mean()

# Build the scatter plots for each city types
plt.scatter(x_urban, y_urban, label = "Urban", s = s_urban*5, c = "cyan", edgecolors = "black")
plt.scatter(x_rural, y_rural, label = "Rural", s = s_rural*5, c = "lime", edgecolors = "black")
plt.scatter(x_suburban, y_suburban, label = "Suburban", s = s_suburban*5, c = "magenta", edgecolors = "black")
plt.grid()

# Incorporate the other graph properties
plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (per city)")
plt.ylabel("Average Fare ($)")

# Create a legend
legend = plt.legend(fontsize = 8, title = "City Types")

# Adjusting legend so all same size
legend.legendHandles[0]._sizes = [30]
legend.legendHandles[1]._sizes = [30]
legend.legendHandles[2]._sizes = [30]

# Incorporate a text label regarding circle size
plt.text(43,32,"Note: Circle size correlates with driver count per city.", fontsize = 8)

# Save Figure
plt.savefig("PyberRideSharingData.png", bbox_inches="tight")

# Show plot
plt.show()

# Calculate Type Percents
type_group = pyber_data.groupby(["type"])
fare_sum = type_group["fare"].sum()

# Build Pie Chart
labels = ["Urban","Rural","Suburban"]
explode = (0, 0, 0.1)
colors = ["cyan", "lime", "magenta"]
plt.pie(fare_sum, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=150)
plt.title("% of Total Fares by City Type")

# Save Figure
plt.savefig("TotalFaresbyCityType.png", bbox_inches="tight")

# Show Figure
plt.show()

# Calculate Ride Percents
rides_count = type_group['ride_id'].count()

# Build Pie Chartplt.savefig("TotalFaresbyCityType.png", bbox_inches="tight")
labels = ["Urban","Rural","Suburban"]
explode = (0, 0, 0.1)
colors = ["cyan", "lime", "magenta"]
plt.pie(rides_count, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=150)
plt.title("% of Total Rides by City Type")

# Save Figure
plt.savefig("TotalRidesbyCityType.png", bbox_inches="tight")

# Show Figure
plt.show()

# Calculate Driver Percents
type_group_drivers = city_data.groupby(['type'])
drivers_sum = type_group_drivers['driver_count'].sum()

# Build Pie Charts
labels = ["Urban","Rural","Suburban"]
explode = (0, 0, 0.1)
colors = ["cyan", "lime", "magenta"]
plt.pie(drivers_sum, explode=explode, labels=labels, colors=colors,autopct="%1.1f%%", shadow=True, startangle=150)
plt.title("% of Total Drivers by City Type")

# Save Figure
plt.savefig("TotalDriversbyCityType.png", bbox_inches="tight")

# Show Figure
plt.show()

