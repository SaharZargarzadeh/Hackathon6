"""
    Create an Streamlit app that does the following:

    - Reads an input from the user
    - Embeds the input
    - Search the vector DB for the entries closest to the user input
    - Outputs/displays the closest entries found
"""

# Streamlit app
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        color: #4A90E2;
        text-align: center;
        margin-bottom: 20px;
    }
    .description {
        font-size: 1.2em;
        margin-bottom: 20px;
        color: #555;
        text-align: center;
    }
    .result {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .error {
        color: red;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Netflix Semantic Search</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Find movies and TV shows based on your description.</p>", unsafe_allow_html=True)

query = st.text_input("Enter a description of the movie or TV show you're looking for:")

if query:
    # Create embedding for the query
    query_embedding = model.encode([query]).tolist()
    
    # Search in Pinecone
    with st.spinner("Searching..."):
        results = index.query(vector=query_embedding, top_k=5, include_metadata=True)

    # Display results
    if results['matches']:
        for result in results['matches']:
            with st.container():
                st.markdown(f"<div class='result'>", unsafe_allow_html=True)
                st.write(f"**Title:** {result['metadata'].get('title', 'N/A')}")
                st.write(f"**Type:** {result['metadata'].get('type', 'N/A')}")
                st.write(f"**Description:** {result['metadata'].get('description', 'N/A')}")
                st.write(f"**Release Year:** {result['metadata'].get('release_year', 'N/A')}")
                st.write(f"**Age Certification:** {result['metadata'].get('age_certification', 'N/A')}")
                st.write(f"**Runtime:** {result['metadata'].get('runtime', 'N/A')}")
                st.write(f"**IMDB Score:** {result['metadata'].get('imdb_score', 'N/A')}")
                st.markdown("</div>", unsafe_allow_html=True)
                st.write("---")
    else:
        st.write("No results found.")
else:
    st.write("<div class='error'>Please enter a description to search.</div>", unsafe_allow_html=True)
