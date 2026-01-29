
# import matplotlib.pyplot as plt

# x = [0,1,2,3,4]
# y = [0,1,4,9,16]
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt
# x = [0,2,4,6,8]
# y = [0,4,16,36,64]
# fig , ax = plt.subplots()
# ax.plot(x,y,marker = 'o', label = 'data points')
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1,2,3,4])
# y =x*2
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# Fruits = ['Apple','Banana','Grapes','cherry']
# Price = [400,350,300,450]

# plt.bar(Fruits,Price)
# plt.title('fruits sales')
# plt.xlabel('Fruits')
# plt.ylabel('Price')
# plt.show()



# import matplotlib.pyplot as plt

# fruits = []
# prices = []

# fruit = input(f"Enter fruit name: ")
# price = int(input(f"Enter price of {fruit}: "))
    
# fruits.append(fruit)
# prices.append(price)

# plt.bar(fruits, prices)
# plt.title("Fruit Sales")
# plt.xlabel("Fruits")
# plt.ylabel("Price")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([12,45,7,89,94,23,67,14,91])
# y = np.array([99,31,72,56,68,47,61,35,77])

# plt.scatter(x,y)
# plt.title('basic scatter plot')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# # Generate random data for the histogram
# data = np.random.randn(1000)

# # Plotting a basic histogram
# plt.hist(data, bins=5, color='red', edgecolor='yellow')

# # Adding labels and title
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Basic Histogram')

# # Display the plot
# plt.show()



# import libraries
# import matplotlib.pyplot as plt
# import numpy as np

# # Creating dataset
# cars = ['AUDI', 'BMW', 'FORD',
#         'TESLA', 'JAGUAR', 'MERCEDES']

# data = [23, 17, 35, 29, 12, 41]

# # Creating plot
# fig = plt.figure(figsize=(10, 7))
# plt.pie(data, labels=cars)

# # show plot
# plt.show()


# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# x = np.linspace(0, 1,100)
# z = np.sin(25 * x)
# y = np.cos(25 * x)

# ax.plot3D(x, y, z, 'red')
# ax.set_title('3D Line Plot')

# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set(style="dark")

# # Load dataset
# fmri = sns.load_dataset("fmri")

# # Plot the responses for different
# # events and regions
# sns.lineplot(
#     x="timepoint",
#     y="signal",
#     hue="region",
#     style="event",
#     data=fmri
# )

# plt.show()


