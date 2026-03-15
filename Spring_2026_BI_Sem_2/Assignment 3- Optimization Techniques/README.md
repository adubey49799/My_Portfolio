### Step 28: Summary of findings

The linear programming model minimized transportation cost and produced an optimal shipment plan with a total transportation cost of **$581,736.30**.

The exact facility-location analysis showed that the best warehouse configuration was **Atlanta, Dallas, Harrisburg, and Kansas City**, with a total cost of **$603,114.80** including fixed warehouse opening costs.

The heuristic approach produced a feasible but more expensive solution, with a total cost of **$668,839.60**, which was **10.9% higher** than the exact facility-location solution.

The gradient-based model produced a shipment allocation with transportation cost very close to the LP solution. Although the solver did not fully converge, the transportation component differed from the LP result by only **$103.15**, indicating that improved load balancing can be achieved with almost no increase in transportation cost.

Sensitivity analysis showed that the optimal network was more sensitive to demand growth and reduced Atlanta capacity than to a moderate increase in transportation cost. In both the **Demand +10%** and **Atlanta capacity -20%** scenarios, the model selected all five warehouses.

## Approach
The assignment was completed in a step-by-step optimization workflow:

1. A regional supply chain dataset was constructed using candidate warehouses and customer demand locations.
2. Route distances were calculated using latitude and longitude coordinates.
3. Transportation cost per unit was estimated from route distance.
4. A feasibility matrix was created to exclude routes that violated the delivery-distance constraint.
5. A linear programming transportation model was solved to minimize transportation cost.
6. A facility-location analysis was performed by testing feasible warehouse combinations and adding fixed warehouse opening costs.
7. A greedy heuristic solution was developed and compared with the exact facility-location result.
8. A gradient-based continuous optimization model was used to study shipment balancing across warehouses.
9. Sensitivity analysis was performed for demand growth, transport cost increase, and warehouse capacity reduction.

## Key Results

### Linear Programming (LP)
The linear programming transportation model produced an optimal transportation cost of **$581,736.30**.

### Exact Facility-Location Solution
The best warehouse configuration was:

- Atlanta
- Dallas
- Harrisburg
- Kansas City

This configuration produced:
- Transportation cost: **$583,714.80**
- Fixed warehouse cost: **$19,400.00**
- Total cost: **$603,114.80**

### Heuristic Solution
The heuristic approach selected:
- Atlanta
- Chicago
- Dallas

This configuration produced:
- Transportation cost: **$653,539.60**
- Fixed warehouse cost: **$15,300.00**
- Total cost: **$668,839.60**

The heuristic solution was **$65,724.80** more expensive than the exact facility-location solution, which is about **10.9% higher**.

### Gradient-Based Solution
The gradient-based model produced:
- Penalized objective value: **$583,244.51**
- Transportation component: **$581,839.45**

Although the solver did not report full convergence, the transportation cost was only **$103.15** higher than the LP transportation cost, showing that more balanced warehouse utilization can be achieved with almost no increase in transportation cost.

### Sensitivity Analysis
Sensitivity analysis showed:

- **Base case:** Atlanta, Dallas, Harrisburg, Kansas City — **$603,114.80**
- **Demand +10%:** All five warehouses open — **$675,028.23**
- **Transport cost +15%:** Atlanta, Dallas, Harrisburg, Kansas City — **$690,672.02**
- **Atlanta capacity -20%:** All five warehouses open — **$627,372.90**

## Conclusion
This assignment demonstrated how optimization techniques can be applied to regional supply chain network design. The linear programming model provided the lowest transportation-cost shipment plan, while the exact facility-location analysis identified the most cost-effective warehouse network after including fixed warehouse opening costs. The heuristic model produced a feasible but more expensive solution, and the gradient-based model showed that shipment balancing can be improved with negligible transportation-cost increase. Sensitivity analysis further showed that the network is more sensitive to demand growth and warehouse capacity reduction than to moderate transportation-cost inflation.

## References
- United States Census Bureau. https://data.census.gov/table
- Bureau of Transportation Statistics. https://www.bts.gov/topics/freight-transportation