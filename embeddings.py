import json
import openai


# Load API Key
def load_config():
    with open("config.json", "r") as key:
        config = json.load(key)
    return config


# Load Requirements from text file
def load_requirements():
    requirements = []
    with open("requirements.txt", "r") as req:
        lines = req.readlines()

        for line in lines:
            print(line)
            requirements.append(line.replace("\n", ""))

    return requirements


# Generate Embeddings with OpenAI API
def get_embeddings(text_list):
    response = openai.embeddings.create(
        input=text_list,  # Passing the list of requirements
        model="text-embedding-ada-002",
    )

    # Extracting embeddings from the response
    embeddings = [item.embedding for item in response.data]

    # Turn into dict with Requirements
    return dict(zip(text_list, embeddings))


# Save Embeddings to JSON
def save_embeddings(embeddings):
    embeddings_json = json.dumps(embeddings)

    with open("embeddings.json", "w") as file:
        file.write(embeddings_json)


# ---------------------------------------------------------
# Run Methods


# Load things
config = load_config()
openai.api_key = config["api_key"]
requirements = load_requirements()

# Translate Requirements into Embeddings
embeddings = get_embeddings(requirements)

# Save
save_embeddings(embeddings)
