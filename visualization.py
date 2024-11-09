import streamlit as st
from wordcloud import WordCloud
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def generate_wordcloud_image(words):
    wordcloud = WordCloud(
        width=600, height=400, background_color="white", colormap="Blues"
    ).generate(" ".join(words))
    buffer = BytesIO()
    wordcloud.to_image().save(buffer, format="PNG")
    image = Image.open(buffer)
    return image


def plot_sentiment_scores(sentiment_dict, general_sentiment_score):
    # Add the general sentiment score to the categories and scores lists
    categories = ["Overall"] + list(sentiment_dict.keys())
    scores = [general_sentiment_score * 100] + [
        sentiment_dict[cat] * 100 for cat in sentiment_dict.keys()
    ]

    # Set up the plot with a consistent font
    plt.figure(figsize=(10, 6))
    plt.barh(categories, scores, color="#4a90e2")  # McKinsey-style blue color
    plt.xlabel("Sentiment Score (%)", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=12)
    plt.title("Sentiment Score by Category", fontsize=14, weight="bold")
    plt.gca().invert_yaxis()
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    return plt


def display_feedback(
    positive_dict,
    negative_dict,
    improvements_dict,
    sentiment_dict,
    general_sentiment_score,
    important_words,
):
    # Page Title
    st.markdown(
        "<h1 style='text-align: center; color: #4a4a4a;'>Customer Feedback Analysis</h1>",
        unsafe_allow_html=True,
    )

    # Overall Sentiment Score
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='color: #4a90e2;'>Overall Sentiment Score</h2>",
        unsafe_allow_html=True,
    )
    st.write(f"**General Sentiment Score**: {general_sentiment_score * 100:.2f}%")

    # Important Words Word Cloud
    st.markdown(
        "<h3 style='color: #4a90e2;'>Key Sentiment Drivers</h3>", unsafe_allow_html=True
    )
    wordcloud_image = generate_wordcloud_image(important_words)
    st.image(
        wordcloud_image,
        caption="Word Cloud of Important Words",
        use_container_width=True,
    )

    # Sentiment Score by Category (Graph)
    st.markdown(
        "<h3 style='color: #4a90e2;'>Sentiment Score by Category</h3>",
        unsafe_allow_html=True,
    )
    plt = plot_sentiment_scores(sentiment_dict, general_sentiment_score)
    st.pyplot(plt)

    # Display feedback summary by category with distinct styling
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='color: #4a90e2;'>Feedback Summary by Category</h2>",
        unsafe_allow_html=True,
    )

    for category in positive_dict.keys():
        st.markdown(
            f"<h3 style='color: #4a4a4a;'>{category} Category</h3>",
            unsafe_allow_html=True,
        )

        # Display sentiment score for the category
        if category in sentiment_dict:
            st.write(
                f"**Sentiment Score for {category}**: {sentiment_dict[category] * 100:.2f}%"
            )

        # Use colored boxes for each feedback type
        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(
                    "<div style='border: 1px solid #4a90e2; padding: 10px; border-radius: 5px;'><h4 style='color: #4a90e2;'>Positive Feedback</h4>",
                    unsafe_allow_html=True,
                )
                for feedback in positive_dict.get(category, []):
                    st.write("- ", feedback)
                st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                st.markdown(
                    "<div style='border: 1px solid #d9534f; padding: 10px; border-radius: 5px;'><h4 style='color: #d9534f;'>Negative Feedback</h4>",
                    unsafe_allow_html=True,
                )
                for feedback in negative_dict.get(category, []):
                    st.write("- ", feedback)
                st.markdown("</div>", unsafe_allow_html=True)

            with col3:
                st.markdown(
                    "<div style='border: 1px solid #f0ad4e; padding: 10px; border-radius: 5px;'><h4 style='color: #f0ad4e;'>Suggested Improvements</h4>",
                    unsafe_allow_html=True,
                )
                for improvement in improvements_dict.get(category, []):
                    st.write("- ", improvement)
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
