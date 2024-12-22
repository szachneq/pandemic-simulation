import streamlit as st
import matplotlib.pyplot as plt

from simulation import Simulation

if "running" not in st.session_state:
    st.session_state.running = False

if "data" not in st.session_state:
    st.session_state.data = None


def run_simulation():
    epidemic_simulation = Simulation(
        population=population_size,
        initially_infected=initially_infected,
        recovery_chance=recovery_chance / 100,
        transmission_rate=transmission_rate / 100,
    )

    days = epidemic_simulation.run()

    unaffected, infected, recovered = zip(*epidemic_simulation.history)
    days = range(len(epidemic_simulation.history))

    st.session_state.data = days, unaffected, infected, recovered


st.title("Pandemic Simulation")

with st.expander(
    label="Simulation Description",
    icon=":material/info:",
):
    st.markdown(
        body="""
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
    """
    )

st.header("Simulation parameters")

disabled = st.session_state.running

with st.form(key="form"):
    left, right = st.columns(2)

    with left:
        population_size = st.number_input(
            label="Population size:",
            min_value=1,
            max_value=10_000,
            value=1000,
            step=1,
            disabled=disabled,
        )

        initially_infected = st.number_input(
            label="Number of initially infected people:",
            min_value=1,
            max_value=population_size,
            value=5,
            step=1,
            disabled=disabled,
        )

    with right:
        transmission_rate = st.number_input(
            label="Transmission probability [%]:",
            min_value=0.1,
            max_value=100.0,
            value=5.0,
            step=0.1,
            disabled=disabled,
            help="Determines how probable is it that a sick person will spread the virus to a healthy one",
        )

        recovery_chance = st.number_input(
            label="Recovery chance [%]:",
            min_value=0.1,
            max_value=100.0,
            value=2.5,
            step=0.1,
            disabled=disabled,
            help="Determines how probable is it that a sick person will recover from the disease on a given day",
        )

    submitted = st.form_submit_button(
        label="Run simulation",
        type="primary",
        icon=":material/play_arrow:",
        on_click=lambda: st.session_state.update(running=True),
        disabled=disabled,
    )

    if submitted:
        with st.spinner("Running simulation..."):
            run_simulation()
        st.session_state.update(running=False)
        st.rerun()

st.divider()

if not st.session_state.data or st.session_state.running:
    # Show placeholder message
    c = st.container(
        border=True,
        height=200,
    )
    c.markdown(
        body=f"""
            <div style="text-align: center;">
                Results will appear here.
            </div>""",
        unsafe_allow_html=True,
    )
else:
    days, unaffected, infected, recovered = st.session_state.data

    plt.figure(figsize=(10, 6))
    plt.plot(days, unaffected, label="unaffected")
    plt.plot(days, infected, label="infected")
    plt.plot(days, recovered, label="recovered")

    plt.xlabel("days")
    plt.ylabel("number of people")
    plt.title("Epidemic simulation results")
    plt.legend()

    st.pyplot(plt)

    st.code(
        f"""
        Population size: {population_size}
        Number of initially infected people: {initially_infected}
        Transmission probability: {transmission_rate}%
        Recovery chance: {recovery_chance}%
    """
    )
