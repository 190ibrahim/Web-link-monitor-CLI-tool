# Web Link Monitor CLI Tool

The tool will continuously monitor the specified URLs at the given intervals and display the reachability status for each URL. The output will show the date and time of each check along with the URL and its reachability status, and it provides unambiguous error messages in case of failures.

### Installation:
Before running the Web Link Monitor CLI Tool, ensure you have Python and the required packages installed. 
You can install the necessary packages using the following command: `python -m pip install requests pyyaml pytz
`

### Usage:
You can add urls to the config.yaml file like following format:

```
monitorInterval: <interval_in_seconds>
urls:
 - <url1>
 - <url2>
 ...
```

`monitorInterval`: The time interval (in seconds) between consecutive scans of the URLs.

`urls`: A list of URLs that you want to monitor for reachability.

To run the Web Link Monitor CLI Tool, use the following command: `python web_link_monitor.py
` 
