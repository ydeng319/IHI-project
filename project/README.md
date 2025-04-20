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

### Architecture Diagram
The architecture diagram of this project is shown in Figure 1. The breakdown of the components and their relationships include:

User: Represents the end user who interacts with the system to visualize the bird flu spread trend
Web App: A web application that serves as the interface for the user. It's where the user views and interacts with the data visualizations. The web app is built using streamlit.
Cloud Server: Hosts the web application and manages the data flow between the web app and the GitHub repository.
GitHub Repo: Stores the application's code and possibly the bird flu data or scripts to fetch the data. It acts as a version control system and can also be part of the deployment pipeline.
Data Visualization: A python script for the date preprocessing and visualization pipeline, along with a web app, built using Streamlit, dedicated to visualizing the bird flu data effectively.
Bird Flu Data: The dataset that is used by the Streamlit component to create visualizations. It’s stored in a database or a similar data storage solution (e.g. csv file) accessible by the web app.
For an user accesses the web app hosted on a cloud server, which retrieves data visualizations powered by Streamlit from the bird flu data, and all updates or application code are managed through a GitHub repository.

![App Overview](images/diagram.png)


### Application Test Steps


| **Test Step**                    | **Test Data**                                                                                                           | **Test Result**                                                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Landing page**                | Users can click on the app link to access the app default page. <br> App link: [http://3.141.42.112:8501/](http://3.141.42.112:8501/) | On the app landing page, users see a world map showing all bird flu cases, key metrics, and total case count.                                                |
| **Left panel**                  | Click the triangle icon on the upper left to expand filter panel.                                                      | Users see the left panel with 2 filter options: **country** and **date picker**.                                                                              |
| **Filter by country**           | Select "United States" from the country dropdown.<br> Click “Filter Map and Summarize Data”.                            | Map filters to US data only. Case count updates to **6488**.<br>AI summary generated for displayed data.                                                      |
| **Filter by date**              | Select start date: **2016-01-01**<br> Select end date: **2016-12-31**<br> Click “Filter Map and Summarize Data”.         | Map filters to US data for 2016. Case count updates to **15**.<br>AI summary generated for displayed data.                                                    |
| **Zoom map**                    | Hover over map and scroll mouse wheel.                                                                                 | Map zooms in and out accordingly.                                                                                                                              |
| **Export data**                 | Click the “Export data” button under the map.                                                                          | Filtered new cases data is downloaded as a CSV file.                                                                                                          |

### 
