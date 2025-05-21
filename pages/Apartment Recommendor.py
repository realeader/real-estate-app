import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Apartments")

# Load required datasets
location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))
link_df = pickle.load(open('datasets/link_df.pkl', 'rb'))  # Load links

def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    top_properties = location_df.index[top_indices].tolist()
    top_links = link_df.iloc[top_indices]['Link'].tolist()

    recommendations_df = pd.DataFrame({
        'Property Name': top_properties,
        'Similarity Score': top_scores,
        'Property Link': top_links  # Store raw links, clickable later
    })

    return recommendations_df

# UI for location-based search
st.title('Select Location and Radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    for key, value in result_ser.items():
        st.text(f"{key} {round(value / 1000)} kms")

# UI for recommendation system
st.title('Recommend Apartments')
selected_apartment = st.selectbox('Select an apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)

    # Display as a simple table with clickable links
    st.write("### Recommended Properties")
    for index, row in recommendation_df.iterrows():
        st.write(f"{row['Property Name']}")
        st.write(f"Similarity Score: {row['Similarity Score']:.4f}")
        st.markdown(f"[👉 View Property]({row['Property Link']})", unsafe_allow_html=True)
        st.markdown("---")  # Divider for better readability


# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np

# st.set_page_config(page_title="Recommend Appartments")

# location_df = pickle.load(open('datasets/location_distance.pkl','rb'))

# cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
# cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl','rb'))
# cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl','rb'))


# def recommend_properties_with_scores(property_name, top_n=5):
#     cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
#     # cosine_sim_matrix = cosine_sim3

#     # Get the similarity scores for the property using its name as the index
#     sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

#     # Sort properties based on the similarity scores
#     sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     # Get the indices and scores of the top_n most similar properties
#     top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
#     top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

#     # Retrieve the names of the top properties using the indices
#     top_properties = location_df.index[top_indices].tolist()

#     # Create a dataframe with the results
#     recommendations_df = pd.DataFrame({
#         'PropertyName': top_properties,
#         'SimilarityScore': top_scores
#     })

#     return recommendations_df


# # Test the recommender function using a property name
# recommend_properties_with_scores('DLF The Camellias')


# st.title('Select Location and Radius')

# selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))

# radius = st.number_input('Radius in Kms')

# if st.button('Search'):
#     result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()

#     for key, value in result_ser.items():
#         st.text(str(key) + " " + str(round(value/1000)) + ' kms')

# st.title('Recommend Appartments')
# selected_appartment = st.selectbox('Select an appartment',sorted(location_df.index.to_list()))

# if st.button('Recommend'):
#     recommendation_df = recommend_properties_with_scores(selected_appartment)

#     st.dataframe(recommendation_df)