
# In this exercise you'll try to build a neural network that predicts the number of sea turtles according to the temperature based on a simple formula.
# In the paper titled Densities and drivers of sea turtle populations across Pacific coral reef ecosystems, it has found that there is a big correlation between Sea Surface Temperature (SST) and sea turtle population. SST was the most influential driver of turtle density. Turtle density peaked at 27.5°C.
# Given the importance of SST, they have mentioned how warming might shift turtle densities. If documented rates of warming continue with climate change, sea turtles might be in big danger.
# When the SST arise, coral reef habitats are affected a lot and due to ocean acidification coral reef density decreases as well.
# Even there is not an equation that shows the correlation between SST and sea turtles. Imagine calculating number of sea turtles in a region was as easy as 50 + 20*(percent cover of corals over a tile)
# So a region with 1 percent cover of corals will have 70 sea turtles, 2 percent cover of corals will have 90 sea turtles, a region with 3 percent cover of corals will have 110 sea turtles and so on
# How would you create a neural network that learns this relationship so that it would predict the number of sea turtles given 7 percent cover of coral reefs as close to 190.

import sys
from pathlib import Path

# This exercise is named tensorflow.py. When running it directly, exclude its
# folder from package lookup so "import tensorflow" loads the installed library.
if __name__ == "__main__":
    script_directory = Path(__file__).resolve().parent
    sys.path = [
        entry for entry in sys.path
        if Path(entry).resolve() != script_directory
    ]

import tensorflow as tf
import numpy as np
from tensorflow import keras


def main():
    keras.utils.set_random_seed(42)

    # Define the model: one neuron learns a weight and bias (y = weight*x + bias).
    model = keras.Sequential([
        keras.Input(shape=(1,)),
        keras.layers.Dense(units=1),
    ])
    model.compile(
        optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
        loss="mean_squared_error",
    )

    # Define the input: coral cover in percentage points (1 means 1%).
    coral_cover = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32).reshape(-1, 1)

    # Define the output: example turtle counts following 50 + 20*coral_cover.
    turtle_counts = np.array([70, 90, 110, 130, 150, 170], dtype=np.float32).reshape(-1, 1)

    # Train on the examples; 7% is kept out of the training data.
    model.fit(coral_cover, turtle_counts, epochs=500, batch_size=6, verbose=0)

    # Predict for a new input using the learned relationship.
    new_cover = np.array([[7.0]], dtype=np.float32)
    prediction = model.predict(new_cover, verbose=0)
    print(f"Predicted sea turtles at 7% coral cover: {prediction[0, 0]:.2f}")
    print("Expected sea turtles from the exercise formula: 190")


if __name__ == "__main__":
    main()
