# Pixela Habit Tracker

This Python script interacts with the Pixela API to track a specific habit (in this case, "Programming"). It allows you to:

* **Create a Pixela User:** (Commented out in the current version) Registers a new user on the Pixela platform. You'll need to provide a unique username and a token.
* **Create a Pixela Graph:** (Implicit in the pixel creation) Defines a graph on your Pixela account to visualize your habit tracking data. The graph is configured with an ID, name, unit (minutes), type (integer), and color.
* **Add Data to the Graph:** Records the quantity of your habit performed on a specific date. The script automatically uses the current date when adding data.

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **`requests` library:** This script uses the `requests` library to make HTTP requests to the Pixela API. You can install it using pip:

    ```bash
    pip install requests
    ```

### Setup

1.  **Obtain a Pixela Token:**
    * Visit the [Pixela website](https://pixe.la/).
    * Sign up for an account.
    * Follow the instructions to generate your unique token.

2.  **Set Your Credentials:**
    * Open the `main.py` file.
    * Replace the empty string assigned to the `TOKEN` variable with your Pixela token:

        ```python
        TOKEN = "YOUR_PIXELA_TOKEN"
        ```
    * Ensure the `USER_NAME` variable is set to your Pixela username:

        ```python
        USER_NAME = "your_pixela_username"
        ```

3.  **Configure the Graph (Optional - First Run):**
    * The script currently attempts to post data to a graph with the ID `"graph2"`. If you haven't already created a graph with this ID, you might need to uncomment the section for creating the graph on your first run.
    * Modify the `graph_config` dictionary if you want to customize the graph ID, name, unit, type, or color:

        ```python
        graph_config = {
            "id": "your-preferred-graph-id",
            "name": "Your Habit Graph Name",
            "unit": "e.g., hours, steps, pages",
            "type": "int",  # or "float"
            "color": "shibafu"  # Choose from: green, red, blue, yellow, purple, black, momiji, sora
        }

        # Uncomment the following lines for the first run to create the graph:
        # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        # print(response.text)
        ```
    * **Important:** Once the graph is created, you can comment out the graph creation part to avoid accidentally trying to create it again on subsequent runs (which will result in an error if a graph with the same ID already exists).

### Running the Script

1.  **Open a terminal or command prompt.**
2.  **Navigate to the directory** where you saved the `main.py` file.
3.  **Run the script:**

    ```bash
    python main.py
    ```

    The script will:
    * Get the current date.
    * Attempt to post data (defaulting to "120" minutes) to your Pixela graph with the ID `"graph2"` for the current date.
    * Print the API response, indicating whether the data was successfully added.

## Usage

* **Automatic Date Tracking:** The script automatically uses the current date when posting data.
* **Customizing Quantity:** To track a different amount of time (or any other unit you've configured), modify the `quantity` value in the `pixel_params` dictionary:

    ```python
    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "your_habit_quantity"
    }
    ```

* **Running Regularly:** You can schedule this script to run daily (or at other intervals) using task schedulers (like cron on Linux/macOS or Task Scheduler on Windows) to automatically update your Pixela habit tracker.

## Contributing

Contributions to enhance this script are welcome. You can suggest improvements or submit pull requests.

## License

This project is provided as is and is intended for personal use with the Pixela API. Refer to the Pixela API's terms of service for usage guidelines.
```