# Datasets

## Units
- Temperature: °C.
- Rainfall: mm.
- Elevation: m

## Record Events
- Date, City, Lat, Lon, State, Country, Metric, Type, Value, Prev, Prev Date, Scope, Since, Elevation, WMO
- Example 1: 2026-04-29, Bangalore, 12.97, 77.57, , India, Rain, 24hrs, 111.5, 108.6, 2001-04-19, Month, 1901-01-01, 920, 43295
- Example 2: 2026-04-26, Anantapur, 14.97, 78.57, , India, Max Temp, High, 44.8, 44.7, 2024-04-29, Month, 1940-01-01, 300, 43330
- Example 3: 2026-04-26, Anantapur, 14.97, 78.57, , India, Max Temp, High, 44.8, 44.7, 2024-05-05, Year, 1940-01-01, 300, 4330

### Structure
- data/records/YYYY/<COUNTRY>.csv contains Record Events

## All Time Records
- Month, City, Lat, Lon, State, Country, Metric, Type, Value, Date, Scope, Since, Elevation, WMO
- Example 1: April, Bangalore, 12.97, 77.57, , India, Min Temp, High, 25.8, 2016-04-15, Month, 1901-01-01, 920, 43295
- Example 1: May, Bangalore, 12.97, 77.57, , India, Min Temp, High, 26.4, 2024-05-03, Month, 1901-01-01, 920, 43295
- Example 1: May, Bangalore, 12.97, 77.57, , India, Min Temp, High, 26.4, 2024-05-03, Year, 1901-01-01, 920, 43295


### Structure
- data/atr/<COUNTRY>.csv contains All Time Records


# Web Page
Display the table containing Record Events or All Records. 
- Use the following format:
1. Alternate striped tables (grey background)
2. Metric to Colour Mapping for the Entire Row's Font: 
- Max Temp: Red, Min Temp: Light Red, Rain: Dark Green, Snow: Blue, Dew Point: Purple, Max Wind: Black, Wet Bulb: Purple

1. Index should contain year and be able to navigate by country. Mention the units on the page before the data table
2. Ability to filter by the following columns by applying filters to one or more of these columns:
2.1 Date: By Prefix: 2026, 2026-04, 2026-04-2 , 2026-04-26.
2.2 City, State, Country, Metric, Type, Scope by one of enumerated values.
2.3 Ability to clear all the filters with one button