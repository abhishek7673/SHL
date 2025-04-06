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

st.set_page_config(page_title="SHL Assessment Recommendation", layout="wide")

st.title("🔍 SHL Assessment Recommendation Engine")

query = st.text_area("Enter a Job Description or Role Requirement:")

if query:
    with st.spinner("Finding relevant assessments..."):
        recommender = SHLRecommender()
        results = recommender.recommend(query)
        st.success("Top Recommendations:")
        st.table(results)
else:
    st.info("Please enter a job description or query to get started.")

