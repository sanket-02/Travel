import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Function to generate itinerary
def generate_itinerary(destination, budget, duration, purpose, preferences, accommodation, mobility, dietary):
    prompt = f"""
    You are a highly skilled travel planner. Create a personalized {duration}-day itinerary for a trip to {destination}.
    Details:
    - Budget: {budget}
    - Purpose: {purpose}
    - Preferences: {preferences}
    - Accommodation Preference: {accommodation}
    - Mobility Concerns: {mobility}
    - Dietary Restrictions: {dietary}

    Provide a detailed day-by-day itinerary including:
    - Top attractions (famous and hidden gems)
    - Activity timing (morning, afternoon, evening)
    - Restaurant suggestions based on dietary restrictions
    - Downtime and relaxation activities
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
def main():
    st.title("Enhanced AI Travel Itinerary Planner")
    st.write("Provide your preferences to generate a highly customized travel itinerary.")
    
    # Inputs
    destination = st.text_input("Destination", placeholder="Enter the destination (e.g., Bali)")
    duration = st.number_input("Trip Duration (in days)", min_value=1, max_value=30, value=5)
    budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
    purpose = st.selectbox("Purpose", ["Leisure", "Adventure", "Business", "Cultural"])
    preferences = st.text_area("Activity Preferences", placeholder="E.g., nature, food, historical sites, hidden gems")
    accommodation = st.selectbox("Accommodation Preference", ["Luxury", "Budget", "Central Location"])
    mobility = st.selectbox("Mobility Concerns", ["No concerns", "Prefer minimal walking", "Mobility challenges"])
    dietary = st.text_input("Dietary Restrictions", placeholder="E.g., vegan, vegetarian, no restrictions")
    
    # Button to generate itinerary
    if st.button("Generate Itinerary"):
        # Check for missing fields
        if not destination or not preferences:
            st.error("Please fill out all required fields.")
        else:
            st.write("Generating your personalized itinerary...")
            itinerary = generate_itinerary(
                destination, budget, duration, purpose, preferences, accommodation, mobility, dietary
            )
            st.subheader("Your Personalized Itinerary")
            st.write(itinerary)

if __name__ == "__main__":
    main()
