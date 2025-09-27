# Consumer Shopping Behavior Analysis Dashboard

## Introduction
This project is a Power BI dashboard that visualizes consumer shopping behavior, including key purchase metrics, demographic insights, and product trends. The dashboard helps businesses understand revenue drivers, customer segments, and purchasing patterns to make data-driven decisions and optimize marketing strategies.

## Project Type
Analytics | Visualization | Dashboard

## Directory Structure

```
consumer-shopping-behavior-dashboard/
├─ dataset/
│  ├─ Consumer_Shopping_Behavior_dataset.csv      
├─ reports/
│  ├─ Consumer_Shopping_Behavior.pbix   
├─ screenshots/
│  ├─ dashboard_overview.png             
│  ├─ kpi_section.png                   
│  ├─ visuals_analysis.png              
├─ README.md                          
```

## Video Walkthrough of the project
Attach a short video walkthrough (1-3 minutes) demonstrating dashboard features, filters, and key insights.

## Video Walkthrough of the codebase
Attach a short video (1-5 minutes) explaining the Power BI data model, measures (DAX), and dashboard structure.

## Features
- Interactive KPI cards for revenue, average purchase, customer count, review ratings, and subscription revenue.
- Visual breakdowns by category, gender, age, season, location, and discount status.
- Dynamic filters (slicers) for Age, Season, Location, and Discount Applied.
- Geographic visualization of purchase amounts by U.S. states.
- Comparative analysis of discounted vs non-discounted purchases.

## Design decisions or assumptions
- Used DAX measures for key KPIs and calculations.
- Assumed clean and well-structured raw data.
- Focused on consumer shopping within the U.S. market.
- Dashboard designed for business analysts and retail managers.
- Color palette and layout optimized for readability and insight extraction.

## Installation & Getting started
To view or modify the dashboard:

1. Clone the repository:
    ```bash
    git clone https://github.com/Ashish0016op/consumer-shopping-behavior-dashboard.git
    ```
2. Open `Consumer_Shopping_Behavior.pbix` in Power BI Desktop.
3. Replace or update the dataset in `/dataset/consumer_shopping_data.csv` if needed.

## Usage
- Open the PBIX file in Power BI Desktop.
- Use the slicers to filter data by age, season, location and discount.
- Export insights as PDF or to Power BI Service.

Include screenshots:
![Dashboard Overview](screenshots/dashboard_overview.png)
![KPI Section](screenshots/kpi_section.png)
![Visuals Analysis](screenshots/visuals_analysis.png)

## Technology Stack
- Power BI Desktop
- DAX (Data Analysis Expressions)
- CSV for dataset


