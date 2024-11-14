# User Guide for Customer Feedback Analysis Program

Welcome to the Customer Feedback Analysis Program! This guide will help you set up, install necessary dependencies, and understand how to use the application effectively.

## 1. Prerequisites

This program requires a few dependencies and additional setup steps before it can be used. Please follow each step carefully to ensure everything is installed correctly.

### System Requirements

- Python 3.7 or higher
- Streamlit
- Internet connection (to download Whisper model on the first run)
- An openAI API key

### Software Dependencies

This program uses `ffmpeg`, which is necessary for audio processing. Follow the instructions below to install it based on your operating system:

- **Windows**: Follow this guide to install `ffmpeg`: [How to Install FFmpeg on Windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
- **Mac**: Follow this guide to install `ffmpeg`: [How to Install FFmpeg on Mac](https://phoenixnap.com/kb/ffmpeg-mac)
- **Linux**: In an administrator terminal, you can install `ffmpeg` using:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

## 2. Installation

1. **Clone or Download the Repository**: Download this program’s code via ZIP in github or clone the repository to your local machine.

2. **Install Required Python Packages**: The required dependencies are listed in the `requirements.txt` file. Use the following command to install them:
   ```bash
   pip install -r requirements.txt
   ```

   This will install packages like `streamlit`, `openai`, `pillow`, `matplotlib`, `whisper`, and other necessary libraries.

3. **Add Your OpenAI API Key**:
   - This program requires an OpenAI API key for sentiment analysis.
   - Open the `results.py` file in your code editor.
   - Find line #25 where the OpenAI API key is retrieved 
   - Replace it with your actual OpenAI API key by assigning it directly as follows:
     ```python
     api_key = "your_openai_api_key_here"
     ```
   - Replace `"your_openai_api_key_here"` with your actual OpenAI API key. If you don’t have an API key, you can get one from [OpenAI](https://platform.openai.com/signup).

4. **Install Whisper Model (First Run)**:
   The first time you run the program, it will automatically download the Whisper model for transcription. This may take a few minutes, so please be patient. Subsequent runs will be faster as the model will be cached locally.

## 3. Running the Program

To start the application, open a terminal, navigate to the program’s directory, and run the following command:

```bash
streamlit run app.py
```

### Program Workflow

The program is divided into three main sections accessible from the sidebar in the Streamlit app:

1. **Record Feedback**:
   - This page allows you to **record audio feedback directly within the app**. Click the button to start recording, then click again to stop.
   - Once you stop the recording, the audio will be saved in memory and will be ready for analysis on the next steps.
   - **Tip**: Ensure your microphone is working correctly, and allow any permissions that the browser may request.

2. **Select Categories**:
   - After recording, you can specify the categories you want feedback analyzed for.
   - Type each category (e.g., "Food," "Service," "Atmosphere") and click to add them to your list.

3. **View Results**:
   - This page provides an analysis of your feedback.
   - The sentiment analysis includes:
     - A **General Sentiment Score** showing the overall tone.
     - A **Word Cloud** highlighting the most frequently mentioned words.
     - A **Sentiment Score by Category** (horizontal bar chart) comparing sentiment across each category.
     - Detailed feedback summaries for each category, separated into positive feedback, negative feedback, and suggested improvements.

## 4. Tips for Best Experience

- **First Run**: The initial run may be slower because the program needs to download the Whisper model for transcription. This will only happen once; subsequent runs will be faster.
- **Audio Requirements**: The program accepts audio recorded directly within the app. Ensure your microphone is properly set up.
- **Category Customization**: You can type any custom categories for feedback analysis. Examples include "Service," "Price," "Atmosphere," etc.

## 5. Troubleshooting

- **FFmpeg Not Found**: If you encounter issues with `ffmpeg`, double-check the installation and that it's added to your system PATH. Refer to the guides above for installation help.
- **Model Download Issues**: If Whisper model download fails, check your internet connection. You can also manually install Whisper by following the [official Whisper installation instructions](https://github.com/openai/whisper).
- **API Key Issues**: Make sure your OpenAI API key is correctly placed in the `results.py` file. Double-check for any extra spaces or incorrect characters.

That’s it! You’re now ready to use the Customer Feedback Analysis Program. Enjoy analyzing feedback with ease, and don’t hesitate to reach out to laurenshoutekamer@gmail.com if you need further assistance.