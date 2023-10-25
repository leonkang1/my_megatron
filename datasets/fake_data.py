import json
import os

# The number of fake articles you want to create
num_articles = 100

# The file where you'll write the fake articles
output_file = "fake_dataset.txt"

with open(output_file, "w") as f:
    for i in range(num_articles):
        # Create a fake article
        article = {
            "id": i,
            "url": f"https://fake.wikipedia.org/wiki/Fake_Article_{i}",
            "title": f"Fake Article {i}",
            "text": f"This is the text of Fake Article {i}. It's not very interesting."
        }

        # Write the fake article to the file as a JSON object
        f.write(json.dumps(article) + os.linesep)
