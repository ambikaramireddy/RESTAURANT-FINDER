Absolutely. Here is the **complete GitHub-ready README** for your **FoodMitra** project, updated to use **`openai/gpt-oss-120b` through Groq API** and keeping your actual keyword-based retrieval approach.

# 🍽️ FoodMitra – AI Restaurant Recommendation Assistant

FoodMitra is an **AI-powered restaurant recommendation and discovery assistant** that helps users find suitable restaurants based on cuisine, budget, food preferences, dining type, location, and food items.

The application combines **LangChain, Groq API, OpenAI GPT-OSS 120B, lightweight retrieval, conversational memory, and Streamlit** to provide interactive restaurant recommendations.

---

## 📌 Business Objective

Finding a suitable restaurant can be difficult when users have multiple requirements such as cuisine, budget, vegetarian preference, dining type, and preferred food.

FoodMitra aims to simplify this process by allowing users to interact with an AI assistant using natural language instead of manually checking multiple restaurant options.

The system understands the user's requirements, retrieves relevant restaurant information, and generates a clear and personalized response.

---

## ❗ Problem Statement

Traditional restaurant search often requires users to:

* Search through multiple restaurants
* Compare cuisines and prices manually
* Check vegetarian or non-vegetarian options
* Find restaurants suitable for families, friends, or couples
* Read large amounts of restaurant information

FoodMitra addresses this problem by providing a **conversational AI-based restaurant assistant** that can understand natural-language queries and provide relevant restaurant suggestions.

---

## 🎯 Objectives

The main objectives of FoodMitra are:

1. Understand restaurant-related questions using natural language.
2. Identify user requirements such as cuisine, budget, and food preference.
3. Retrieve relevant restaurant information from the available knowledge base.
4. Generate useful responses using an LLM.
5. Maintain conversation history for follow-up questions.
6. Provide restaurant locations using Google Maps.
7. Provide a simple and interactive Streamlit interface.
8. Avoid generating restaurant information that is not available in the knowledge base.

---

## 🧠 Key Features

### 🔍 Restaurant Search

Users can search for restaurants based on:

* Cuisine
* Location
* Budget
* Food items
* Vegetarian preference
* Dining type
* Ambience
* Restaurant name

Example:

```text
Suggest vegetarian restaurants in Hyderabad.
```

---

### 🍛 Food-Based Recommendations

Users can search based on specific food items.

Example:

```text
Where can I find good biryani?
```

---

### 💰 Budget-Based Search

Users can specify their preferred price range.

Example:

```text
Suggest a low-budget restaurant for my family.
```

---

### 👨‍👩‍👧 Dining Type

FoodMitra can consider whether the restaurant is suitable for:

* Family
* Friends
* Couple

Example:

```text
Suggest a restaurant suitable for a family dinner.
```

---

### 🥗 Vegetarian Preference

Users can request vegetarian restaurants or vegetarian-friendly options.

Example:

```text
Find vegetarian restaurants.
```

---

### 💬 Conversational Memory

FoodMitra maintains conversation history using LangChain's `InMemoryChatMessageHistory`.

This allows users to ask follow-up questions.

Example:

```text
User: Suggest a biryani restaurant.

AI: Royal Biryani is an option...

User: Is it suitable for families?

AI: Yes, Royal Biryani is suitable for families.
```

---

### 🗺️ Google Maps Integration

FoodMitra extracts restaurant names from the generated response and displays Google Maps links/embeds for the recommended restaurants.

This allows users to easily locate the restaurants.

---

## 🤖 Large Language Model

FoodMitra uses **OpenAI GPT-OSS 120B**, accessed through the **Groq API**.

### Model Details

```text
Model: openai/gpt-oss-120b
Provider/API: Groq
Framework: LangChain
Integration: ChatGroq
```

The model is used for:

* Query rewriting
* Understanding user requirements
* Restaurant recommendation
* Restaurant comparison
* Conversational responses
* Restaurant name extraction

### Architecture

```text
User Query
     ↓
Streamlit Interface
     ↓
LangChain
     ↓
Query Rewriting
     ↓
Restaurant Retrieval
     ↓
Restaurant Context
     ↓
OpenAI GPT-OSS 120B
     ↓
Generated Response
     ↓
Restaurant Name Extraction
     ↓
Google Maps
```

> **Important:** Although the model name is `openai/gpt-oss-120b`, FoodMitra accesses the model through the **Groq API**, not directly through the OpenAI API.

---

## 🔎 Retrieval Approach

FoodMitra currently uses a **lightweight keyword-based retrieval approach**.

The restaurant information is stored as LangChain `Document` objects.

Example:

```python
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
)
```

When the user enters a query, FoodMitra:

1. Rewrites the query into a clear restaurant search query.
2. Compares query words with the restaurant knowledge base.
3. Retrieves matching restaurant documents.
4. Combines the retrieved documents into context.
5. Sends the context along with the question to the LLM.
6. Generates the final answer.

### Retrieval Flow

```text
User Question
      ↓
Query Rewriting
      ↓
Keyword Matching
      ↓
Relevant Restaurant Documents
      ↓
Context Creation
      ↓
LLM
      ↓
Final Response
```

### Note

The current version **does not use FAISS, Chroma, or embedding-based vector search**.

It uses keyword-based retrieval because the project is designed as a lightweight restaurant recommendation assistant.

---

## 🔄 Query Rewriting

Before retrieving restaurant information, the user's question is converted into a clearer search query.

For example:

```text
User Query:
"I need a cheap vegetarian place for my family"

↓
Rewritten Query:

"low price vegetarian family restaurant"
```

Important information such as:

* Location
* Cuisine
* Budget
* Vegetarian preference
* Dining type
* Food items
* Ambience
* Restaurant name

is preserved during query rewriting.

This helps the retrieval process identify relevant restaurant documents.

---

## 🧩 System Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    Streamlit     │
                    │       UI         │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Query Rewriting  │
                    │    LangChain     │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Keyword-Based    │
                    │    Retrieval     │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Restaurant       │
                    │ Knowledge Base   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Context Creation │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ OpenAI GPT-OSS   │
                    │      120B        │
                    │   via Groq API   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Final Restaurant │
                    │    Response      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Google Maps      │
                    │   Integration    │
                    └──────────────────┘
```

---

## 🛠️ Technology Stack

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| Python              | Application development           |
| Streamlit           | User interface                    |
| LangChain           | LLM application framework         |
| LangChain Core      | Prompts, messages and chains      |
| LangChain Community | LangChain components              |
| Groq API            | LLM API access                    |
| OpenAI GPT-OSS 120B | Language model                    |
| Python-dotenv       | Environment variable management   |
| Tiktoken            | Tokenization utilities            |
| Google Maps         | Restaurant location visualization |
| LangSmith           | LLM tracing and monitoring        |

---

## 📚 Python Libraries

The project uses the following main libraries:

```text
streamlit
langchain
langchain-core
langchain-community
langchain-groq
python-dotenv
tiktoken
```

---

## 📂 Project Structure

```text
FoodMitra/
│
├── app.py
├── chain.py
├── requirements.txt
├── README.md
└── .env
```

### `app.py`

Responsible for:

* Streamlit UI
* Sidebar filters
* Chat interface
* Quick search buttons
* Conversation display
* Restaurant summary
* Google Maps integration

### `chain.py`

Responsible for:

* LLM configuration
* Restaurant knowledge base
* Query rewriting
* Keyword retrieval
* Context creation
* Conversation memory
* Response generation
* Restaurant name extraction

### `requirements.txt`

Contains all required Python dependencies.

### `.env`

Stores API keys locally.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FoodMitra.git
```

Move into the project directory:

```bash
cd FoodMitra
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Keys

Create a `.env` file in the project root directory.

```text
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

`LANGCHAIN_API_KEY` is optional if LangSmith tracing is not required.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💻 Example Queries

Users can ask questions such as:

```text
Suggest vegetarian restaurants in Hyderabad.
```

```text
Where can I get biryani?
```

```text
Suggest a low-budget restaurant for family.
```

```text
Which restaurant is suitable for friends?
```

```text
I want an Italian restaurant.
```

```text
Suggest a cozy cafe for a couple.
```

```text
Compare Spice Garden and Royal Biryani.
```

---

## 📊 Sample Restaurant Knowledge Base

The current knowledge base contains restaurant information such as:

### Spice Garden

```text
Location: Hyderabad
Cuisine: Indian
Food: Biryani, Paneer Tikka, Butter Naan, Veg Biryani
Price: Medium
Suitable for: Family, Friends
Vegetarian: Yes
Ambience: Comfortable and family friendly
```

### Green Leaf

```text
Location: Hyderabad
Cuisine: South Indian
Food: Dosa, Idli, Vada, South Indian Meals
Price: Low
Suitable for: Family
Vegetarian: Yes
Ambience: Simple and peaceful
```

### Arabian Nights

```text
Location: Hyderabad
Cuisine: Arabian
Food: Chicken Mandi, Shawarma, Grilled Chicken
Price: High
Suitable for: Friends, Family
Vegetarian: Limited
Ambience: Modern and spacious
```

### Pizza Corner

```text
Location: Hyderabad
Cuisine: Italian
Food: Pizza, Pasta, Garlic Bread
Price: Medium
Suitable for: Friends, Couple
Vegetarian: Yes
Ambience: Casual
```

### Royal Biryani

```text
Location: Hyderabad
Cuisine: Indian
Food: Chicken Biryani, Mutton Biryani, Veg Biryani
Price: Medium
Suitable for: Family, Friends
Vegetarian: Yes
Ambience: Traditional
```

### Cafe Bliss

```text
Location: Hyderabad
Cuisine: Cafe
Food: Coffee, Sandwiches, Burgers, Desserts
Price: Low
Suitable for: Couple, Friends
Vegetarian: Yes
Ambience: Relaxed and cozy
```

---

## 🧠 LangChain Workflow

FoodMitra uses LangChain to connect the different components of the application.

The major workflow is:

```text
Prompt Template
      ↓
LLM
      ↓
Output Parser
      ↓
Retrieval
      ↓
Context
      ↓
Final Prompt
      ↓
LLM Response
```

The application also uses:

* `ChatPromptTemplate`
* `MessagesPlaceholder`
* `InMemoryChatMessageHistory`
* `HumanMessage`
* `AIMessage`
* `Document`
* `StrOutputParser`

---

## 💾 Conversation Memory

FoodMitra uses:

```python
InMemoryChatMessageHistory
```

to store conversation messages during the active application session.

The conversation history is passed to the LLM along with the current question.

This allows the assistant to understand follow-up questions.

Example:

```text
User:
Suggest a biryani restaurant.

Assistant:
Royal Biryani is available.

User:
Is it vegetarian?

Assistant:
Royal Biryani also offers Veg Biryani.
```

---

## 🔬 LangSmith Integration

FoodMitra supports **LangSmith tracing** for monitoring and debugging LLM operations.

Tracing can help inspect:

* LLM calls
* Prompt execution
* Query rewriting
* Response generation
* Chain execution
* Errors

Environment variables:

```text
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AI_Restaurant_Planner
```

---

## 🚀 Deployment

FoodMitra can be deployed using platforms such as:

* Hugging Face Spaces
* Streamlit-compatible hosting platforms
* Cloud deployment platforms

For Hugging Face Spaces, API keys should be added through **Space Secrets** instead of uploading the `.env` file.

Required secret:

```text
GROQ_API_KEY
```

Optional:

```text
LANGCHAIN_API_KEY
```

---

## 🔒 Security

API keys should never be hardcoded in Python files.

Avoid:

```python
GROQ_API_KEY = "my-secret-key"
```

Instead use environment variables:

```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

Also, do not upload `.env` to GitHub.

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---
🚀 Live Demo

Try the deployed FoodMitra application here:

👉 🍽️ Launch FoodMitra – Live Demo

Platform: Hugging Face Spaces

Application: Streamlit-based AI Restaurant Recommendation Assistant

## 🔮 Future Enhancements

The current version uses a small in-memory restaurant knowledge base and keyword-based retrieval.

Future versions can include:

### 1. Vector Database

Replace keyword retrieval with:

* FAISS
* ChromaDB
* Qdrant

This would allow semantic search.

### 2. Embeddings

Restaurant descriptions can be converted into vector embeddings for better similarity-based retrieval.

### 3. Real-Time Restaurant Data

The system can be connected to restaurant APIs to retrieve:

* Current restaurant information
* Opening hours
* Ratings
* Reviews
* Availability
* Updated menus

### 4. Advanced Filtering

Add filters for:

* Rating
* Distance
* Delivery
* Opening hours
* Specific dishes
* Dietary requirements

### 5. Restaurant Reviews

The system could retrieve and summarize customer reviews.

### 6. Better Location Search

Integrate a location service to find restaurants based on the user's selected area.

---

## 📈 Current System vs Future System

| Feature         | Current Version              | Future Version           |
| --------------- | ---------------------------- | ------------------------ |
| Retrieval       | Keyword-based                | Vector/semantic search   |
| Knowledge Base  | In-memory documents          | Database/vector DB       |
| LLM             | OpenAI GPT-OSS 120B via Groq | Configurable LLM         |
| Memory          | In-memory                    | Persistent memory        |
| Restaurant Data | Static                       | Real-time                |
| Maps            | Google Maps                  | Advanced location search |
| Reviews         | Not available                | Review integration       |
| Ratings         | Not available                | Rating integration       |

---



## 🏁 Conclusion

FoodMitra demonstrates how an AI-powered conversational application can be developed to simplify restaurant discovery.

The application combines **Streamlit for the interface, LangChain for orchestration, keyword-based retrieval for restaurant information, OpenAI GPT-OSS 120B through the Groq API for natural-language generation, conversational memory for follow-up questions, and Google Maps for restaurant locations**.

The project provides a foundation that can be extended into a more advanced restaurant discovery platform using vector databases, embeddings, real-time restaurant APIs, ratings, reviews, and location-based search.

---

## 👩‍💻 Author

**Ramireddy Ambika**

B.Tech – Computer Science & Engineering
Specialization: Data Science

### Project

**FoodMitra – AI Restaurant Recommendation Assistant**
