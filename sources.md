# Sources

This project was developed with the assistance of various resources, including prompts and guidance from OpenAI's ChatGPT. Below are some essential prompts used in the development process, along with references to ChatGPT’s contributions.

---

## Assistance from ChatGPT

The following sections of this project were created or refined based on guidance and prompts provided by ChatGPT:

### Key Prompts Used

1. **Project Structure and Multi-Page Setup**
   - **Prompt**: "I have a project with multiple Python files and I want to organize the main file to manage navigation between pages. Can you guide me on structuring the project with multiple pages in Streamlit?"
   - **Response**: ChatGPT provided guidance on organizing the project into separate modules (`app.py`, `audio_recorder.py`, `category_selection.py`, `results.py`) and setting up a navigation system with Streamlit.

2. **Audio Recording Setup**
   - **Prompt**: "The program needs to allow audio recording on one page. Can you show me how to integrate an audio recorder in Streamlit and save the recorded audio for analysis?"
   - **Response**: ChatGPT suggested using the `audiorecorder` library to enable in-app audio recording, along with installation instructions and setup details.

3. **Sentiment Analysis and OpenAI API Usage**
   - **Prompt**: "Can you help me create a function that uses the OpenAI API to analyze customer feedback? I need to get structured feedback analysis and sentiment scores for different categories."
   - **Response**: ChatGPT provided a structured prompt for using OpenAI's API to analyze text data, including sentiment scoring by category and general sentiment scores.

4. **Enhanced Visualization**
   - **Prompt**: "I want to make the final page look like a McKinsey-style presentation with clear visual separation for each category and a professional design. Any ideas on how to style it with Streamlit and add a sentiment score graph?"
   - **Response**: ChatGPT offered advice on adding a bar chart for sentiment scores, customizing section layouts with colors and borders, and aligning fonts and styles for a more polished look.

5. **User Guide and Documentation**
   - **Prompt**: "Can you help me write a user guide for this project that includes installation instructions and tips for first-time users? Also, mention the need for ffmpeg and Whisper model download."
   - **Response**: ChatGPT provided a complete user guide template, detailing installation steps, program usage, and additional dependencies, which was then saved as `USER_GUIDE.md`.

6. **Sources File**
   - **Prompt**: "Can you create a sources file that includes a reference to ChatGPT with some of the essential prompts used in this project?"
   - **Response**: ChatGPT provided this `SOURCES.md` template, listing the prompts and contributions made throughout the project.

---

## Additional Resources

1. **FFmpeg Installation Guides**:
   - **Windows**: [How to Install FFmpeg on Windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
   - **Mac**: [How to Install FFmpeg on Mac](https://phoenixnap.com/kb/ffmpeg-mac)

2. **Whisper Model**:
   - [Whisper GitHub Repository](https://github.com/openai/whisper)

3. **Streamlit Documentation**:
   - [Streamlit Official Documentation](https://docs.streamlit.io/)
