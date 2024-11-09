import streamlit as st
from sentiment_analysis import analyze_sentiment
from visualization import display_feedback
from transcribe import transcribe_audio


def main():
    st.title("Feedback Analysis Results")

    # Check if audio was recorded
    if st.session_state["audio_bytes"] is None:
        st.error("Please record your feedback on the 'Record Feedback' page.")
        return

    # Check if categories were selected
    if not st.session_state["selected_categories"]:
        st.error("Please select categories on the 'Select Categories' page.")
        return

    # Transcribe audio
    transcript = transcribe_audio(st.session_state["audio_bytes"])
    st.session_state["transcript"] = transcript

    # Analyze sentiment using OpenAI API
    api_key = "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"
    (
        positive_dict,
        negative_dict,
        improvements_dict,
        sentiment_dict,
        general_sentiment_score,
        important_words,
    ) = analyze_sentiment(transcript, api_key, st.session_state["selected_categories"])

    # Display results with the updated display_feedback function
    display_feedback(
        positive_dict,
        negative_dict,
        improvements_dict,
        sentiment_dict,
        general_sentiment_score,
        important_words,
    )


if __name__ == "__main__":
    main()
