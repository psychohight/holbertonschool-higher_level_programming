import requests
import csv

class APIClient:
    """A class to interact with the JSONPlaceholder API.
    """

    def __init__(self):
        """Initialize the APIClient.
        """
        self.base_url = "https://jsonplaceholder.typicode.com"

    def fetch_and_print_posts(self):
        """Fetch all posts from JSONPlaceholder and print their titles.
        """
        response = requests.get(f"{self.base_url}/posts")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])

    def fetch_and_save_posts(self):
        """Fetch all posts from JSONPlaceholder and save them to a CSV file.
        """
        response = requests.get(f"{self.base_url}/posts")
        
        if response.status_code == 200:
            posts = response.json()
            posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
            
            with open('posts.csv', 'w', newline='') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(posts_data)

if __name__ == "__main__":
    client = APIClient()
    client.fetch_and_print_posts()
    client.fetch_and_save_posts()
