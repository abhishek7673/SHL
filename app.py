import streamlit as st
import requests

st.title("SHL Assessment Recommendation")

query = st.text_area("Enter a Job Description or Role Requirement:")

if st.button("Get Recommendations") and query.strip():
    response = requests.post(
        "https://shl-2m13.onrender.com/recommend",
        json={"query": query}
    )

    if response.status_code == 200:
        results = response.json()
        if results:
            st.success("Top Recommendations:")
            for rec in results:
                st.write(f"**{rec['Assessment Name']}**")
                st.write(f"- Description: {rec['Assessment Description']}")
                st.write(f"- Type: {rec['Assessment Type']}")
                st.write(f"- Level: {rec['Job Level']}")
                st.markdown("---")
        else:
            st.warning("No recommendations found.")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

# import streamlit as st
# from recommender import SHLRecommender

# st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# st.title("SHL Assessment Recommendation Engine")

# query = st.text_input("Enter Job Description or Query")

# if query:
#     recommender = SHLRecommender()
#     results = recommender.recommend(query)
#     st.write("### Top Matching Assessments")
#     st.dataframe(results.drop(columns="score"))

    # app.py
import streamlit as st
from recommender import SHLRecommender

# st.set_page_config(page_title="SHL Assessment Recommendation", layout="wide")

# st.title("🔍 SHL Assessment Recommendation Engine")

# query = st.text_area("Enter a Job Description or Role Requirement:")

# if query:
#     with st.spinner("Finding relevant assessments..."):
#         recommender = SHLRecommender()
#         results = recommender.recommend(query)
#         st.success("Top Recommendations:")
#         st.table(results)
# else:
#     st.info("Please enter a job description or query to get started.")

