import requests


class OpenBreweryAPI:
    def __init__(self):
        """Initializes the base_url for OpenBreweryAPI."""
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def _error_handler(self, response):
        """Handles any error that may occur during the API request.

        Args:
            response (requests.Response): The response obtained from the API request.

        Raises:
            ConnectionError: If the status code of the response is not 200 or 201.

        Returns:
            dict: The JSON content of the response if the request was successful.
        """
        if response.status_code in (200, 201):
            return response.json()
        else:
            raise ConnectionError(f'Error: {response.status_code} - {response.text}.')

    def get_breweries(self):
        """Fetches all breweries from the OpenBreweryAPI.

        Returns:
            dict: The JSON content of the response containing all breweries.
        """
        response = requests.get(self.base_url)
        return self._error_handler(response)

    def get_brewery_by_id(self, brewery_id):
        """Fetches a specific brewery by its ID from the OpenBreweryAPI.

        Args:
            brewery_id (str): The ID of the brewery to fetch.

        Returns:
            dict: The JSON content of the response containing the brewery information.
        """
        url = f"{self.base_url}/{brewery_id}"
        response = requests.get(url)
        return self._error_handler(response)

    def search_breweries(self, query, per_page="none"):
        """Searches breweries based on a query.

        Args:
            query (str): The search term to use.
            per_page (str, optional): The number of results to return per page. Defaults to "none".

        Returns:
            dict: The JSON content of the response containing the search results.
        """
        url = f"{self.base_url}?query={query}&per_page={per_page}"
        response = requests.get(url)
        return self._error_handler(response)


if __name__ == "__main__":
    brewery_api = OpenBreweryAPI()
    print(brewery_api.get_breweries())