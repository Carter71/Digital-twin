import os
from openai import OpenAI
import gradio as gr



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
