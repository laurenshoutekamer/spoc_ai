import streamlit as st


def main():
    st.title("Select Feedback Categories")
    st.write("Type the feedback categories you care about and add them to the list.")

    # Input for adding a custom category
    new_category = st.text_input("Enter a category", "")

    # Button to add the typed category to the list
    if st.button("Add Category"):
        if new_category:
            if "selected_categories" not in st.session_state:
                st.session_state["selected_categories"] = []
            st.session_state["selected_categories"].append(new_category)
            st.success(f"Added category: {new_category}")
        else:
            st.warning("Please enter a valid category.")

    # Display current list of categories
    st.write("Selected Categories:")
    if (
        "selected_categories" in st.session_state
        and st.session_state["selected_categories"]
    ):
        for idx, category in enumerate(st.session_state["selected_categories"], 1):
            st.write(f"{idx}. {category}")

    # Button to proceed
    if st.button("Submit Categories"):
        if st.session_state["selected_categories"]:
            st.success("Categories saved! Proceed to the next step.")
        else:
            st.warning("Please add at least one category.")


if __name__ == "__main__":
    main()
