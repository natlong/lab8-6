import streamlit as st

options_list = [
    "Recommend degrees or skills for a job position",
    "Jobs I can apply for with my qualifications",
    "Find a job quickly after graduation",
    "Does my school affect my employment rate?",
    "Industries in high demand"
]

# Function to display options
def display_options():
    st.write("Please select an option:")
    for idx, option in enumerate(options_list):
        # Use a unique key for each button by combining a string with the index
        if st.button(option, key=f"option_{idx}"):
            st.session_state.selected_option = option
            handle_option(option)  # Handle the option immediately upon clicking
            st.rerun()  # Force rerun after the state is updated

# Function to handle the selected option
def handle_option(option):
    # Append the selected option to chat history
    st.session_state.messages.append({"user": "user", "message": option})

    # Generate bot's response based on the selected option
    if option == options_list[0]:
        bot_response = "To excel in a job position, degrees in relevant fields, alongside skills like critical thinking and communication, are essential."
        
    elif option == options_list[1]:
        bot_response = "Based on your qualifications, you can apply for jobs such as Data Analyst, Software Developer, or Marketing Specialist."
        
    elif option == options_list[2]:
        bot_response = "To find a job quickly, consider internships, networking events, and job fairs as they can provide valuable opportunities."
        
    elif option == options_list[3]:
        bot_response = "Yes, the reputation and resources of your school can influence your employment opportunities."
        
    elif option == options_list[4]:
        bot_response = "Currently, industries such as Technology, Healthcare, and Renewable Energy are in high demand."
        
    else:
        bot_response = "I'm sorry, I didn't understand that option."
    
    # Append the bot's response to chat history
    st.session_state.messages.append({"user": "bot", "message": bot_response})

# Function to display messages
def display_messages():
    for msg in st.session_state.messages:
        if msg['user'] == "user":
            st.write(f"<div style='text-align: right; margin: 5px;'><b>You:</b> {msg['message']}</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div style='text-align: left; margin: 5px;'><b>Bot:</b> {msg['message']}</div>", unsafe_allow_html=True)
