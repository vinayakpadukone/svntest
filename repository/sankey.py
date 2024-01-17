import pandas as pd
import plotly.graph_objects as go

# Read data from the CSV file
data = pd.read_csv('Book7.csv')

# Extract unique nodes from all three columns
all_nodes = list(set(data['SymptomName'].tolist() + data['Diagnosis'].tolist() + data['MedicineName'].tolist()))

# Create dictionaries to map nodes to indices
node_indices = {node: idx for idx, node in enumerate(all_nodes)}

# Map string data to numeric indices for each column
data['source_idx'] = data['SymptomName'].map(node_indices)
data['target_idx'] = data['Diagnosis'].map(node_indices)
data['value_idx'] = data['MedicineName'].map(node_indices)

# Create a Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes
    ),
    link=dict(
        source=data['source_idx'],
        target=data['target_idx'],
        value=data['value_idx']
    ))])

# Update layout options
fig.update_layout(title_text="Three Column Sankey Diagram")

# Display the Sankey diagram in the browser
fig.show()
