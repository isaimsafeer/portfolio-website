from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    project_list = [
        {
            "title": "Movie Recommender System",
            "description": "A movie recommendation system based on content filtering, applied data preprocessing, and machine learning.",
            "technologies": ["Python", "SK-Learn", "Streamlit"],
            "SourceCode": "https://github.com/isaimsafeer/movie_recomendation",
            "image": "https://blog.lancedb.com/content/images/size/w1000/2024/05/1_AatBvnpVpEPoQvZAMeqU-A.webp"
        },
        {
            "title": "RAG based Medical Chatbot",
            "description": "A RAG based Chatbot for Medical help, using RAG and Langchain for medical responses.",
            "technologies": ["Python", "OpenAI", "Langchain", "Pinecone", "FASTAPI"],
            "SourceCode": "https://github.com/isaimsafeer/medical_chatbot",
            "image": "https://kms-healthcare.com/wp-content/uploads/2023/10/ai-chatbots-in-healthcare-1-1024x575.png"
        },
        {
            "title": "Brain Tumor Detection",
            "description": "A Brain Tumor Detection system using CNN and Keras, the system was trained on a labeled dataset and achieved high accuracy in distinguishing between tumorous and non-tumorous brain scans",
            "technologies": ["Python", "Tensorflow", "Keras", "FASTAPI", "HTML", "CSS", "JavaScript"],
            "SourceCode": "https://github.com/isaimsafeer",
            "image": "https://media.licdn.com/dms/image/v2/C4D12AQEWHzMrlFh0nQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1651474032780?e=2147483647&v=beta&t=oXw2GMCCQFQ82ldQaVEWNzhh7oMJMoZLYPYkRZjN5KM"
        },
        {
            "title": "Image to Food and Ingredients Recogniton System",
            "description": "Combined Convolutional Neural Networks (CNN) for image recognition with a custom-trained NLP model to generate ingredient lists. Implemented the solution using TensorFlow and Keras for model development.",
            "technologies": ["Python", "Tensorflow", "Keras", "Streamlit"],
            "SourceCode": "https://github.com/isaimsafeer",
            "image": "https://miro.medium.com/v2/resize:fit:2000/format:webp/1*OHZ6ukR4V5FVviY2ne_KIQ.jpeg"
        }
    ]

    # Icon map for technologies
    icon_map = {
        "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "SK-Learn": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg",
        "Streamlit": "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        "OpenAI": "https://www.svgrepo.com/show/306500/openai.svg",
        "Langchain": "https://avatars.githubusercontent.com/u/139914090?s=200&v=4",
        "Pinecone": "https://avatars.githubusercontent.com/u/74971167?s=200&v=4",
        "FASTAPI": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
        "Tensorflow": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg",
        "Keras": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg",
        "HTML": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
        "CSS": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
        "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    }

    # Enrich project data
    enriched_projects = []
    for project in project_list:
        # Add flag for external image
        project["is_external_image"] = project["image"].startswith("http")

        # Add tech details with icons
        project["tech_details"] = []
        for tech in project["technologies"]:
            project["tech_details"].append({
                "name": tech,
                "icon": icon_map.get(tech)
            })

        enriched_projects.append(project)

    return render(request, 'projects.html', {'projects': enriched_projects})


def contact(request):
    return render(request, 'contact.html')


@csrf_exempt
def ask_chatbot(request):
    return render(request, 'chatbot.html')



        