# Income Survey Tool

## Overview

This project is a web-based survey tool developed using Flask for collecting and analyzing participants' data on income and expenses. The data is stored in MongoDB, processed with Python, and visualized in a Jupyter Notebook. The Flask application is deployed on AWS for easy access.

## Features

- **User Data Collection:** A simple webpage for users to input their age, gender, total income, and expenses across various categories.
- **Data Storage:** Collected data is securely stored in MongoDB.
- **Data Processing:** A Python class to fetch and save the data in a CSV file.
- **Data Visualization:** Visualizations of income and spending patterns based on the collected data.
- **Deployment:** The application is hosted on AWS, making it accessible over the internet.

## Project Structure

```plaintext
income_survey_tool/
│
├── app.py                  # Main Flask application
├── process_data.py         # Script for processing data and saving to CSV
├── templates/
│   └── index.html          # HTML template for the survey form
│── user_data.csv           # CSV file generated from MongoDB data
├── jupyter analysis.ipynb  # Jupyter Notebook for data visualization
└── README.md               # Project documentation
```

## Installation

### Prerequisites

- Python 3.6 or higher
- MongoDB
- Flask
- AWS Account (for deployment)

### Local Setup

1. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run MongoDB:**
   - Ensure MongoDB is installed and running on your local machine.

4. **Run the Flask Application:**

   ```bash
   python app.py
   ```

5. **Access the Application:**
   - Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Fill Out the Survey:**
   - Enter the required details on the survey form.
   - Submit the form to store the data in MongoDB.

2. **Process the Data:**
   - Run `process_data.py` to fetch the data from MongoDB and save it to a CSV file.

   ```bash
   python process_data.py
   ```

3. **Visualize the Data:**
   - Open the Jupyter Notebook in the `notebooks/` directory to perform data visualization.

   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```

4. **Export Visualizations:**
   - The notebook contains code to generate and save charts. The images will be saved in the `static/images/` directory.

## Deployment on AWS

1. **Launch an EC2 Instance:**
   - Create an EC2 instance with Ubuntu and SSH into the server.

2. **Install Dependencies on EC2:**

   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev nginx
   ```

3. **Upload Project Files:**
   - Use SCP or any other method to upload your project files to the EC2 instance.

4. **Run the Flask App:**
   - Install project dependencies and run the Flask application.

   ```bash
   pip install -r requirements.txt
   python app.py
   ```

5. **Configure NGINX:**
   - Configure NGINX to serve your Flask application, ensuring that the app is accessible via the public IP address of your EC2 instance.

6. **Access the Deployed Application:**
   - Visit the public IP address of your EC2 instance to access the deployed application.

## Visualizations

The project includes two primary visualizations:

1. **Ages with the Highest Income:** A bar chart displaying which age groups have the highest income.
2. **Gender Distribution Across Spending Categories:** A bar chart showing the distribution of expenses across different categories segmented by gender.

##TEST
The user.py document has test data to show how the application will turn out once data is generated.
The jupyter_analysis_test.ipynb shows a sample of the analysis and generates the visulaizations.

Both visualizations are saved as PNG files in the directory.
