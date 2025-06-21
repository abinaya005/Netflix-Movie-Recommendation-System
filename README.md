Netflix Movie Recommendation System
A content-based recommendation system that suggests movies similar to a user's input by analyzing movie metadata using TF-IDF and cosine similarity.
Project Overview
This project aims to build a simple yet effective movie recommendation system based on the content of movies. It uses a real-world Netflix dataset containing movie metadata like titles, genres, and descriptions. Instead of relying on user ratings or collaborative filtering, this system focuses entirely on the descriptive content of the movies.
The core idea is to take a movie title from the user and return a list of the top 5 most similar movies based on text features. This is achieved using **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert the text into numerical vectors and **cosine similarity** to measure how closely two movies are related in terms of content.
This system is especially helpful in situations where user history is unavailable (cold-start problem) and can be adapted to recommend books, news articles, or courses with minimal modifications.
Features
- Content-based filtering using movie metadata
- Natural language processing using TF-IDF vectorization
- Similarity measurement using cosine similarity
- Top 5 movie suggestions based on user input
- Scalable approach that works without user ratings or interactions
- Clean and easy-to-understand Python code
Requirements
To run this project, make sure the following tools and libraries are installed:
- Python 3.7+
- pandas
- scikit-learn
- numpy
You can install the necessary packages by running:
bash
pip install -r requirements.txt
Installation
Follow these steps to set up and run the project:
1. Clone the Repository
git clone https://github.com/yourusername/netflix-recommendation-system.git
2. Navigate to the Project Folder
cd netflix-recommendation-system
3. Install Required Libraries
pip install -r requirements.txt
4. Add the Dataset
Make sure the Netflix movie metadata CSV file is placed in the project directory (e.g., `netflix_dataset.csv`). Update the file path in the code if needed.
Usage
1. Open the script file (e.g., `recommend.py`) in your code editor.
2. Run the script using Python:
python recommend.py
3. Enter a movie title when prompted.
4. The system will output the top 5 most similar movies based on their content.
Output
When the program is run, and a user inputs a movie title (e.g., **Inception**), the output will be a ranked list of five similar movies. For example:
Top 5 Recommendations for 'Inception':
1. Interstellar
2. The Matrix
3. Source Code
4. Tenet
5. Edge of Tomorrow
This output is based on the similarity of the movies' genres, keywords, and descriptions.
Troubleshooting
Error: FileNotFoundError
Ensure the dataset file is placed in the correct directory and the file name matches the one in the code.
Error: No such movie found
The input movie name might not exist in the dataset. Try entering another movie name that exists in the dataset.
ModuleNotFoundError
Run `pip install -r requirements.txt` to make sure all necessary libraries are installed.
Future Enhancements
* Add a **collaborative filtering** component using user ratings for hybrid recommendations.
* Build a **web interface** using Flask or Streamlit for easier interaction.
* Use **movie posters and cast** to improve recommendation relevance.
* Add **search suggestions** for partial movie title inputs.
* Include **real-time data** from online movie databases (e.g., IMDb, TMDb).
* Deploy the system on cloud platforms or as a web app for public use.
Let me know if you want this saved as a downloadable .md file or paired with a working recommend.py script!
