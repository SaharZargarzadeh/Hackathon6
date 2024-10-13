# Load the dataset
df = pd.read_csv('Netflix TV Shows and Movies.csv')


# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')
