# Volume Hand Control Setup Guide

This guide provides step-by-step instructions for setting up the Volume Hand Control application on a Linux system. Follow these steps to get started.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- A webcam connected to your computer

## Step 1: Clone the Repository

Clone the Volume Hand Control repository to your local machine. Open a terminal and execute:

```bash
git clone https://github.com/ruchir-k/HandTrackingOpenCV.git
cd HandTrackingOpenCV
```

## Step 2: Create a Virtual Environment

Create a virtual environment named .venv within the project directory:
```
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment by running the following command:
```
source .venv/bin/activate
```

## Step 4: Install Required Packages

Install the required Python packages using pip:
```
pip install -r requirements.txt
```

## Step 5: Run the Application

Run the Volume Hand Control application by executing the following command:
```
python VolumeHandController.py
```

### Deactivate the Virtual Environment

To deactivate the virtual environment, run the following command:
```
deactivate
```