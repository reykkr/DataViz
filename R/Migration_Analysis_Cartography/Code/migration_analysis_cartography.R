rm(list=ls())

# Install and load required packages
# Uncomment the installation lines if you haven't installed the packages yet
# install.packages("cartography", dependencies = TRUE)
# install.packages("rgdal")
# install.packages("maptools")

# Packages
library(reshape2)
library(maptools)   # Spatial vector data
library(rgdal)      # Geospatial Data Abstraction Library for spatial data
library(cartography)  # Modern package for creating maps

# Importation and transformation of a migration matrix
# Loading the migration data
tab <- read.table("migrations.csv",
                  header=TRUE,
                  sep=";",
                  stringsAsFactors=FALSE,
                  encoding="UTF-8")
str(tab)
tab

# Converting data frame to matrix
mat <- as.matrix(tab[,-1])
row.names(mat) <- tab[,1]
mat

# Original flows (Fij)
Fij <- mat
# Slice to see the first few rows and columns
Fij[1:3,1:3]

# Transpose of flows (Fji)
Fji <- t(mat)
# Slice to see the first few rows and columns
Fji[1:3,1:3]

# Total flows (Fvij = Fij + Fji)
Fvij <- Fij + Fji
# Slicing
Fvij[1:3,1:3]

# Net flows (Fsij = Fij - Fji)
Fsij <- Fij - Fji
# Slicing
Fsij[1:3,1:3]

# Calculate metrics for each region
O <- apply(Fij, 1, sum)  # Total outgoing flows for each region (sum rows)
D <- apply(Fij, 2, sum)  # Total incoming flows for each region (sum columns)
V <- O + D               # Total flows (incoming + outgoing)
S <- D - O               # Net difference (incoming - outgoing)
A <- round(S/V, 2)       # Asymmetry index (rounded to two decimals)

# Create a data frame with calculated parameters
param <- data.frame(cbind(O, D, V, S, A))
param$CODE <- row.names(param)
param

# Importing shapefile for mapping
carte <- "fondcarte.shp"
fdc <- readOGR(carte)

# Display attribute data of the shapefile
head(fdc@data)

# Merge the migration parameters with the spatial data
fdc@data <- merge(fdc@data, param, by.x = "ID", by.y = "CODE", all.x = TRUE)

# Plotting the map with cartography
# Basic plot of the shapefile
plot(fdc, col = "lightgrey", border = "darkgrey")

# Adding a choropleth layer to visualize outgoing flows (O)
choroLayer(spdf = fdc, 
           df = fdc@data, 
           var = "O", 
           legend.pos = "bottomleft",
           legend.title.txt = "Total Outgoing Flows",
           method = "quantile",
           nclass = 5,
           col = carto.pal(pal1 = "blue.pal", n1 = 5),
           border = "white",
           lwd = 0.5,
           add = TRUE)

# Adding title and layout
layoutLayer(title = "Migration Flows by Region",
            author = "Your Name", 
            sources = "Source: Migration Dataset",
            frame = TRUE, 
            col = "black", 
            scale = 5e5)
