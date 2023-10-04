# Grondwaterpeil 
Basic script to plot groundwater levels from the Dutch groundwater network. Based on the Grondwatertools website.

## Usage 
The script works with Python, and requires pyproj (`pip install pyproj`) to convert the Rijkswaterstaat coordinates to WGS84 (which is way easier to plot on a map). The data is downloaded from the [Grondwatertools website](https://www.grondwatertools.nl/metran-service/api/zip/features), and the original data is in a geojson format. The data in this geojson is only the basic data, such as the coordinates and 15/25 year trends. 

The converted csv is included in the repo. It was downloaded and converted on the 4th of October 2023.

## What are these data points?
Each row in the csv represents a measuring well/pipe where the groundwater level is measured. These pipes can have multiple filters which are used to measure the groundwater level. The filters are numbered.NB: The script only downloads the first five filters per location. For each point, the location and the NAP height of the maaiveld (ground level) is also given. Each point in this dataset includes the 15 year and 25 year trend, which is measured respectively between 2005-2020 and between 1995-2020.

## Possible improvements / additional data
If you want more specific data per well, you can scrape these from the website as well, using the endpoints with the well ID and filter id, such as https://www.grondwatertools.nl/metrandata/getloc?wellid=B45A0309&screenid=001. This gives you time series with all of the measured data points. With those data, you can make very concise visualisations [like the NYT one](https://www.nytimes.com/interactive/2023/08/28/climate/groundwater-drying-climate-change.html). 