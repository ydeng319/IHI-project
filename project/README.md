# 2017 Bird Flu Transmission Path Research Project

📺 **Youtube Link to presentation:** [https://youtu.be/Dps7X53fx6g]

---
## project structure
```bash
project/
├── app.py                     # Streamlit app entry point
├── Dockerfile                 # Docker configuration
├── README.md                  # Project documentation
├── Outbreak_240817.csv     # Raw data file

 ```bash

### Application Test Steps


| **Test Step**                    | **Test Data**                                                                                                           | **Test Result**                                                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Landing page**                | Users can click on the app link to access the app default page. <br> App link: [http://3.141.42.112:8501/](http://3.141.42.112:8501/) | On the app landing page, users see a world map showing all bird flu cases, key metrics, and total case count.                                                |
| **Left panel**                  | Click the triangle icon on the upper left to expand filter panel.                                                      | Users see the left panel with 2 filter options: **country** and **date picker**.                                                                              |
| **Filter by country**           | Select "United States" from the country dropdown.<br> Click “Filter Map and Summarize Data”.                            | Map filters to US data only. Case count updates to **6488**.<br>AI summary generated for displayed data.                                                      |
| **Filter by date**              | Select start date: **2016-01-01**<br> Select end date: **2016-12-31**<br> Click “Filter Map and Summarize Data”.         | Map filters to US data for 2016. Case count updates to **15**.<br>AI summary generated for displayed data.                                                    |
| **Zoom map**                    | Hover over map and scroll mouse wheel.                                                                                 | Map zooms in and out accordingly.                                                                                                                              |
| **Export data**                 | Click the “Export data” button under the map.                                                                          | Filtered new cases data is downloaded as a CSV file.                                                                                                          |

