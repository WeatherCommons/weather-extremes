# Datasets

## Units
- Temperature: °C.
- Rainfall: mm.

## Record Events
- Date, City, Lat, Lon, Country, Metric, Type, Value, Prev, Prev Date, Scope, Since
- Example 1: 2026-04-29, Bangalore, 12.97, 77.57, India, Rain, 24hrs, 111.5, 108.6, 2001-04-19, Month, 1901
- Example 2: 2026-04-26, Anantapur, 14.97, 78.57, India, Max Temp, High, 44.8, 44.7, 2024-04-29, Month, 1940
- Example 3: 2026-04-26, Anantapur, 14.97, 78.57, India, Max Temp, High, 44.8, 44.7, 2024-05-05, Year, 1940

## Structure
- data/records/YYYY/<COUNTRY>.csv contains Record Events

## All Time Records
- Month, City, Lat, Lon, Country, Metric, Type, Value, Date, Scope, Since

## Structure
- data/records/<COUNTRY>.csv contains All Time Records


# Web Page
1. Index should contain year and be able to navigate by country. Mention the units on the page before the data table
2. Ability to filter by the following columns by applying filters to one or more of these columns:
2.1 Date: By Prefix: 2026, 2026-04, 2026-04-2 , 2026-04-26.
2.2 City, Country, Metric, Type, Scope by one of enumerated values.
2.3 Value: By >=, <= 
2.4 Ability to clear all the filters with one button