# Helmet Detection Model

This project is a helmet detection system built using the YOLO (You Only Look Once) object detection model. It is designed to detect whether a person is wearing a helmet or not, aiming to promote safety and compliance in various scenarios such as road traffic monitoring or workplace safety inspections.

## Features
- **Real-Time Detection**: Accurately detects helmets on individuals in real-time from live video feeds or uploaded media.
- **YOLO Model**: Utilizes the YOLO architecture for fast and efficient object detection.
- **Interactive Web Interface**: A user-friendly frontend where it uses real time detection ie uses webcam for the detection.

## How the Project Was Built
### 1. Model Training
- The detection model is built using the YOLO architecture, a popular framework for real-time object detection.
- The training dataset included labeled images of individuals with and without helmets, ensuring the model is robust across various scenarios.
- Training, evaluation, and testing were performed in a Jupyter Notebook, and the notebook has been uploaded to my **Machine Learning Repository** for reference.

### 2. Web Interface
- The backend was developed using Flask to integrate the YOLO model and enable easy interaction with users.
- The frontend (webpage) was generated with the help of AI, resulting in a clean and functional user experience.
- The web application processes live video feeds in real-time to detect and highlight helmet usage or non-compliance.

## Repository Contents
- **Notebook**: The Jupyter Notebook used for training and testing the YOLO model is available in my Machine Learning Repository.
- **Web Interface Code**: The AI-generated script for the frontend, along with Flask integration, is included in this repository.

## How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the Flask application to start the web server.
4. Access the web interface in your browser, where you can connect a live video feed.
5. View the real-time detection results with highlighted helmets or non-helmet areas.

## Applications
- **Traffic Monitoring**: Detect helmet compliance among motorcyclists.
- **Workplace Safety**: Ensure employees are wearing helmets in construction sites or industrial zones.
- **Event Security**: Monitor helmet usage in public events or sporting activities.

## Acknowledgments
- **YOLO Framework**: For providing a state-of-the-art object detection architecture.
- **OpenAI**: For assisting with the generation of the web interface and deployment scripts.

Feel free to explore this repository, test the system, and use it as a base for your own projects aimed at improving safety and compliance!

