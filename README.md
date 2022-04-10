# media-organiser

Problem - no time and goodwill to spend time on organising a lot of photos/videos, stored chaotically

V1 Features:
- scans source directory for media files
- calculates MD5 hashes to find duplicates
- performs analysis of exif metadata
- copies files to new structure
  <year>
    <country>
    <unknown location>

Usage:
      python media-organiser.py <source directory> <destination directory>

For reverse geocoding I used https://api.bigdatacloud.net/ and it blocks IP address if there are a lot of requests so it may sense to use vpn to change ip address from time to time.


