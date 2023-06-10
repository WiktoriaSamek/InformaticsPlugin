# QGIS InformaticsPlugin
The plugin is used for counting selected points, displaying coordinates of selected points, calculating height differences between 2 points, and calculating the area of a polygon formed by points using the Gauss method, as well as displaying their coordinate system (+ zones).

## Minimum hardware requirements:
- Windows 10  
- Qgis: 3.28.4

## Plugin Work Description:
1.The user selects points accordingly for calculating height differences or area. <br/>
2. Then, the user opens the plugin and clicks the appropriate button for the desired action.
```sh
count
```
```sh
show coordinates
```
```sh
calculate
```
```sh
height
```
3. The result is displayed above the button.

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
To ensure proper functioning of the plugin, you need to either import a .csv file similar to the one provided above into QGIS or use any other method to ensure that the attribute table contains columns with the following names:
```sh
Nr X Y H
```
and that the values in these columns are floating-point numbers.
