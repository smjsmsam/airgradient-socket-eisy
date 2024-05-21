
# AirGradient Node Server

A simple node server for connection to the AirGradient air quality sensor using socket connection to the AirGradient's arduino.

## Installation


### Node Settings
The settings for this node are:

#### Short Poll
   * How often to increment the API request

#### Token
   * Client token, which can be found on the AirGradient dashboard.

#### Index
   * Based on the order of AirGradient devices on client account, 0-indexed.

#### Port
   * Sets port number for communication with AirGradient, any number between 1024 and 49151.   


## Requirements

1. Polyglot V3.
2. ISY firmware 5.3.x or later

# Release Notes

- 1.0.0 05/20/2024
   - Initial version published to github
