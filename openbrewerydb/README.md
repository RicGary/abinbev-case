## Overview

The class `OpenBreweryAPI` provides an interface for interacting with the OpenBrewery API. The class allows users to fetch information about breweries, including retrieving all breweries, getting details for a specific brewery by its ID, and searching for breweries based on a query.

## Class: OpenBreweryAPI

### Initialization

- The `__init__` method initializes the class with the base URL for the OpenBrewery API, setting up the endpoint for making requests.

### Methods

1. **_error_handler(response)**

- Handles responses from API requests.
- Checks the status code of the response and raises an error if the request was unsuccessful.
- If successful, it returns the JSON content of the response.

2. **get_breweries()**

- Fetches a list of all breweries from the OpenBrewery API.
- Returns the JSON content containing details of all breweries.

3. **get_brewery_by_id(brewery_id)**

- Retrieves information about a specific brewery identified by its ID.
- Returns the JSON content with the requested brewery's details.

4. **search_breweries(query, per_page="none")**

- Searches for breweries based on a given query.
- Optionally allows specifying the number of results to return per page.
- Returns the JSON content containing the search results.

### Example Usage

The code includes a main block that creates an instance of the `OpenBreweryAPI` class and prints the list of all breweries by calling the `get_breweries()` method.