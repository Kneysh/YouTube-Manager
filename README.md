# Youtube Manager

A simple Python CLI application for managing a list of YouTube videos. The app allows users to list, add, update, and delete video details which are stored in a JSON file.

## Features

- List all videos with title and duration
- Add new videos
- Update existing video details
- Delete videos

## File Structure

- **[youtube_manager.py](youtube_manager.py)** – Main application script that provides the CLI.
- **[Video_Details.txt](Video_Details.txt)** – JSON file that stores video details.

## Prerequisites

- Python 3.x installed on your machine.
- Install dependencies using [pip](https://pip.pypa.io/en/stable/). The app uses the `python-dotenv` library to load environment variables.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Kneysh/YouTube-Manager.git
    cd YouTube-Manager
    ```

2. Install the required dependencies:
    ```sh
    pip install python-dotenv
    ```

## Running the Application

Run the main script:
```sh
python youtube_manager.py