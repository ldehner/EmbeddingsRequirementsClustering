import json
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
import graph


# Read Embeddings from JSON File
def getEmbeddings(path):
    with open(path, "r") as file:
        return json.load(file)


# KMeans with a fixed random state for reproducibility
def getKmeans(clusters, state, embeddings):
    kmeans = KMeans(n_clusters=clusters, random_state=state)
    return kmeans.fit_predict(embeddings)


# Generate Hierarchical Clusters
def getHierarchical(clusters, embeddings):
    hierarchical = AgglomerativeClustering(n_clusters=clusters)
    return hierarchical.fit_predict(embeddings)


# Function to group and print clusters
def print_clusters(labels, requirements):
    clustered_requirements = {i: [] for i in range(max(labels) + 1)}
    for index, (requirement, label) in enumerate(zip(requirements, labels)):
        # Append the index and requirement to the appropriate cluster
        clustered_requirements[label].append((index, requirement))

    for cluster, requirements_list in clustered_requirements.items():
        print(f"Cluster {cluster+1}:")
        for index, requirement in requirements_list:
            print(f"  {index+1}. {requirement}")  # Index+1 to start numbering from 1
        print("\n")  # Add a newline for better readability


# --------------------------------------------------------------
# Run Methods


# Get Embeddings and Requirements
embeddings_dict = getEmbeddings("embeddings.json")
embeddings = np.array(list(embeddings_dict.values()))
requirements = list(embeddings_dict.keys())

# Get KMeans Clusters
print("KMeans Clusters:")
kmeans_cluster = getKmeans(5, 42, embeddings)
print_clusters(kmeans_cluster, requirements)
graph.plot_clusters(embeddings, kmeans_cluster, 6, "KMeans Clusters")

# Get Hierarchical Clusters
print("Hierarchical Clusters:")
hier_cluster = getHierarchical(5, embeddings)
print_clusters(hier_cluster, requirements)
graph.plot_clusters(embeddings, hier_cluster, 9, "Hierarchical Clusters")
