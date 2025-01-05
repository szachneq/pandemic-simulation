# Pandemic simulation

[https://pandemic-simulation.streamlit.app/](https://pandemic-simulation.streamlit.app/)

## Running the code

Install requirements
```sh
pip install -r requirements.txt
```

Run the application
```sh
streamlit run main.py
```

# Description

This is a simple simulation of a pandemic, with a few assumptions:
- Population of given size starts with the specified amount of sick people
- Every single day all the people meet each other
- For every contact with a healthy person, a sick person has a probability of spreading the disease specified by the user
- After that, every sick person has a chance of recovery specified by the user
- This cycle continues until there is no sick person left
- People who recovered from the disease cannot become sick again
- The disease is not lethal and everyone infected survives until the end of the simulation
- The simulation may either end when every single person gets infected and everyone recovers, or the disease spreads too slowly and initial population of sick people recovers before spreading the disease further
- For the same input parameters, the simulation may have a different outcomes

This repository was created during data science course hosted by [Mateusz Dorobek](https://github.com/mateuszdorobek)
