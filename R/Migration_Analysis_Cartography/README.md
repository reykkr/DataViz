# Migration Analysis using Cartography

This project involves analyzing migration flow data and visualizing it using modern R packages. The main objective is to understand the migration patterns between different regions, including calculating metrics like total outgoing flows, net flows, and visualizing these metrics using choropleth maps.

## Files Included

- **`migration_analysis_cartography.R`**: This script performs the data analysis and visualization of migration flows using the `cartography` package.
- **`migrations.csv`**: Contains the migration flow data used in the analysis.
- **`fondcarte.shp`** (and associated files): The shapefile containing the geographical boundaries of the regions being analyzed.

## Key Libraries Used

- **`maptools`**: For handling spatial vector data.
- **`rgdal`**: For reading and manipulating spatial data files.
- **`cartography`**: For visualizing the spatial data, including creating choropleth maps.

## Key Components of the Script

1. **Data Import and Preparation**
   - The migration flow data is imported from `migrations.csv` and transformed into a matrix format.
   - The shapefile (`fondcarte.shp`) is imported to provide geographical boundaries for mapping.

2. **Flow Calculations**
   - Calculated different types of flows, including:
     - **Outgoing Flows (O)**: Total outgoing migration from each region.
     - **Incoming Flows (D)**: Total incoming migration to each region.
     - **Net Flows (S)**: Difference between incoming and outgoing flows.
     - **Asymmetry Index (A)**: The ratio of net flows to total flows, indicating flow balance.

3. **Mapping and Visualization**
   - A **choropleth map** is created using the `cartography` package to visualize outgoing flows.
   - The map includes a title, author information, and a legend to aid in interpretation.

## How to Run the Script

1. **Install Required Packages**:
   ```R
   install.packages("cartography", dependencies = TRUE)
   install.packages("rgdal")
   install.packages("maptools")
   ```

2. **Run the Script**
   - Make sure that all required files (`migrations.csv`, `fondcarte.shp`, etc.) are in the working directory.
   - Run the script in an R environment (e.g., RStudio) to generate the migration analysis and visualization.

## Output

- The script generates a **choropleth map** showing the migration patterns by region, with a focus on outgoing flows. The map provides insights into which regions have the highest and lowest migration activities.

## Notes

- The **shapefile** (`fondcarte.shp`) must include the attribute `ID` that matches the codes in the migration data (`migrations.csv`) for successful merging.
- The script has been updated to use the `cartography` package for enhanced mapping capabilities and easier customization.

## Author
- **Mohamad Ali Ghaddar**

Feel free to customize this script and adapt it for other migration datasets or similar spatial analyses.