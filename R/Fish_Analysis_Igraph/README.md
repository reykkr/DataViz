# Fish Network Analysis using igraph

This project involves analyzing a fish network using the `igraph` package in R. The main objective is to understand the structure of the fish trade network, identify influential nodes, and visualize changes in the network after removing specific connections.

## Files Included

- **`fish_network_analysis.R`**: This script performs the analysis and visualization of the fish trade network using the `igraph` package.
- **`fish.txt`**: Contains the fish network data used in the analysis.

## Key Libraries Used

- **`igraph`**: For analyzing and visualizing network structures.

## Key Components of the Script

1. **Data Import and Preparation**
   - The fish network data is imported from `fish.txt` and converted into a graph object.

2. **Network Analysis**
   - **Original Network**: The initial fish network is plotted to visualize the complete structure.
   - **Filtered Network**: Edges with weights (`poidsqte`) below a threshold (3000) are removed to create a refined network.
   - **Node Removal**: Nodes with a degree of less than 1 are removed to further refine the network.

3. **Network Metrics**
   - Various metrics are calculated to understand the network, including:
     - **Order and Size**: Number of nodes (`gorder`) and edges (`gsize`).
     - **Edge Density**: Density of the network.
     - **Degree**: Average degree of nodes.
     - **Diameter**: Longest shortest path in the network.
     - **Transitivity**: Global clustering coefficient.
     - **Mean Distance**: Average path length between nodes.
     - **Degree Distribution**: Degree of each node.

4. **Community Detection**
   - Communities within the network are detected using different clustering methods:
     - **Edge Betweenness**: Finds communities by progressively removing edges with the highest betweenness.
     - **Fast Greedy**: Optimizes modularity to find communities.

## How to Run the Script

1. **Install Required Packages**:
   ```R
   install.packages("igraph")
   ```

2. **Run the Script**
   - Make sure that the required file (`fish.txt`) is in the working directory.
   - Run the script in an R environment (e.g., RStudio) to perform the network analysis and visualization.

## Output

- The script generates multiple visualizations of the fish network, including the original, filtered, and refined versions. It also calculates various metrics that provide insights into the structure and characteristics of the network.

## Notes

- The **fish.txt** file must be properly formatted with headers and appropriate delimiters for successful import.
- The filtering and community detection steps help in understanding the important nodes and groups within the fish network.

## Author
- **Mohamad Ali Ghaddar**

Feel free to customize this script and adapt it for other network datasets or similar analyses.
