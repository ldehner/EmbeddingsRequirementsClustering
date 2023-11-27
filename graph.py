import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


def plot_clusters(embeddings, labels, perp, title="Cluster Visualization"):
    # Ensure perplexity is less than the number of samples
    perplexity_value = perp  # Adjust 30 to a lower number if needed

    # Reduce dimensionality for visualization
    tsne = TSNE(n_components=2, perplexity=perplexity_value, random_state=42)
    reduced_embeddings = tsne.fit_transform(embeddings)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=labels, cmap="Spectral"
    )
    plt.title(title)
    plt.xlabel("t-SNE Axis 1")
    plt.ylabel("t-SNE Axis 2")

    # Annotate points with their index or custom label
    for i, point in enumerate(reduced_embeddings):
        plt.text(point[0], point[1], str(i + 1), fontsize=9)

    # Generate custom legend
    legend_labels = [f"Cluster {i+1}" for i in range(max(labels) + 1)]
    legend1 = plt.legend(
        handles=scatter.legend_elements()[0], labels=legend_labels, title="Clusters"
    )
    plt.gca().add_artist(legend1)

    # Show plot
    plt.show()
