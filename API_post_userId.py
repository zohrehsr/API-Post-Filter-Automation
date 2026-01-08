import requests
import csv
import os
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code !=200 :
            print(f"Error: API returned status code {response.status_code}")
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error : {e}") 
        return None

def load_user_ids(file_path):
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found. make sure it's in the same folder as this script.")
        return
    
    user_ids = []

    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if not row:
                 continue
            try:
                user_ids.append(int(row[0]))
            except ValueError :
                print(f"Invalid User Id Skipped : {row}")
    return user_ids

def analyze_posts(posts, user_ids):
    filtered = [post for post in posts if post["userId"] in user_ids]
    titles = [post["title"] for post in filtered]
    return filtered, titles

def main():
    try:
        file_path = input("Enter the CSV file name (e.g., new_data.csv): ")
        output_file = input("Enter output file name: ")
        output_format = input("Choose output format (csv/json): ").lower()

        posts = fetch_posts(API_URL)
        if posts is None:
            print("No posts to analyze.")
            return None
        
        user_ids = load_user_ids(file_path)
        if not user_ids:
            print("No valid user IDs found.")
            return
        
        filtered, titles = analyze_posts(posts, user_ids)  

        if output_format == "json" :
             with open(output_file,"w", encoding="utf-8") as f:
                  json.dump(filtered, f, indent=4)


        elif output_format == "csv":
            with open(output_file, 'w', encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["userId", "id", "title", "body"])
                for post in filtered:
                     writer.writerow([post["userId"], post["id"], post["title"], post["body"]]) 

        else:
             print("Invalid format selected!")  

        print("Automation completed successfully.")

        print(f"{len(posts)} items fetched from API")
        print(f"{len(filtered)} items matched user IDs")
        print(f"{len(posts) - len(filtered)} items remaining")
    except FileNotFoundError as e:
                print(e)

if __name__ == "__main__":
        main()   
