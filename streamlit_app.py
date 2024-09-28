import streamlit as st
import google.generativeai as genai

#st.title("🎈 My chatbot app")
#st.subheader("Conversation")
#st.write(
    #"Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
# Display the user input

#Exercise1.1
#if user_input := st.text_input("You: ", placeholder="Type your message here..."):
    #st.write(f"User Input: {user_input}")

#Exercise1.2
# Initialize session state for storing chat history
#if "chat_history" not in st.session_state:
    #st.session_state.chat_history = [] # Initialize with an empty list
# Display the user input
#if user_input := st.text_input("You: ", placeholder="Type your message here..."):
    #st.session_state.chat_history.append(user_input)
# Display all messages using st.write
#for message in st.session_state.chat_history:
    #st.write(message)

#Exercise1.3
# Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [] # Initialize with an empty list
# # Display all chat messages
# for message in st.session_state.chat_history:
#     with st.chat_message("user"):
#         st.markdown(message)
# # Capture user input and append to chat history
# if prompt := st.chat_input("Type your message here ..."):
#     st.session_state.chat_history.append(prompt)
#     st.chat_message("user").markdown(prompt)



# st.title("🎈My chatbot app")
# st.subheader("Conversation")

# # Capture Gemini API Key
# gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# # Initialize the Gemini Model
# if gemini_api_key:
#  try:
#   # Configure Gemini with the provided API Key
#   genai.configure(api_key=gemini_api_key)
#   model = genai.GenerativeModel("gemini-pro")
#   st.success("Gemini API Key successfully configured.")
#  except Exception as e:
#   st.error(f"An error occurred while setting up the Gemini model: {e}")
  
# # Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
#  st.session_state.chat_history = [] # Initialize with an empty list
 
# # Display previous chat history using st.chat_message (if available)
# for role, message in st.session_state.chat_history:
#  st.chat_message(role).markdown(message)
 
# # Capture user input and generate bot response
# if user_input := st.chat_input("Type your message here..."):
#  # Store and display user message
#  st.session_state.chat_history.append(("user", user_input))
#  st.chat_message("user").markdown(user_input)
 
#  # Use Gemini AI to generate a bot response
#  if model:
#   try:
#    response = model.generate_content("Data Analytics Expert only")
#    bot_response = response.text
   
#    # Store and display the bot response
#    st.session_state.chat_history.append(("assistant", bot_response))
#    st.chat_message("assistant").markdown(bot_response)
#   except Exception as e:
#    st.error(f"An error occurred while generating the response: {e}")

#import streamlit as st

st.title("🎨 Art Toy Pop Mart Collection")
st.subheader("Select your favorite Art Toy and view its collections")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
model = genai.GenerativeModel("gemini-pro")

# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history and selected art toy
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list
if "selected_art_toy" not in st.session_state:
    st.session_state.selected_art_toy = None  # Initialize with no selected toy

# Text input for entering Art Toy name
art_toy_input = st.text_input("Enter the name of your Art Toy (e.g., Molly, Dimoo, etc.)")

# Check if the entered art toy has changed
if art_toy_input and art_toy_input != st.session_state.selected_art_toy:
    # Clear chat history if a new art toy is entered
    st.session_state.chat_history = []
    st.session_state.selected_art_toy = art_toy_input

# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Generate bot response based on entered art toy
if art_toy_input:
    # Capture user message
    if user_input := st.chat_input("Ask about the collection of your selected Art Toy..."):
        # Store and display the user's message
        st.session_state.chat_history.append(("user", user_input))
        st.chat_message("user").markdown(user_input)

        # Use Gemini AI to generate the collection details for the entered art toy
        if model:
            try:
                response = model.generate_content(f"Provide collection details for {art_toy_input} art toy")
                bot_response = response.text

                # Store and display the bot response
                st.session_state.chat_history.append(("assistant", bot_response))
                st.chat_message("assistant").markdown(bot_response)
            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")
        else:
            st.error("Gemini model is not available. Please provide a valid API Key.")