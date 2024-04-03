import numpy as np
import sys
import faiss

data = np.load('image_features.npz', allow_pickle=True)
feature_vectors = data['features']
labels = data['labels']
vector_dim = feature_vectors.shape[1]
index = faiss.IndexFlatL2(vector_dim)  
index.add(feature_vectors)  

def query_vector(vec, k=10):
    """
    Query the index for the k nearest neighbors of vec.
    
    Parameters:
    - vec: The query vector.
    - k: Number of nearest neighbors to find.
    
    Returns:
    - The labels of the k nearest neighbors.
    """
    D, I = index.search(vec.reshape(1, -1), k)  # vec needs to be reshaped as a 1xvector_dim matrix
    return [labels[i//8] for i in I[0]]

def get_feature_vector_by_label(label):
    matches = np.where(labels == label)
    ind = matches[0][0]
    return feature_vectors[ind*8]

if __name__ == '__main__':
    while True:
        user_input = input("Enter a codepoint (4 characters) or type 'q': ")
        if user_input.strip().lower() == 'q':
            break
        if len(user_input.strip().lower()) != 4:
            print("\nMust be 4 characters\n")
            continue
        
        query_label = user_input.strip().lower()
        query_vec = get_feature_vector_by_label(query_label)
        nearest_labels = query_vector(query_vec, 10)
        print(f'\nQuery codepoint: {query_label}')
        print("Labels of the nearest neighbors:", nearest_labels)
        print("\n")
