import numpy as np
import faiss

# Step 2: Load feature vectors and labels
data = np.load('image_features.npz', allow_pickle=True)
feature_vectors = data['features']
labels = data['labels']
print(feature_vectors.shape)
print(labels.shape)
# Step 3: Create and populate a FAISS index
# Assuming feature_vectors is of shape (num_vectors, vector_dim) and type float32
vector_dim = feature_vectors.shape[1]
print(vector_dim)
index = faiss.IndexFlatL2(vector_dim)  # Using L2 distance for similarity
# If your vectors are not normalized:
# faiss.normalize_L2(feature_vectors)
index.add(feature_vectors)  # Adding the feature vectors to the index

# Step 4: Querying
def query_vector(vec, k=10):
    """
    Query the index for the k nearest neighbors of vec.
    
    Parameters:
    - vec: The query vector.
    - k: Number of nearest neighbors to find.
    
    Returns:
    - The labels of the k nearest neighbors.
    """
    # If your query vector needs to be normalized:
    # faiss.normalize_L2(vec.reshape(1, -1))
    D, I = index.search(vec.reshape(1, -1), k)  # vec needs to be reshaped as a 1xvector_dim matrix
    return [labels[i] for i in I[0]]

# Example usage
# Let's query for the first vector in our dataset as a simple test
#def get_feature_vector_by_label(label):
#    matches = np.where(labels == label)
#    ind = matches[0][0]
#    return feature_vectors[ind]

#query_vec = get_feature_vector_by_label('0042')
print(query_vec)
nearest_labels = query_vector(query_vec, 10)
print("Labels of the nearest neighbors:", nearest_labels)
#print(labels[:10])
