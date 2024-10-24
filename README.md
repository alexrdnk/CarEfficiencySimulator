# Economic Assessment of Carsharing Fleet Maintenance Efficiency

Projekt ten wykorzystuje symulacje w Pythonie do generowania zestawów danych dotyczących różnych predefiniowanych strategii konserwacji pojazdów serwisowych. W trakcie symulacji dokładnie monitorowany jest czas użytkowania pojazdów, zarówno podczas ich eksploatacji, jak i w okresach konserwacji, a także rejestrowane są koszty związane z serwisowaniem, przeglądami oraz wymianą pojazdów. Wygenerowane zbiory danych, obejmujące symulacje o różnych okresach trwania, są zapisywane w formacie CSV. Następnie dane te są analizowane i wizualizowane przy użyciu bibliotek takich jak matplotlib i pandas, co umożliwia szczegółową ocenę efektywności strategii konserwacyjnych.

---

## Features

- **Customizable Maintenance Strategies:**
  - Simulate different maintenance approaches (reactive, preventive, or mixed strategies).
  - Evaluate the impact of maintenance strategies on overall fleet performance.
  
- **Data Tracking & Recording:**
  - Tracks vehicle usage, maintenance periods, repair costs, and replacement expenses.
  - Records operational downtime and service availability metrics.
  
- **Performance Metrics:**
  - Calculates availability of the fleet.
  - Assesses economic efficiency and reliability of components over time.

- **Simulation Analysis:**
  - Generates CSV files with detailed data from each simulation.
  - Provides a detailed breakdown of cost structures and fleet efficiency.

---

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo-url/CarsharingFleetSimulator.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the simulation script:
    ```bash
    python run_simulation.py
    ```

---

## Usage

### 1. Configure Simulation
In the `config.py` file, set your simulation parameters:
- **Strategy Selection:** Choose between reactive, preventive, or mixed maintenance strategies.
- **Vehicle Parameters:** Set vehicle usage times, maintenance intervals, and component aging models.

### 2. Run Simulation
Once configured, run the simulation. This will generate a CSV file with performance metrics and cost breakdowns for the chosen maintenance strategy.

### 3. Analyze Results
Use the generated CSV files to analyze the effectiveness of each strategy. The analysis can be done using libraries like **pandas** for data manipulation and **matplotlib** for visualization.

---

## Data Handling

- **Input Data:**
  - Defined by user configurations, including vehicle usage time, repair time, and maintenance intervals.
  
- **Generated Data:**
  - CSV files that include vehicle operation periods, maintenance costs, and fleet availability metrics.
  
- **Visualization:**
  - Use the included scripts to generate visual charts from simulation data, showcasing the economic impact of different maintenance strategies.

---

## Example

Here is an example of how to visualize data from the simulation:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the simulation data
df = pd.read_csv('simulation_output.csv')

# Plot the total maintenance cost over time
plt.plot(df['time'], df['maintenance_cost'])
plt.title('Maintenance Cost Over Time')
plt.xlabel('Time')
plt.ylabel('Cost')
plt.show()

```
## Authors
- **Oleksandr Radionenko**
- **Bohdan Stepanenko**
- **Mykhailo Dek**

