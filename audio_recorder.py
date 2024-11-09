import streamlit as st
from audiorecorder import audiorecorder


def main():
    st.title("Audio Recorder")
    st.write("Click to record your feedback, then click again to stop.")

    # Use the audiorecorder function to record audio
    audio = audiorecorder("Click to record", "Click to stop recording")

    if len(audio) > 0:
        # Play the recorded audio in the frontend
        st.audio(audio.export().read(), format="audio/wav")

        # Save audio to session state for further processing
        st.session_state["audio_bytes"] = audio.export().read()

        # Display audio properties
        st.write(f"Frame rate: {audio.frame_rate}")
        st.write(f"Frame width: {audio.frame_width}")
        st.write(f"Duration: {audio.duration_seconds} seconds")

        st.success("Recording saved! Proceed to the next step.")


if __name__ == "__main__":
    main()
