import openai
import re


def analyze_sentiment(transcript, api_key, categories):
    openai.api_key = api_key
    client = openai.OpenAI(api_key=api_key)  # Initialize OpenAI client

    # Convert the list of categories into a readable format
    categories_str = ", ".join(categories)

    # Define the prompt with user-specified categories
    prompt = f"""
    You are an assistant that analyzes customer feedback transcripts. The feedback is about the following categories: {categories_str}.

    For each feedback category, please provide the following in this specific structured format, make sure every category is named exactly as in the prompt:

    - sentiment_score_<category_name> = <number between 0 and 1>
    - positive_feedback_<category_name> = ["positive aspect 1", "positive aspect 2", ...]
    - negative_feedback_<category_name> = ["negative aspect 1", "negative aspect 2", ...]
    - improvements_<category_name> = ["improvement 1", "improvement 2", ...]

    In addition, please provide:

    - general_sentiment_score = <number between 0 and 1> for the whole feedback transcript
    - important_words = ["word1", "word2", ...]

    The transcript is:

    \"\"\"{transcript}\"\"\"
    """

    # Make the API call
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the response content
    response_text = completion.choices[0].message.content

    # Initialize variables
    general_sentiment_score = None
    important_words = []
    positive_dict = {}
    negative_dict = {}
    improvements_dict = {}
    sentiment_dict = {}

    # Extract general sentiment score
    general_score_match = re.search(
        r"general_sentiment_score\s*=\s*([\d.]+)", response_text
    )
    if general_score_match:
        general_sentiment_score = float(general_score_match.group(1))

    # Extract important words
    important_words_match = re.search(r"important_words\s*=\s*\[(.*?)\]", response_text)
    if important_words_match:
        important_words = [
            word.strip().strip('"')
            for word in important_words_match.group(1).split(",")
        ]

    # Extract information for each category
    for category in categories:
        # Sentiment score
        sentiment_match = re.search(
            f"sentiment_score_{category}\\s*=\\s*([\\d.]+)",
            response_text,
            re.IGNORECASE,
        )
        if sentiment_match:
            sentiment_dict[category] = float(sentiment_match.group(1))

        # Positive feedback
        positive_match = re.search(
            f"positive_feedback_{category}\\s*=\\s*\\[(.*?)\\]",
            response_text,
            re.IGNORECASE,
        )
        if positive_match:
            positive_dict[category] = [
                item.strip().strip('"') for item in positive_match.group(1).split(",")
            ]

        # Negative feedback
        negative_match = re.search(
            f"negative_feedback_{category}\\s*=\\s*\\[(.*?)\\]",
            response_text,
            re.IGNORECASE,
        )
        if negative_match:
            negative_dict[category] = [
                item.strip().strip('"') for item in negative_match.group(1).split(",")
            ]

        # Improvements
        improvements_match = re.search(
            f"improvements_{category}\\s*=\\s*\\[(.*?)\\]", response_text, re.IGNORECASE
        )
        if improvements_match:
            improvements_dict[category] = [
                item.strip().strip('"')
                for item in improvements_match.group(1).split(",")
            ]

    return (
        positive_dict,
        negative_dict,
        improvements_dict,
        sentiment_dict,
        general_sentiment_score,
        important_words,
    )
