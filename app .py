import streamlit as st

from chain import get_response


st.set_page_config(
    page_title="FoodMitra",
    layout="wide"
)


st.markdown("""
<style>

.stApp {
    background: radial-gradient(
        circle at top left,
        #7b2d26,
        #3b1f1f,
        #000000
    );
    color: white;
}

.header {
    text-align: center;
    font-size: 50px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #ff9966,
        #ff5e62
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 5px;
}

.subtext {
    text-align: center;
    font-size: 16px;
    color: #dcdcdc;
    margin-bottom: 25px;
}

.glass {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 22px;

    backdrop-filter: blur(16px);

    box-shadow:
        0 8px 40px rgba(0,0,0,0.5);

    margin-bottom: 18px;

    line-height: 1.6;
}

.user-msg {
    background: linear-gradient(
        135deg,
        #ff9966,
        #ff5e62
    );

    padding: 12px;

    border-radius: 14px;

    margin-bottom: 10px;

    color: white;

    max-width: 75%;
}

.bot-msg {
    background: rgba(
        255,
        255,
        255,
        0.1
    );

    padding: 14px;

    border-radius: 14px;

    margin-bottom: 10px;

    max-width: 80%;
}

.summary {
    background: linear-gradient(
        135deg,
        #ff7e5f,
        #feb47b
    );

    padding: 14px;

    border-radius: 14px;

    color: black;

    font-weight: 600;

    margin-top: 10px;
}

.map-box {
    border-radius: 14px;

    overflow: hidden;

    margin-bottom: 12px;

    border:
        1px solid
        rgba(255,255,255,0.2);
}

.section-title {
    font-size: 22px;

    font-weight: 600;

    margin-top: 20px;

    margin-bottom: 10px;
}

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #2b1a1a,
        #432323
    );

    color: white;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION
# -----------------------------
if "chats" not in st.session_state:

    st.session_state.chats = {
        "Restaurant Chat 1": []
    }

    st.session_state.current_chat = (
        "Restaurant Chat 1"
    )

def show_map(restaurant):

    url = (
        "https://www.google.com/maps?q="
        + restaurant.replace(" ", "+")
        + "&output=embed"
    )

    st.markdown(
        "<div class='map-box'>",
        unsafe_allow_html=True
    )

    st.components.v1.iframe(
        url,
        height=260
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

with st.sidebar:

    st.title("🍽️ FoodMitra")

    if st.button("➕ New Chat"):

        name = (
            f"Restaurant Chat "
            f"{len(st.session_state.chats) + 1}"
        )

        st.session_state.chats[name] = []

        st.session_state.current_chat = name


    st.radio(
        "Chats",
        list(st.session_state.chats.keys()),
        key="current_chat"
    )


    st.markdown("### ⚙️ Preferences")


    cuisine = st.selectbox(
        "Cuisine",
        [
            "Any",
            "Indian",
            "South Indian",
            "Italian",
            "Arabian",
            "Cafe"
        ]
    )


    budget = st.selectbox(
        "Budget",
        [
            "Any",
            "Low",
            "Medium",
            "High"
        ]
    )


    food_type = st.selectbox(
        "Food Preference",
        [
            "Any",
            "Vegetarian",
            "Non-Vegetarian"
        ]
    )


    dining_type = st.selectbox(
        "Dining Type",
        [
            "Any",
            "Family",
            "Friends",
            "Couple"
        ]
    )


    st.markdown("### 🎯 Quick Search")


    if st.button("🥗 Vegetarian"):

        st.session_state.quick = (
            "Find vegetarian restaurants"
        )


    if st.button("🍛 Biryani"):

        st.session_state.quick = (
            "Find restaurants serving biryani"
        )


    if st.button("☕ Cafe"):

        st.session_state.quick = (
            "Find good cafes"
        )


st.markdown(
    "<div class='header'>FoodMitra</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtext'>"
    "AI Restaurant Discovery & Recommendation Assistant 🍽️"
    "</div>",
    unsafe_allow_html=True
)


st.success(
    "🧠 LangSmith Tracing Enabled"
)

chat_history = st.session_state.chats[
    st.session_state.current_chat
]


for msg in chat_history:

    if msg["role"] == "user":

        st.markdown(
            f"<div class='user-msg'>"
            f"👤 {msg['content']}"
            f"</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"<div class='bot-msg'>"
            f"🤖 {msg['content']}"
            f"</div>",
            unsafe_allow_html=True
        )



user_input = st.chat_input(
    "Ask about restaurants..."
)


if "quick" in st.session_state:

    user_input = st.session_state.quick

    del st.session_state.quick


# -----------------------------
# PROCESS QUERY
# -----------------------------
if user_input:

    query = user_input


    if cuisine != "Any":
        query += f", {cuisine} cuisine"


    if budget != "Any":
        query += f", {budget} budget"


    if food_type != "Any":
        query += f", {food_type} food"


    if dining_type != "Any":
        query += f", suitable for {dining_type}"


    st.markdown(
        f"<div class='user-msg'>"
        f"👤 {query}"
        f"</div>",
        unsafe_allow_html=True
    )


    chat_history.append({
        "role": "user",
        "content": query
    })


    with st.spinner(
        "🍳 Finding suitable restaurants..."
    ):

        response, restaurants = get_response(
            query,
            st.session_state.current_chat
        )



    st.markdown(
        f"<div class='glass'>"
        f"🤖 {response}"
        f"</div>",
        unsafe_allow_html=True
    )



    st.markdown(
        f"""
        <div class='summary'>
        🍽️ Cuisine: {cuisine}
        &nbsp; • &nbsp;
        💰 Budget: {budget}
        &nbsp; • &nbsp;
        🥗 Food: {food_type}
        &nbsp; • &nbsp;
        👨‍👩‍👧 Dining: {dining_type}
        </div>
        """,
        unsafe_allow_html=True
    )


    if restaurants:

        st.markdown(
            "<div class='section-title'>"
            "📍 Explore Restaurants"
            "</div>",
            unsafe_allow_html=True
        )


        for restaurant in restaurants[:5]:

            with st.expander(
                f"🍽️ {restaurant}"
            ):

                show_map(restaurant)


    chat_history.append({
        "role": "assistant",
        "content": response
    })
