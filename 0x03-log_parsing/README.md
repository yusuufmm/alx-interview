# Log Parser and Analyzer

## Overview

This project consists of two Python scripts that work together to generate and analyze HTTP access log entries.

1. **Log Generator**: Simulates HTTP access log entries.
2. **Log Analyzer**: Processes and summarizes log data from stdin.

## Scripts

### 1. Log Generator (`log_generator.py`)

Generates random HTTP access log entries with:
- Random IP addresses
- Current timestamps
- GET requests to `/projects/260`
- Various HTTP status codes
- Random response sizes

