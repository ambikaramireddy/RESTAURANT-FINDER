
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY or ""
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI_Restaurant_Planner"



docs = [
    Document(
        page_content="""
        Restaurant: Spice Garden
        Location: Hyderabad
        Cuisine: Indian
        Food: Biryani, Paneer Tikka, Butter Naan, Veg Biryani
        Price: Medium
        Suitable for: Family, Friends
        Vegetarian: Yes
        Ambience: Comfortable and family friendly
        """
    ),

    Document(
        page_content="""
        Restaurant: Green Leaf
        Location: Hyderabad
        Cuisine: South Indian
        Food: Dosa, Idli, Vada, South Indian Meals
        Price: Low
        Suitable for: Family
        Vegetarian: Yes
        Ambience: Simple and peaceful
        """
    ),

    Document(
        page_content="""
        Restaurant: Arabian Nights
        Location: Hyderabad
        Cuisine: Arabian
        Food: Chicken Mandi, Shawarma, Grilled Chicken
        Price: High
        Suitable for: Friends, Family
        Vegetarian: Limited
        Ambience: Modern and spacious
        """
    ),

    Document(
        page_content="""
        Restaurant: Pizza Corner
        Location: Hyderabad
        Cuisine: Italian
        Food: Pizza, Pasta, Garlic Bread
        Price: Medium
        Suitable for: Friends, Couple
        Vegetarian: Yes
        Ambience: Casual
        """
    ),

    Document(
        page_content="""
        Restaurant: Royal Biryani
        Location: Hyderabad
        Cuisine: Indian
        Food: Chicken Biryani, Mutton Biryani, Veg Biryani
        Price: Medium
        Suitable for: Family, Friends
        Vegetarian: Yes
        Ambience: Traditional
        """
    ),

    Document(
        page_content="""
        Restaurant: Cafe Bliss
        Location: Hyderabad
        Cuisine: Cafe
        Food: Coffee, Sandwiches, Burgers, Desserts
        Price: Low
        Suitable for: Couple, Friends
        Vegetarian: Yes
        Ambience: Relaxed and cozy
        """
    ),
]


chat_memories = {}


def get_memory(chat_id):

    if chat_id not in chat_memories:
        chat_memories[chat_id] = InMemoryChatMessageHistory()

    return chat_memories[chat_id]



def get_llm(temp=0.7):

    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY")

    return ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=GROQ_API_KEY,
    temperature=temp
)



def retrieve_docs(query):

    results = []

    for d in docs:

        if any(
            word.lower() in d.page_content.lower()
            for word in query.split()
            if len(word) > 2
        ):
            results.append(d)

    return results[:4]


def build_context(docs):

    return "\n\n".join(
        [d.page_content for d in docs]
    )



def rewrite_query(question):

    prompt = ChatPromptTemplate.from_template("""
Convert the user's question into a clear restaurant search query.

Keep important information such as:
- location
- cuisine
- budget
- vegetarian/non-vegetarian preference
- family/friends/couple
- food items
- ambience
- restaurant name

Query:
{question}
""")

    chain = prompt | get_llm(0) | StrOutputParser()

    return chain.invoke({
        "question": question
    })


def extract_restaurants(text):

    prompt = ChatPromptTemplate.from_template("""
Extract only restaurant names from the following response.

Return restaurant names separated by commas.

Do not return:
- food names
- cities
- cuisines
- explanations

Text:
{text}
""")

    chain = prompt | get_llm(0) | StrOutputParser()

    result = chain.invoke({
        "text": text
    })

    return [
        restaurant.strip()
        for restaurant in result.split(",")
        if restaurant.strip()
    ]


def generate_response(question, memory):

    refined = rewrite_query(question)

    docs_found = retrieve_docs(refined)

    context = build_context(docs_found)

    prompt = ChatPromptTemplate.from_messages([

        ("system", """
You are FoodMitra, an AI Restaurant Recommendation Assistant.

Use the provided restaurant context to answer the user's question.

Provide useful information such as:

- Restaurant name
- Location
- Cuisine
- Popular food
- Price range
- Vegetarian availability
- Suitable for family/friends/couple
- Ambience

Rules:

1. Use the provided context whenever possible.
2. Do not invent restaurant information.
3. If the information is not available in the context, clearly say that it is not available.
4. For comparison questions, compare the available restaurants clearly.
5. For recommendation questions, explain why each restaurant matches the user's requirements.
6. Keep the answer simple and helpful.
"""),

        MessagesPlaceholder("chat_history"),

        ("human", """
User Question:
{question}

Restaurant Context:
{context}
""")
    ])

    chain = prompt | get_llm() | StrOutputParser()

    return chain.invoke({

        "question": refined,

        "context": context,

        "chat_history": memory.messages
    })


# -----------------------------
# MAIN RESPONSE
# -----------------------------
def get_response(question, chat_id):

    memory = get_memory(chat_id)

    answer = generate_response(
        question,
        memory
    )

    restaurants = extract_restaurants(answer)

    memory.add_message(
        HumanMessage(content=question)
    )

    memory.add_message(
        AIMessage(content=answer)
    )

    return answer, restaurants
