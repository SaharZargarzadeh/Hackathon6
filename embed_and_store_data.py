# Create embeddings
embeddings = model.encode(df['text_for_embedding'].tolist())

# Initialize Pinecone
pc = Pinecone(api_key="b9a7b1fe-0ebb-40f8-bbdc-26246b2c3805")

# Create or connect to an index
index_name = "netflix-search"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'  # Update to the correct region
        )
    )

# Get the index
index = pc.Index(index_name)

# Upsert data to Pinecone
batch_size = 100
for i in range(0, len(df), batch_size):
    i_end = min(i + batch_size, len(df))
    metadata = df.iloc[i:i_end][['title', 'type', 'description', 'release_year', 'age_certification', 'runtime', 'imdb_score']].to_dict(orient='records')
    
    # Convert NaN values to empty strings in metadata
    for item in metadata:
        for key, value in item.items():
            if pd.isna(value):
                item[key] = ''  # Replace NaN with an empty string

    to_upsert = list(zip(df.index[i:i_end].astype(str), embeddings[i:i_end], metadata))
    index.upsert(vectors=to_upsert)
