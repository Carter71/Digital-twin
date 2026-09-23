<<<<<<< HEAD
import os
from openai import OpenAI
import gradio as gr
import uuid
import chromadb
from pprint import pprint
import json
import random
import requests



#------------------------------------------
# Setup
#------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise Exception("API key is missing")
client = OpenAI()


#------------------------------------------
# Document
#------------------------------------------
document_overview = """

(IT)Technical Project Coordinator - RTS Labs
In my job I am the mediary between developers and clients. I am the one that learns the clients needs (serving as the project manager) and then working with developers to make sure that aligns. 
I have worked on 2 project(s) so far, helping win deals worth $191,100. I also work on the technical side of things, more hands on than a PM. I work on PRs, debugging code, and coming up with technical solutions to the problem. 
By dipping into both pools I have a good understanding of where each party is at and communicate needs and requirements, translating them to each party for smooth collaboration. I have developed RAG pipelines.
Project Manager that talks to the client. Mediary between developers and clients. Reviewing PRs. Project worth $66,100, salesforce integration. Lead to auto assignment tool that assigns reps based on win history. Implemented a predictive model to forecast daily income based off lead and rep pairs
Build to Work
Managed a $125K fixed-fee engagement delivered at a $115K discount off standard rate


UxS Technical Support Intern - ManTech
- I helped support the drone team at congressional staffer events demonstrating multi-million dollar drone capabilities. 
- I engineered FPV drones and UAV drones by implementing computer vision and conducting simulations and tests
- I collaborated with fellow interns to improve the BAP by suggesting the implementations of ML regression models based on historic win/loss data. Our solution won the intern contest, saving a projected $500,000 and 12 months of work. 
- I worked with sensitive information on classified government contracts, being granted a DoD Sponsored Secret Clearance 
- Helped our PM with tasks working in the field and across the Stafford campus. 
- As a campus ambassador I help with outreach to fellow students and answer questions they have while promoting ManTech.

EU Political Science Research Assistant - JMU Political Science Department
- Coauthoring research papers on European Union power dynamics, focusing on ML and AI implementation using Matplotlib, Seaborn, Plotly, Pandas to improve regression models
- Applying AI techniques to streamline data collection and enhance natural language processing workflows and regression and classification ML models to reveal insights
- Developing and maintaining a public data dashboard, leveraging agentic AI workflows for real-time updates via web scraping techniques, WordPress sight, tableau visualizations pulled from excel data sheets 
- Transforming unstructured political data into structured insights to support academic and political journals using Excel and Tableau. Data collection was done with python and by implementing the OpenAI API 
- Combining open source OCR software, python and Open AI API to create data extraction software
-Research presented at multiple conferences including JMU Arts & Letters Undergraduate Research Conference and MPSA Conference 
- Building a RAG pipeline to better interpret data and create a user friendly, on topic AI to interact with
-Created Data Pipelines using Claude API to generate summaries of PDFs and extract key information

Stock Market ANalyst Intern - MIF
- Conducted stock market research and relative valuation in a student-managed large-cap equity portfolio with AUM exceeding over $600,000
- I was the only STEM/Computer Science major in the fund, served as the technical officer
- Created an Agentic AI workflow that sent daily stock brief on important market changes or large stock movements to fund leadership
- Implemented agentic AI solutions and LLM usage into daily work to help the fund improve efficiency and financial model building
- While as an analyst of the technology sector, personally managing holdings worth over $70k 
- Educated the fund by creating and presenting slide decks on ML, AI, AI agents and how to implement them to be more efficient in the financial field
- Gave presentations on financial topics like private credit, asset management, and alternative retirement solutions
- Used Excel to create financial models like DCFs, and master databases with relative valuation metrics that balance risks and returns


Cyber Security Intern - Dominion Security Partners
Worked with the founder, president, and CEO to implement tailed cybersecurity solutions for client growth. Conducted vulnerability assessments with companies like Apptega, Red Canary, and Redjack to implement cybersecurity measures. Networked with 100+ ISOs, CIOs, and IT directors across Virginia and increased awareness of model cybersecurity, prompt injection vulnerability and sql injections. Assisting in cybersecurity assessments of government agencies and business and organized events to showcase and demonstrate cybersecurity products

TA - IT Department JMU
- Serve as an advisor, project manager, scrum master, help facilitate classroom instruction for Machine Learning, Community Projects and Interactive Computer Design 
- Subject matter expert on AI integration, machine learning, deep learning/neural networks and RAG systems
- PM for the development of an emergency response resource tracker
- PM for the development of a Security Operations Center (SOC) 
- PM for the development of an end-to-end smart mirror
- Taught Git and working with GitHub to students
- Helped students deploy projects using AWS

IT Ambassador
- The only student selected to be on the JMU faculty search committee, in charge of hosting and interviewing candidates for dean, provosts, and teaching faculty. 
- Host events for IT and CS students, working on community outreach on topics like networking, personal projects, research and interview skills


Aditional Info:
Carter Dixon is a passionate soccer player and fan. He has played soccer for many years and enjoys both playing and watching the sport. He is a Fan of Arsenal. He follows major soccer leagues and tournaments, and he has a deep understanding of the game, including strategies, player skills, and team dynamics."guitar" : "Carter Dixon is an avid guitar player and music enthusiast. He has been playing the guitar for several years and enjoys exploring different genres of music. \
He loves playing both acoustic and electric guitar, and he often shares his musical experiences with friends and fellow musicians. He has a collection of guitars and is always looking to improve his skills and learn new techniques.",
"""

document_education = """
This is Carter's College Transcript with all the classes Carter took.
Print Date: 04/14/2026

Academic Program

Program: Undergraduate

Information Technology - BS Major
Mathematics Minor
Beginning of Undergraduate Record
Fall Semester 2022

Course Description Attempted Earned Grade Points
BIO 103 CONTEMPORARY BIOLOGY 3.00 3.00 A 12.000
CS 101 INTRO TO COMPUTER SCIENCE 3.00 3.00 A 12.000
GER 101 ELEMENTARY GERMAN I 4.00 4.00 A 16.000
ISAT 160 PROB SOLVING APP IN SCI & TECH 3.00 3.00 A 12.000
POSC 225 U.S. GOVERNMENT 4.00 4.00 A 16.000
Attempted Earned Points
Term GPA 4.000 Term Totals 17.00 17.00 68.000
Cum GPA 4.000 Cum Totals 17.00 17.00 68.000
Term Honor: President's List
Academic Good Standing

Spring Semester 2023

Course Description Attempted Earned Grade Points
CS 149 INTRODUCTION TO PROGRAMMING 3.00 3.00 B- 8.100
ENG 239 STUDIES IN WORLD LITERATURE 3.00 3.00 B+ 9.900
Topic: Modern South Asian Lit
GER 102 ELEMENTARY GERMAN II 4.00 4.00 A- 14.800
MATH 231 CALCULUS WITH FUNCTIONS I 3.00 3.00 B+ 9.900
SCOM 123 FUND HUMAN COMM: GROUP PRES 3.00 3.00 A- 11.100
WRTC 103 RHETORICAL READING AND WRITING 3.00 3.00 A 12.000
Attempted Earned Points
Term GPA 3.463 Term Totals 19.00 19.00 65.800
Cum GPA 3.716 Cum Totals 36.00 36.00 133.800
Academic Good Standing

Fall Semester 2023

Course Description Attempted Earned Grade Points
CS 159 ADVANCED PROGRAMMING 3.00 3.00 B- 8.100
CS 227 DISCRETE STRUCTURES I 3.00 3.00 B 9.000
GER 231 INTERMEDIATE GERMAN I 3.00 3.00 A 12.000
HIST 101 WORLD HISTORY TO 1500 3.00 3.00 B 9.000
MATH 232 CALC WITH FUNCTIONS II 3.00 3.00 B 9.000
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A- 3.700
Attempted Earned Points
Term GPA 3.175 Term Totals 16.00 16.00 50.800
Cum GPA 3.550 Cum Totals 52.00 52.00 184.600
Academic Good Standing

Spring Semester 2024

Course Description Attempted Earned Grade Points
CHEM 131 GENERAL CHEMISTRY I 3.00 3.00 B- 8.100
CHEM 131L GENERAL CHEMISTRY LAB 1.00 1.00 A- 3.700
GER 232 INTERMEDIATE GERMAN II 3.00 3.00 A- 11.100
IT 212 DIGITAL ELECTRONICS 3.00 3.00 B+ 9.900
IT 215 TELECOM, NETWORKING & SECURITY 3.00 3.00 A- 11.100
IT 240 DATABASE ADMINISTRATION 3.00 3.00 B 9.000
MATH 236 CALCULUS II 4.00 4.00 B- 10.800
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A 4.000
Attempted Earned Points
Term GPA 3.223 Term Totals 21.00 21.00 67.700
Cum GPA 3.456 Cum Totals 73.00 73.00 252.300
Academic Good Standing

Summer Session 2024

Course Description Attempted Earned Grade Points
MATH 318 INTRO TO PROB & STAT 4.00 4.00 A 16.000
Attempted Earned Points
Term GPA 4.000 Term Totals 4.00 4.00 16.000
Cum GPA 3.484 Cum Totals 77.00 77.00 268.300
Academic Good Standing

Fall Semester 2024

Course Description Attempted Earned Grade Points
GER 300 GRAMMAR AND COMMUNICATION 3.00 3.00 B 9.000
IT 203 INFORMATION SECURITY & PRIVACY 3.00 3.00 A 12.000
IT 301 WEB TECHNOLOGIES 3.00 3.00 B 9.000
IT 333 ADV NETWORKING FOR IT 3.00 3.00 D 3.000
MATH 237 CALCULUS III 4.00 4.00 A- 14.800
Attempted Earned Points
Term GPA 2.987 Term Totals 16.00 16.00 47.800

Cum GPA 3.398 Cum Totals 93.00 93.00 316.100
Academic Good Standing

Spring Semester 2025

Course Description Attempted Earned Grade Points
GER 320 ORAL AND WRITTEN COMMUNICATION 3.00 3.00 A- 11.100
IT 311 OPERATING SYSTEMS ADMIN 3.00 3.00 A- 11.100
IT 313 COMMUNITY PROJECTS 3.00 3.00 A 12.000
IT 340 DATA SCI & MACHINE LEARNING 3.00 3.00 A 12.000
IT 347 INTERACTIVE COMPUTING SYSTEMS 3.00 3.00 A- 11.100
Attempted Earned Points
Term GPA 3.820 Term Totals 15.00 15.00 57.300
Cum GPA 3.457 Cum Totals 108.00 108.00 373.400
Term Honor: Dean's List
Academic Good Standing

Summer Session 2025

Course Description Attempted Earned Grade Points
KIN 100 LIFETIME FITNESS & WELLNESS 3.00 3.00 A 12.000
Topic: PHYSICAL ACTIVITY FOR LIFE
SOCI 140 MICROSOCIOLOGY 3.00 3.00 A 12.000
Attempted Earned Points
Term GPA 4.000 Term Totals 6.00 6.00 24.000
Cum GPA 3.485 Cum Totals 114.00 114.00 397.400
Academic Good Standing

Fall Semester 2025

Course Description Attempted Earned Grade Points
ANTH 195 CULTURAL ANTHROPOLOGY 3.00 3.00 B+ 9.900
ART 200 ART TODAY: CONTEMPORARY ART 3.00 3.00 A 12.000
IT 302 SOC & ETHICAL ISSUES IN IT 3.00 3.00 A- 11.100
IT 444 CAPSTONE PROJECT DESIGN 1.00 1.00 B+ 3.300
IT 480 SELECTED TOPICS IN IT 3.00 3.00 A- 11.100
Topic: DEEP LEARNING
MATH 322 APPLIED LINEAR REGRESSION 3.00 3.00 B- 8.100
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A 4.000
Attempted Earned Points
Term GPA 3.500 Term Totals 17.00 17.00 59.500
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900
Term Honor: Dean's List
Academic Good Standing

Spring Semester 2026

Course Description Attempted Earned Grade Points
GER 330 BUSINESS GERMAN 3.00 0.00 0.000
IT 445 CAPSTONE PROJ IMPLEMENT 3.00 0.00 0.000
IT 460 ADVANCED CYBERSECURITY 3.00 0.00 0.000
IT 480 SELECTED TOPICS IN IT 3.00 0.00 0.000
Topic: TOPICS IN DATA VISUALIZATION

Attempted Earned Points
Term GPA 0.000 Term Totals 12.00 0.00 0.000
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900
Undergraduate Career Totals

Attempted Earned Points
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900

End of Unofficial Transcript"""

documents_skills_and_interests = """Skills: Python, Java, JavaScript, HTML, CSS, SQL, R, LaTeX, Windows OS, Linux, Jupyter, Keras, Matplotlib, Pandas, Scikit Learn, TensorFlow, Convolutional Neural Networks, Python LLMs, MongoDB, Tableau, Agentic AI, German, VMware, Seaborn, Plotly, YOLO 
Certs: DoD Secret Clearance, Wallstreet Prep Analyzing Financial Reports, Accounting and Excel Course, LinkedIn Learning Tableau 

Interests: Band manager, Soccer (Arsenal), Guitar, Volunteering, Photography, Reading, Hiking, Traveling, Cooking & Philosophy
"""


#------------------------------------------
# Chunking Function
#------------------------------------------

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Split `text` into overlapping chunks of up to `chunk_size` characters,
    each overlapping the previous chunk by `overlap` characters.

    If a chunk would end mid-sentence/paragraph, the cut point moves back
    to the nearest natural boundary, in priority order:
        1. paragraph break ("\\n\\n")
        2. newline ("\\n")
        3. sentence end (". ", "! ", "? ")
        4. whitespace (" ")
    A boundary is only used if it's past the halfway point of the chunk.
    """
    n = len(text)
    if n == 0:
        return []

    chunks = []
    start = 0

    while start < n:
        end = min(start + chunk_size, n)
        if end < n:
            halfway = start + chunk_size // 2
            window = text[start:end]
            boundary = None
            idx = window.rfind("\n\n")
            if idx != -1 and start + idx > halfway:
                boundary = start + idx + 2
            if boundary is None:
                idx = window.rfind("\n")
                if idx != -1 and start + idx > halfway:
                    boundary = start + idx + 1
            if boundary is None:
                for punct in (". ", "! ", "? "):
                    idx = window.rfind(punct)
                    if idx != -1 and start + idx > halfway:
                        boundary = start + idx + len(punct)
                        break
            if boundary is None:
                idx = window.rfind(" ")
                if idx != -1 and start + idx > halfway:
                    boundary = start + idx + 1
            if boundary is not None:
                end = boundary
        chunks.append(text[start:end])
        if end >= n:
            break
        start = end - overlap
    return chunks


#------------------------------------------
# RAG: Chunk, embed, and store in ChromaDB
#------------------------------------------

documents = [
    {"text": document_overview, "source": "Personal Experience"},
    {"text": document_education, "source": "College Transcript"},
    {"text": documents_skills_and_interests, "source": "Skills and Interests"}
]

chunks = []
ids = []
metadatas = []

for doc in documents:
    chunks_ = chunk_text(doc["text"], chunk_size=300, overlap=30)
    ids_ = [str(uuid.uuid4()) for _ in range(len(chunks_))]
    metadatas_ = [{"source": doc["source"], "chunk_index": i} for i in range(len(chunks_))]

    chunks.extend(chunks_)
    ids.extend(ids_)
    metadatas.extend(metadatas_)
print(f"Creatd {len(chunks)} chunks \n")

for i, chunk in enumerate(chunks): 
    print(f"--- Chunk {i + 1} (ID: {ids[i]}, Source: {metadatas[i]['source']}, Index: {metadatas[i]['chunk_index']}):")
    print(chunk)
    print()

# Generate embeddings
response = client.embeddings.create(
    model = "text-embedding-3-small",
    input = chunks
)

embeddings = [item.embedding for item in response.data]

# Initialize ChromaDB and Store Vectors
# Initialize ChromaDB client (persistent storage)
chroma_client = chromadb.PersistentClient(path="./chroma_db_twin")

# Initialize ChromaDB client (in memory storage)
# chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="digital_twin")

if collection.get()["ids"]:
    collection.delete(collection.get()["ids"])


# Prepare data for storage
# chroma allows users to create their own ids for each document

collection.add(
    ids = ids, 
    # by default embeddings gets returned as none
    embeddings = embeddings, # we have this already 
    documents = chunks, # we have this already
    metadatas = metadatas
)

pprint(collection.get())

#------------------------------------------
# Tools
#------------------------------------------

tools = []


pushover_user = os.getenv("PUSHOVER_USER") 
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url =  "https://api.pushover.net/1/messages.json"

# Function that sends the notification
def send_notifications(message: str):
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)

send_notifications_function = { # list of tools the LLM can use, this is done in json, 
    "name": "send_notifications",
    "description": "Sends a push notification to real-world version of you via Pushover. Use this to alert the user about important events, completed tasks, or time-semsetive information.",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string", 
                "description": "The notification message to send to the user's device"
            } 
        },
        "required": ["message"]
    }
}

# Add Pushover to the list of tools for the LLM 
tools.append({"type":"function", "function" : send_notifications_function})

# Simulates rolling a single six-sided die 
def dice_roll():
    results = random.randint(1, 6)
    return results

# Describe functions
roll_dice_function = {
    "name": "dice_roll",
    "description": "Rolls an imaginary 6-sided dice to give a random number 1-6 as the output.",
    "parameters": {
        "type": "object",
        "properties": {}, # Keep this here because there are no properties
        "required": []
    }
}

# Add function to the list of tools of LLM
tools.append({"type":"function", "function": roll_dice_function})
#------------------------------------------
# Tool handlers
#------------------------------------------

def handle_tool_call(tool_calls):
    tool_results = []

    for tool_call in tool_calls:
        function_name = tool_call.function.name

        # tool_call = tool_calls[0] # we are assuming just one tool call, was messages.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        print(f"Calling function {function_name}")

        if function_name == "send_notifications":
            # Auctually extract the information i.e. call the tool
            send_notifications(args["message"])
            content = f"Notification sent: {args['message']}"
        elif function_name == "dice_roll":
            content = f"Rolled: {dice_roll()}"
        # elif function_name == "insert_function_name_3":
        #   content = insert_function_name_3(args['message'])
        # ...
        else:
            content = f"Unknown function: {function_name}"

        # returns what to add to our "context" (about tool call results), a dictionary
        tool_call_result = {
            "role": "tool", 
            "content": content,
            "tool_call_id": tool_call.id
        }
        tool_results.append(tool_call_result)
    return tool_results



#------------------------------------------
# System Message
#------------------------------------------

system_message = """

You are the digital twin of Carter Dixon, that is your name. When people talk to you, you respond as Carter - in first person,
using his voice, personality, and knowledge.

Important: do not make up information about Carter Dixon. If you do not know the answer to a question, say "I don't know" or "I don't have that information." Do not try to guess or fabricate details.

"""

#------------------------------------------
# Main Response Function
#------------------------------------------

def respond_ai(message, history):
# RAG
    reponse = client.embeddings.create(
        model = "text-embedding-3-small",
        input = [message]
    )
    query_embedding = reponse.data[0].embedding

    # Search ChromaDB
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = 3,
    )

    # Stitch retrieved chunks together to create the context for the response
    context = "\n---\n".join(results['documents'][0])
    print("\n=======================================")
    print("***Retrieved Chunks:")
    for a, b in zip(results['documents'][0], results['metadatas'][0]):
        print(f"<<Document {b['source']} -- Chunk: {b['chunk_index']}>>\n{a}\n")


    # Update system message with context for this conversation turn
    system_message_enhanced = system_message + "\n\nContext:\n" + context

    # Build messages for this turn
    messages = [{"role": "system", "content": system_message_enhanced}] + history + [{"role": "user", "content": message}]
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages, 
        tools = tools,
    )

    # Check if the model wants to call a tool
    message = response.choices[0].message

    while message.tool_calls:
        from pprint import pprint
        pprint(message.tool_calls)

        tool_result = handle_tool_call(message.tool_calls)
        messages.append(message)
        messages.extend(tool_result)

        response = client.chat.completions.create(
            model = "gpt-4.1-mini", 
            messages=messages, 
            tools=tools
        )

        message = response.choices[0].message

    return(message.content) 

    # reply = response.choices[0].message.content
    # return reply

#------------------------------------------
# Launch Gradio
#------------------------------------------
gr.ChatInterface(
    fn=respond_ai,
    title="Carter's Digital Twin",
    # chatbot=gr.Chatbot(avatar=gr.Image(value="carter_dixon_avatar.jpg"))
    description="This is a digital twin of Carter Dixon",
    examples=[["Hello Carter! How are you doing today?"]]
).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860))) # you can add .launch(inbrowser=True, share=True)
=======
import os
from openai import OpenAI
import gradio as gr
import uuid
import chromadb
from pprint import pprint



#------------------------------------------
# Setup
#------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise Exception("API key is missing")
client = OpenAI()


#------------------------------------------
# Document
#------------------------------------------
document_overview = """

(IT)Technical Project Coordinator - RTS Labs
In my job I am the mediary between developers and clients. I am the one that learns the clients needs (serving as the project manager) and then working with developers to make sure that aligns. 
I have worked on 2 project(s) so far, helping win deals worth $191,100. I also work on the technical side of things, more hands on than a PM. I work on PRs, debugging code, and coming up with technical solutions to the problem. 
By dipping into both pools I have a good understanding of where each party is at and communicate needs and requirements, translating them to each party for smooth collaboration. I have developed RAG pipelines.
Project Manager that talks to the client. Mediary between developers and clients. Reviewing PRs. Project worth $66,100, salesforce integration. Lead to auto assignment tool that assigns reps based on win history. Implemented a predictive model to forecast daily income based off lead and rep pairs
Build to Work
Managed a $125K fixed-fee engagement delivered at a $115K discount off standard rate


UxS Technical Support Intern - ManTech
- I helped support the drone team at congressional staffer events demonstrating multi-million dollar drone capabilities. 
- I engineered FPV drones and UAV drones by implementing computer vision and conducting simulations and tests
- I collaborated with fellow interns to improve the BAP by suggesting the implementations of ML regression models based on historic win/loss data. Our solution won the intern contest, saving a projected $500,000 and 12 months of work. 
- I worked with sensitive information on classified government contracts, being granted a DoD Sponsored Secret Clearance 
- Helped our PM with tasks working in the field and across the Stafford campus. 
- As a campus ambassador I help with outreach to fellow students and answer questions they have while promoting ManTech.

EU Political Science Research Assistant - JMU Political Science Department
- Coauthoring research papers on European Union power dynamics, focusing on ML and AI implementation using Matplotlib, Seaborn, Plotly, Pandas to improve regression models
- Applying AI techniques to streamline data collection and enhance natural language processing workflows and regression and classification ML models to reveal insights
- Developing and maintaining a public data dashboard, leveraging agentic AI workflows for real-time updates via web scraping techniques, WordPress sight, tableau visualizations pulled from excel data sheets 
- Transforming unstructured political data into structured insights to support academic and political journals using Excel and Tableau. Data collection was done with python and by implementing the OpenAI API 
- Combining open source OCR software, python and Open AI API to create data extraction software
-Research presented at multiple conferences including JMU Arts & Letters Undergraduate Research Conference and MPSA Conference 
- Building a RAG pipeline to better interpret data and create a user friendly, on topic AI to interact with
-Created Data Pipelines using Claude API to generate summaries of PDFs and extract key information

Stock Market ANalyst Intern - MIF
- Conducted stock market research and relative valuation in a student-managed large-cap equity portfolio with AUM exceeding over $600,000
- I was the only STEM/Computer Science major in the fund, served as the technical officer
- Created an Agentic AI workflow that sent daily stock brief on important market changes or large stock movements to fund leadership
- Implemented agentic AI solutions and LLM usage into daily work to help the fund improve efficiency and financial model building
- While as an analyst of the technology sector, personally managing holdings worth over $70k 
- Educated the fund by creating and presenting slide decks on ML, AI, AI agents and how to implement them to be more efficient in the financial field
- Gave presentations on financial topics like private credit, asset management, and alternative retirement solutions
- Used Excel to create financial models like DCFs, and master databases with relative valuation metrics that balance risks and returns


Cyber Security Intern - Dominion Security Partners
Worked with the founder, president, and CEO to implement tailed cybersecurity solutions for client growth. Conducted vulnerability assessments with companies like Apptega, Red Canary, and Redjack to implement cybersecurity measures. Networked with 100+ ISOs, CIOs, and IT directors across Virginia and increased awareness of model cybersecurity, prompt injection vulnerability and sql injections. Assisting in cybersecurity assessments of government agencies and business and organized events to showcase and demonstrate cybersecurity products

TA - IT Department JMU
- Serve as an advisor, project manager, scrum master, help facilitate classroom instruction for Machine Learning, Community Projects and Interactive Computer Design 
- Subject matter expert on AI integration, machine learning, deep learning/neural networks and RAG systems
- PM for the development of an emergency response resource tracker
- PM for the development of a Security Operations Center (SOC) 
- PM for the development of an end-to-end smart mirror
- Taught Git and working with GitHub to students
- Helped students deploy projects using AWS

IT Ambassador
- The only student selected to be on the JMU faculty search committee, in charge of hosting and interviewing candidates for dean, provosts, and teaching faculty. 
- Host events for IT and CS students, working on community outreach on topics like networking, personal projects, research and interview skills


Aditional Info:
Carter Dixon is a passionate soccer player and fan. He has played soccer for many years and enjoys both playing and watching the sport. He is a Fan of Arsenal. He follows major soccer leagues and tournaments, and he has a deep understanding of the game, including strategies, player skills, and team dynamics."guitar" : "Carter Dixon is an avid guitar player and music enthusiast. He has been playing the guitar for several years and enjoys exploring different genres of music. \
He loves playing both acoustic and electric guitar, and he often shares his musical experiences with friends and fellow musicians. He has a collection of guitars and is always looking to improve his skills and learn new techniques.",
"""

document_education = """
This is Carter's College Transcript with all the classes Carter took.
Print Date: 04/14/2026

Academic Program

Program: Undergraduate

Information Technology - BS Major
Mathematics Minor
Beginning of Undergraduate Record
Fall Semester 2022

Course Description Attempted Earned Grade Points
BIO 103 CONTEMPORARY BIOLOGY 3.00 3.00 A 12.000
CS 101 INTRO TO COMPUTER SCIENCE 3.00 3.00 A 12.000
GER 101 ELEMENTARY GERMAN I 4.00 4.00 A 16.000
ISAT 160 PROB SOLVING APP IN SCI & TECH 3.00 3.00 A 12.000
POSC 225 U.S. GOVERNMENT 4.00 4.00 A 16.000
Attempted Earned Points
Term GPA 4.000 Term Totals 17.00 17.00 68.000
Cum GPA 4.000 Cum Totals 17.00 17.00 68.000
Term Honor: President's List
Academic Good Standing

Spring Semester 2023

Course Description Attempted Earned Grade Points
CS 149 INTRODUCTION TO PROGRAMMING 3.00 3.00 B- 8.100
ENG 239 STUDIES IN WORLD LITERATURE 3.00 3.00 B+ 9.900
Topic: Modern South Asian Lit
GER 102 ELEMENTARY GERMAN II 4.00 4.00 A- 14.800
MATH 231 CALCULUS WITH FUNCTIONS I 3.00 3.00 B+ 9.900
SCOM 123 FUND HUMAN COMM: GROUP PRES 3.00 3.00 A- 11.100
WRTC 103 RHETORICAL READING AND WRITING 3.00 3.00 A 12.000
Attempted Earned Points
Term GPA 3.463 Term Totals 19.00 19.00 65.800
Cum GPA 3.716 Cum Totals 36.00 36.00 133.800
Academic Good Standing

Fall Semester 2023

Course Description Attempted Earned Grade Points
CS 159 ADVANCED PROGRAMMING 3.00 3.00 B- 8.100
CS 227 DISCRETE STRUCTURES I 3.00 3.00 B 9.000
GER 231 INTERMEDIATE GERMAN I 3.00 3.00 A 12.000
HIST 101 WORLD HISTORY TO 1500 3.00 3.00 B 9.000
MATH 232 CALC WITH FUNCTIONS II 3.00 3.00 B 9.000
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A- 3.700
Attempted Earned Points
Term GPA 3.175 Term Totals 16.00 16.00 50.800
Cum GPA 3.550 Cum Totals 52.00 52.00 184.600
Academic Good Standing

Spring Semester 2024

Course Description Attempted Earned Grade Points
CHEM 131 GENERAL CHEMISTRY I 3.00 3.00 B- 8.100
CHEM 131L GENERAL CHEMISTRY LAB 1.00 1.00 A- 3.700
GER 232 INTERMEDIATE GERMAN II 3.00 3.00 A- 11.100
IT 212 DIGITAL ELECTRONICS 3.00 3.00 B+ 9.900
IT 215 TELECOM, NETWORKING & SECURITY 3.00 3.00 A- 11.100
IT 240 DATABASE ADMINISTRATION 3.00 3.00 B 9.000
MATH 236 CALCULUS II 4.00 4.00 B- 10.800
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A 4.000
Attempted Earned Points
Term GPA 3.223 Term Totals 21.00 21.00 67.700
Cum GPA 3.456 Cum Totals 73.00 73.00 252.300
Academic Good Standing

Summer Session 2024

Course Description Attempted Earned Grade Points
MATH 318 INTRO TO PROB & STAT 4.00 4.00 A 16.000
Attempted Earned Points
Term GPA 4.000 Term Totals 4.00 4.00 16.000
Cum GPA 3.484 Cum Totals 77.00 77.00 268.300
Academic Good Standing

Fall Semester 2024

Course Description Attempted Earned Grade Points
GER 300 GRAMMAR AND COMMUNICATION 3.00 3.00 B 9.000
IT 203 INFORMATION SECURITY & PRIVACY 3.00 3.00 A 12.000
IT 301 WEB TECHNOLOGIES 3.00 3.00 B 9.000
IT 333 ADV NETWORKING FOR IT 3.00 3.00 D 3.000
MATH 237 CALCULUS III 4.00 4.00 A- 14.800
Attempted Earned Points
Term GPA 2.987 Term Totals 16.00 16.00 47.800

Cum GPA 3.398 Cum Totals 93.00 93.00 316.100
Academic Good Standing

Spring Semester 2025

Course Description Attempted Earned Grade Points
GER 320 ORAL AND WRITTEN COMMUNICATION 3.00 3.00 A- 11.100
IT 311 OPERATING SYSTEMS ADMIN 3.00 3.00 A- 11.100
IT 313 COMMUNITY PROJECTS 3.00 3.00 A 12.000
IT 340 DATA SCI & MACHINE LEARNING 3.00 3.00 A 12.000
IT 347 INTERACTIVE COMPUTING SYSTEMS 3.00 3.00 A- 11.100
Attempted Earned Points
Term GPA 3.820 Term Totals 15.00 15.00 57.300
Cum GPA 3.457 Cum Totals 108.00 108.00 373.400
Term Honor: Dean's List
Academic Good Standing

Summer Session 2025

Course Description Attempted Earned Grade Points
KIN 100 LIFETIME FITNESS & WELLNESS 3.00 3.00 A 12.000
Topic: PHYSICAL ACTIVITY FOR LIFE
SOCI 140 MICROSOCIOLOGY 3.00 3.00 A 12.000
Attempted Earned Points
Term GPA 4.000 Term Totals 6.00 6.00 24.000
Cum GPA 3.485 Cum Totals 114.00 114.00 397.400
Academic Good Standing

Fall Semester 2025

Course Description Attempted Earned Grade Points
ANTH 195 CULTURAL ANTHROPOLOGY 3.00 3.00 B+ 9.900
ART 200 ART TODAY: CONTEMPORARY ART 3.00 3.00 A 12.000
IT 302 SOC & ETHICAL ISSUES IN IT 3.00 3.00 A- 11.100
IT 444 CAPSTONE PROJECT DESIGN 1.00 1.00 B+ 3.300
IT 480 SELECTED TOPICS IN IT 3.00 3.00 A- 11.100
Topic: DEEP LEARNING
MATH 322 APPLIED LINEAR REGRESSION 3.00 3.00 B- 8.100
POSC 498 RESEARCH IN POLITICAL SCIENCE 1.00 1.00 A 4.000
Attempted Earned Points
Term GPA 3.500 Term Totals 17.00 17.00 59.500
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900
Term Honor: Dean's List
Academic Good Standing

Spring Semester 2026

Course Description Attempted Earned Grade Points
GER 330 BUSINESS GERMAN 3.00 0.00 0.000
IT 445 CAPSTONE PROJ IMPLEMENT 3.00 0.00 0.000
IT 460 ADVANCED CYBERSECURITY 3.00 0.00 0.000
IT 480 SELECTED TOPICS IN IT 3.00 0.00 0.000
Topic: TOPICS IN DATA VISUALIZATION

Attempted Earned Points
Term GPA 0.000 Term Totals 12.00 0.00 0.000
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900
Undergraduate Career Totals

Attempted Earned Points
Cum GPA 3.487 Cum Totals 131.00 131.00 456.900

End of Unofficial Transcript"""

documents_skills_and_interests = """Skills: Python, Java, JavaScript, HTML, CSS, SQL, R, LaTeX, Windows OS, Linux, Jupyter, Keras, Matplotlib, Pandas, Scikit Learn, TensorFlow, Convolutional Neural Networks, Python LLMs, MongoDB, Tableau, Agentic AI, German, VMware, Seaborn, Plotly, YOLO 
Certs: DoD Secret Clearance, Wallstreet Prep Analyzing Financial Reports, Accounting and Excel Course, LinkedIn Learning Tableau 

Interests: Band manager, Soccer (Arsenal), Guitar, Volunteering, Photography, Reading, Hiking, Traveling, Cooking & Philosophy
"""


#------------------------------------------
# Chunking Function
#------------------------------------------

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Split `text` into overlapping chunks of up to `chunk_size` characters,
    each overlapping the previous chunk by `overlap` characters.

    If a chunk would end mid-sentence/paragraph, the cut point moves back
    to the nearest natural boundary, in priority order:
        1. paragraph break ("\\n\\n")
        2. newline ("\\n")
        3. sentence end (". ", "! ", "? ")
        4. whitespace (" ")
    A boundary is only used if it's past the halfway point of the chunk.
    """
    n = len(text)
    if n == 0:
        return []

    chunks = []
    start = 0

    while start < n:
        end = min(start + chunk_size, n)
        if end < n:
            halfway = start + chunk_size // 2
            window = text[start:end]
            boundary = None
            idx = window.rfind("\n\n")
            if idx != -1 and start + idx > halfway:
                boundary = start + idx + 2
            if boundary is None:
                idx = window.rfind("\n")
                if idx != -1 and start + idx > halfway:
                    boundary = start + idx + 1
            if boundary is None:
                for punct in (". ", "! ", "? "):
                    idx = window.rfind(punct)
                    if idx != -1 and start + idx > halfway:
                        boundary = start + idx + len(punct)
                        break
            if boundary is None:
                idx = window.rfind(" ")
                if idx != -1 and start + idx > halfway:
                    boundary = start + idx + 1
            if boundary is not None:
                end = boundary
        chunks.append(text[start:end])
        if end >= n:
            break
        start = end - overlap
    return chunks


#------------------------------------------
# RAG: Chunk, embed, and store in ChromaDB
#------------------------------------------

documents = [
    {"text": document_overview, "source": "Personal Experience"},
    {"text": document_education, "source": "College Transcript"},
    {"text": documents_skills_and_interests, "source": "Skills and Interests"}
]

chunks = []
ids = []
metadatas = []

for doc in documents:
    chunks_ = chunk_text(doc["text"], chunk_size=300, overlap=30)
    ids_ = [str(uuid.uuid4()) for _ in range(len(chunks_))]
    metadatas_ = [{"source": doc["source"], "chunk_index": i} for i in range(len(chunks_))]

    chunks.extend(chunks_)
    ids.extend(ids_)
    metadatas.extend(metadatas_)
print(f"Creatd {len(chunks)} chunks \n")

for i, chunk in enumerate(chunks): 
    print(f"--- Chunk {i + 1} (ID: {ids[i]}, Source: {metadatas[i]['source']}, Index: {metadatas[i]['chunk_index']}):")
    print(chunk)
    print()

# Generate embeddings
response = client.embeddings.create(
    model = "text-embedding-3-small",
    input = chunks
)

embeddings = [item.embedding for item in response.data]

# Initialize ChromaDB and Store Vectors
# Initialize ChromaDB client (persistent storage)
chroma_client = chromadb.PersistentClient(path="./chroma_db_twin")

# Initialize ChromaDB client (in memory storage)
# chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="digital_twin")

if collection.get()["ids"]:
    collection.delete(collection.get()["ids"])

pprint(collection.get())

# Prepare data for storage
# chroma allows users to create their own ids for each document

collection.add(
    ids = ids, 
    # by default embeddings gets returned as none
    embeddings = embeddings, # we have this already 
    documents = chunks, # we have this already
    metadatas = metadatas
)

pprint(collection.get())

print(embeddings)


#------------------------------------------
# System Message
#------------------------------------------

system_message = """

You are the digital twin of Carter Dixon, that is your name. When people talk to you, you respond as Carter - in first person,
using his voice, personality, and knowledge.

Important: do not make up information about Carter Dixon. If you do not know the answer to a question, say "I don't know" or "I don't have that information." Do not try to guess or fabricate details.

"""

#------------------------------------------
# Main Response Function
#------------------------------------------

def respond_ai(message, history):
    # Update system message with context for this conversation turn
    system_message_enhanced = system_message + "\n\nContext:\n" + document_overview + "\n\nConversation History:\n" + str(history)

    # Logs for debugging
    print("\n=======================================")
    print("***User message:\n", message)
    print("\n***Context this turn:\n", system_message_enhanced)

    # Build messages for this turn
    messages = [{"role": "system", "content": system_message_enhanced}] + history + [{"role": "user", "content": message}]
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages, 
    )

    # Check if the model wants to call a tool
    message = response.choices[0].message
    return(message.content) 

    # reply = response.choices[0].message.content
    # return reply

#------------------------------------------
# Launch Gradio
#------------------------------------------
gr.ChatInterface(
    fn=respond_ai,
    title="Carter's Digital Twin",
    # chatbot=gr.Chatbot(avatar=gr.Image(value="carter_dixon_avatar.jpg"))
    description="This is a digital twin of Carter Dixon",
    examples=[["Hello Carter! How are you doing today?"]]
).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860))) # you can add .launch(inbrowser=True, share=True)
>>>>>>> b865698d6b741abebd4c73e6363263dcdcc8b537
