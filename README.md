# Ocular-Disease-Detection-Web-Application
### Done as a part of PDP - Project Design Practice Project

## Overview

This project aims to develop a web application using Flask for user dashboard functionality and cataract prediction. The application utilizes the Ocular Disease Detection dataset obtained from Kaggle, specifically filtering data for cataract-positive cases.

## Dataset
The dataset used in this project is the [Ocular Disease Detection dataset](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k) from Kaggle. Please refer to the dataset's documentation and terms of use for specific details.

## Prediction Model
The cataract prediction model utilized in this application can be accessed [here](https://drive.google.com/file/d/1Dtz5oYnWIpveowxbsRyG-N7ywAJTafo3/view?usp=sharing). It is crucial to place the model file in the same directory as the `app.py` file for proper functionality. If the model file is not working use VGG16.ipynb file to custom train your model and use that model for the application while doing so make sure to save the model with name vgg16_1.h5.

## Project Structure

### Directories
- `static`: Contains static files (e.g., CSS, JavaScript) utilized within the web application.
- `templates`: Consists of HTML templates defining the web interface's structure.
- `uploads`: Directory designated for uploaded files within the application.

### Files
- `app.py`: The main file containing the Flask application and server-side logic.
- `requirements.txt`: Lists all necessary dependencies and packages required for the project.
- `todo.db`: Database file utilized within the application for data storage.
- `LICENSE`: License information and terms of use for this project.
- `README.md`: This documentation file.
- `VGG16.ipynb`: Jupyter Notebook file potentially containing project-related notes, code snippets, or analysis utilizing the VGG16 model.


# Instructions for Running the Flask Application

## Prerequisites
Ensure Python is installed on your system.

## Usage
To execute the application, ensure Python is installed on your system. Install all necessary dependencies listed in `requirements.txt` using the following command:
```pip install -r requirements.txt```

## Running the Application
1. Place the model file for cataract prediction in the same directory as `app.py`.
2. Execute the Flask application by running the following command in your terminal:
   ```python app.py```

This command initializes the Flask server.

Access the application by navigating to ```http://localhost:5000``` using a web browser.

## Contributing

Contributions to this project are welcomed. If you wish to contribute, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Issues

If you encounter any issues or have suggestions for enhancements, please create a new issue in the repository's "Issues" tab.

## License

This project is licensed under the terms of the LICENSE file included in this repository.
