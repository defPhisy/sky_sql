# SKY-SQL

## Description

A Python-based cli application for managing and querying flight information using an SQLite database. This application allows users to retrieve flight details, search for flights by various criteria, and view delayed flights. The application features an interactive menu-driven interface and integrates with SQLAlchemy for database operations.

## Features

- **Query Flights:**
  - Retrieve flight details by **flight ID**.
  - Search for flights departing on a specific **date**.
  - View **delayed flights** by airline or origin airport.
- **Interactive Menu:**
  - Simple text-based menu for seamless user interaction.
  - Menu options to perform queries and exit the application.

### Example Queries

1. **Show Flights by Date:** Enter the date in `DD/MM/YYYY` format when prompted. \_ View all flights departing on that date.
2. **Delayed Flights by Airline:** Enter the airline name when prompted. \_ View all delayed flights for the specified airline.
3. **Flight Details by ID:** Enter a numeric flight ID. Retrieve detailed information about the flight.

## Technologies Used

- **Python**:
  - SQLAlchemy for database integration
- **SQLite**: Lightweight database for storing flight data

## Setup and Usage

### Prerequisites

- Python 3.7 or later

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/defPhisy/sky_sql.git
   cd flight-management-system
   ```
