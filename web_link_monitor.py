import os
import time
import datetime
import requests
import yaml
import pytz


# Loading the configuration from the YAML file
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


# Checking the reachability of a URL
def check_url_reachability(url):
    try:
        # Sending a HEAD request to the URL with a timeout of 10 seconds
        response = requests.head(url, timeout=10)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return "REACHABLE"
    except requests.ConnectionError as e:
        # Handle ConnectionError, typically raised when a connection cannot be established
        return f"UNREACHABLE (ConnectionError: {e})"
    except requests.Timeout as e:
        # Handle Timeout, raised when the request times out
        return "UNREACHABLE (Request Timeout)"
    except requests.RequestException as e:
        # Handle other RequestExceptions
        return f"UNREACHABLE (Request Exception: {e})"


def monitor_urls(config):
    while True:
        # Including the datetime with the specified time zone
        local_timezone = pytz.timezone('Europe/Budapest')
        local_time = datetime.datetime.now(local_timezone)
        timestamp = local_time.strftime('%a %d %b %Y %I:%M:%S %p %Z')
        for url in config['urls']:
            reachability = check_url_reachability(url)
            print(f"{timestamp}, {url}, {reachability}")

        # Waiting for the specified monitorInterval before the next round of monitoring
        time.sleep(config['monitorInterval'])


if __name__ == "__main__":
    config_file = "config.yaml"
    if not os.path.exists(config_file):
        print(f"Error: Config file '{config_file}' not found.")
    else:
        config = load_config(config_file)
        monitor_urls(config)
