from pulp import *

def optimize_shipping():

    # Create Optimization Problem
    problem = LpProblem(
        "Shipping_Optimization",
        LpMinimize
    )

    # Decision Variable
    shipment_units = LpVariable(
        "shipment_units",
        lowBound=0
    )

    # Objective Function
    problem += 2500 * shipment_units

    # Constraint
    problem += shipment_units <= 100

    # Solve Problem
    problem.solve()

    # Results
    print("Optimization Status:",
          LpStatus[problem.status])

    print("Optimized Shipment Units:",
          value(shipment_units))

    print("Minimum Shipping Cost:",
          value(problem.objective))

if __name__ == "__main__":
    optimize_shipping()
