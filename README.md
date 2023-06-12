# QGIS InformaticsPlugin

The QGIS InformaticsPlugin is a plugin designed for performing various geospatial calculations and operations. It provides functionalities such as counting selected points, displaying coordinates of selected points, calculating height differences between two points, and calculating the area of a polygon formed by points using the Gauss method. It also displays the coordinate system and zone information.

## Minimum Requirements

To use the QGIS InformaticsPlugin, make sure you have the following minimum hardware and software requirements:

- Operating System: Windows 10
- QGIS Version: 3.28.4

## Plugin Functionality

The QGIS InformaticsPlugin offers the following functionalities:

### 1. Count Objects

The "Count Objects" feature allows the user to count the number of selected points. To use this feature, follow these steps:
1. Select the points on the map.
2. Open the plugin, select "General" and click the "Count" button.
3. The plugin will display the number of selected points.

### 2. Show Coordinates

The "Show Coordinates" feature displays the coordinates of the selected points. To use this feature, follow these steps:
1. Select the points on the map.
2. Open the plugin, select "Description" and click the "Show Coordinates" button.
3. The plugin will display the coordinates of the selected points.

### 3. Calculate Area

The "Calculate Area" feature calculates the area of a polygon formed by the selected points using the Gauss method. To use this feature, follow these steps:
1. Select the points that form a closed polygon.
2. Open the plugin, select "Area" and click the "Calculate" button.
3. The plugin will display the calculated area of the polygon in the user-selected units, the coordinate system (+zone) and create new layer for that polygon.

### 4. Calculate Height Difference

The "Calculate Height Difference" feature calculates the height difference between two selected points. To use this feature, follow these steps:
1. Select two points on the map.
2. Open the plugi, select "Elevation" and click the "Height" button.
3. The plugin will display the calculated height difference between the two points.

## Additional comments:
If the file contains layers with points in different coordinate systems, before selecting specific points, user should select the respective layer on the left side of the window.
Close button also clear all calculations, unlike "x" button, which only close a calculation's window without deleting newcome informations (layers etc.).

## Possible Errors:
If the user does not select a point or selects too few points for a specific calculation, an error will appear:
```sh
Not enough points selected
```
If the user selects too many points, they will see the following message:
```sh
Too many points were selected
```

## Technical Notes:
-The "Clear All" option deletes all calculations and newly created temporary layers.
-To ensure proper functioning of the plugin, you need to either import a .csv file similar to the one provided above into QGIS or use any other method to ensure that the attribute table contains columns with the following names:
```sh
Nr X[m] Y[m] H[m]
```
To add an input file, you need to use option: layer -> add a layer -> add a CSV text layer.
Input file needs to look like this one:
```sh
nr;X;Y;H
1;352600;672600;198,34
2;352600;672700;197,49
3;352600;672800;199,61
4;352700;672500;185,96
```
The input file should be formatted similar to the example provided above, with the column names in the first row and the corresponding values in subsequent rows. The values in the columns should be floating-point numbers.

For any technical issues or further information, please refer to the plugin documentation or contact the plugin developers.
