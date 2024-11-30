# SKY-SQL

# Flight Information Management System

## Description

A Python-based application for managing and querying flight information using an SQLite database. This application allows users to retrieve flight details, search for flights by various criteria, and view delayed flights. It features an interactive menu-driven interface and an API for programmatic access to flight data.

## Features

### CLI Features

- **Query Flights:**
  - Retrieve flight details by **flight ID**.
  - Search for flights departing on a specific **date**.
  - View **delayed flights** by airline or origin airport.
- **Interactive Menu:**
  - Simple text-based menu for seamless user interaction.
  - Menu options to perform queries and exit the application.
- **Data Validation:**
  - Ensures valid input for dates, flight IDs, and IATA codes.
  - Handles errors gracefully with informative messages.

### API Features

- **Endpoints:**
  - `/api/flights`: Query flight data with filters such as ID, date, airline delay, and airport delay.
- **Query Parameters:**
  - `id`: Filter flights by numeric ID.
  - `date`: Retrieve flights for a specific date (format: `DD/MM/YYYY`).
  - `airline_delay`: Retrieve delayed flights for a specific airline.
  - `airport_delay`: Retrieve delayed flights for a specific airport.
- **Rate Limiting:**
  - API calls are rate-limited to 30 requests per minute.

## Technologies Used

- **Python**:
  - SQLAlchemy for database integration
- **Flask**: Lightweight web framework for creating the API.
- **SQLite**: Lightweight database for storing flight data.
- **Flask-Limiter**: Middleware for rate-limiting API requests.

## Setup and Usage

### Prerequisites

- Python 3.7 or later
- SQLite database file

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/defPhisy/sky_sql.git
   cd sky_sql
   ```
2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On MacOS
   ```bash
   source venv/bin/activate
   ```
4. Install requirements
   ```bash
   pip install -r requirements
   ```

### Run App

#### Run CLI

  ```bash
  python main.py
  ```

#### Run API

  ```bash
  python api.py
  ```

### Example API Queries

Get Flight by ID:

```bash
http://localhost:5001/api/flights?id=123
```

Get Flights by Date:

```bash
http://localhost:5001/api/flights?date=25/12/2023
```

Get Delayed Flights by Airline:

```bash
http://localhost:5001/api/flights?airline_delay=AirlineName
```

Get Delayed Flights by Airport:

```bash
http://localhost:5001/api/flights?airport_delay=ABC
```
