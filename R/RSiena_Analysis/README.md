# RSiena Analysis

This folder contains R scripts that perform Social Network Analysis (SNA) on a longitudinal dataset using the RSiena package. The analysis focuses on network evolution over three time periods and examines how individual behaviors like alcohol consumption change in response to the social network.

## Files Included

- **`siena_1.R`**: 
  - **Description**: Analyzes the evolution of friendship networks across three time points. This script also includes individual covariates such as smoking and alcohol use to understand their influence on network changes.
  - **Focus**: Network evolution and structural effects.

- **`siena_TP_enonce.r`**: 
  - **Description**: Extends the analysis by modeling individual behavior over time. Alcohol consumption is treated as a dependent behavior, and the script explores how friendships and individual attributes affect this behavior.
  - **Focus**: Behavioral dynamics and network influence.

## Key Libraries Used

- **`RSiena`**: For analyzing social network dynamics over time, including modeling changes in relationships and individual behaviors.
- **`network`** and **`sna`**: For creating and visualizing social network graphs.

## Key Components of the Scripts

1. **Data Import and Preparation**
   - The friendship network data is imported from three different time points and converted into a `sienaNet` object.
   - Attributes like alcohol consumption and smoking behavior are imported as covariates to be used in the analysis.

2. **Model Specification and Effects**
   - **Network Effects**: Includes effects like transitive triplets and reciprocity to model the structural evolution of the network.
   - **Behavioral Effects**: Alcohol consumption is modeled as a dependent behavior, influenced by both network structure and individual attributes.

3. **Estimation and Results**
   - The model is estimated using the `siena07` function, which calculates parameter estimates for the specified effects.
   - Outputs are generated to summarize the effects and their significance.

## How to Run the Scripts

1. **Install Required Packages**:
   ```R
   install.packages("RSiena")
   install.packages("network")
   install.packages("sna")
   ```

2. **Run the Scripts**
   - Make sure that all required data files (`s50-1.dat`, `s50-alcohol.dat`, etc.) are in the working directory.
   - Run the scripts in an R environment (e.g., RStudio) to perform the network analysis and behavior modeling.

## Output

- The scripts generate parameter estimates for network and behavioral effects, providing insights into how friendships evolve and how individual behaviors are influenced by the network structure.

## Notes

- The **data files** (`s50-1.dat`, `s50-alcohol.dat`, etc.) must be available in the working directory for the scripts to run successfully.
- The analysis uses both **structural network effects** and **individual-level covariates** to provide a comprehensive view of network and behavioral dynamics.

## Author
- **Mohamad Ali Ghaddar**

Feel free to customize these scripts and adapt them for other social network datasets or similar longitudinal analyses.
