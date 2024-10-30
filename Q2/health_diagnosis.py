# Import required libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create a new directed graph
G = nx.DiGraph()

# Define nodes (diseases, symptoms, patients)
G.add_node("Malaria", type="Disease")
G.add_node("Tuberculosis", type="Disease")
G.add_node("COVID-19", type="Disease")

G.add_node("Fever", type="Symptom")
G.add_node("Cough", type="Symptom")
G.add_node("Headache", type="Symptom")
G.add_node("Patient1", type="Patient")

# Define edges (relationships between nodes)
G.add_edge("Malaria", "Fever", relation="hasSymptom")
G.add_edge("Malaria", "Headache", relation="hasSymptom")
G.add_edge("Tuberculosis", "Cough", relation="hasSymptom")
G.add_edge("COVID-19", "Fever", relation="hasSymptom")

# Patient symptoms
G.add_edge("Patient1", "Fever", relation="hasSymptom")
G.add_edge("Patient1", "Headache", relation="hasSymptom")

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()

#FOPL
# Define facts as Python dictionaries
symptoms = {
    "Malaria": ["Fever", "Headache"],
    "Tuberculosis": ["Cough"],
    "COVID-19": ["Fever"]
}

# Patient symptoms
patient_symptoms = {
    "Patient1": ["Fever", "Headache"]
}

# Inference function to diagnose diseases based on symptoms
def diagnose(patient):
    possible_diseases = []
    for disease, disease_symptoms in symptoms.items():
        if all(symptom in patient_symptoms[patient] for symptom in disease_symptoms):
            possible_diseases.append(disease)
    return possible_diseases

# Run inference for Patient1
diagnosis = diagnose("Patient1")
print(f"Diagnosis for Patient1: {diagnosis}")
