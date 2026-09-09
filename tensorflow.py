
# In this exercise you'll try to build a neural network that predicts the number of sea turtles according to the temperature based on a simple formula.
# In the paper titled Densities and drivers of sea turtle populations across Pacific coral reef ecosystems, it has found that there is a big correlation between Sea Surface Temperature (SST) and sea turtle population. SST was the most influential driver of turtle density. Turtle density peaked at 27.5°C.
# Given the importance of SST, they have mentioned how warming might shift turtle densities. If documented rates of warming continue with climate change, sea turtles might be in big danger.
# When the SST arise, coral reef habitats are affected a lot and due to ocean acidification coral reef density decreases as well.
# Even there is not an equation that shows the correlation between SST and sea turtles. Imagine calculating number of sea turtles in a region was as easy as 50 + 20*(percent cover of corals over a tile)
# So a region with 1 percent cover of corals will have 70 sea turtles, 2 percent cover of corals will have 90 sea turtles, a region with 3 percent cover of corals will have 110 sea turtles and so on
# How would you create a neural network that learns this relationship so that it would predict the number of sea turtles given 7 percent cover of coral reefs as close to 190.

import tensorflow as tf
import numpy as np
from tensorflow import keras
# Your Code Here#
# define the model

# Your Code Here#
# define the input

# Your Code Here#
# define the output

# Your Code Here#
# Train the model


# Your Code Here#
# Predict for a new input
