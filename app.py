from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

career_responses = {
    "data scientist": """🎯 Data Scientist Roadmap:

1. Learn Python Programming
2. Study Statistics and Probability
3. Learn SQL and Database Management
4. Master Machine Learning Algorithms
5. Work on Data Analysis Projects
6. Build a GitHub Portfolio
7. Gain Internship Experience
8. Prepare for Technical Interviews

💡 Key Skills:
• Python
• Pandas & NumPy
• SQL
• Scikit-learn
• Data Visualization
""",

    "web developer": """🌐 Web Developer Roadmap:

1. Learn HTML, CSS, and JavaScript
2. Master Frontend Frameworks (React)
3. Learn Backend Development (Flask/Node.js)
4. Work with Databases
5. Build Real-world Projects
6. Create a Portfolio Website

💡 Key Skills:
• HTML
• CSS
• JavaScript
• React
• Flask/Node.js
""",

    "ai engineer": """🤖 AI Engineer Roadmap:

1. Learn Python
2. Study Machine Learning
3. Learn Deep Learning
4. Explore NLP and Computer Vision
5. Build AI Projects
6. Stay Updated with Latest AI Trends

💡 Key Skills:
• Python
• TensorFlow/PyTorch
• NLP
• Computer Vision
""",

    "resume": """📄 Resume Tips:

• Keep your resume to 1 page
• Highlight projects and internships
• Mention technical skills clearly
• Include certifications
• Use a clean and professional format
• Customize your resume for each job role
""",

    "interview": """💼 Interview Preparation Tips:

• Practice coding problems regularly
• Prepare aptitude questions
• Improve communication skills
• Attend mock interviews
• Revise core technical concepts
• Research the company before interviews
""",

    "machine learning": """🧠 Machine Learning Roadmap:

1. Learn Python
2. Understand Statistics
3. Study Supervised Learning
4. Explore Unsupervised Learning
5. Work on ML Projects
6. Learn Model Deployment

💡 Key Skills:
• Python
• Scikit-learn
• Statistics
• Data Preprocessing
""",

    "cyber security": """🔒 Cyber Security Roadmap:

1. Learn Networking Fundamentals
2. Study Linux
3. Learn Ethical Hacking
4. Understand Security Analysis
5. Practice Penetration Testing
6. Earn Certifications (CEH, CompTIA Security+)

💡 Key Skills:
• Networking
• Linux
• Ethical Hacking
• Security Tools
""",

    "cloud computing": """☁️ Cloud Computing Roadmap:

1. Learn AWS, Azure, or GCP
2. Understand Virtualization
3. Learn Docker and Kubernetes
4. Practice Cloud Deployment
5. Obtain Cloud Certifications

💡 Key Skills:
• AWS/Azure/GCP
• Docker
• Kubernetes
• CI/CD
""",

    "courses": """📚 Recommended Courses:

• Machine Learning by Andrew Ng (Coursera)
• CS50: Introduction to Computer Science
• Google Data Analytics Certificate
• IBM Data Science Professional Certificate
• Python for Everybody
""",

    "skills": """🚀 Essential Career Skills:

• Communication Skills
• Problem Solving
• Critical Thinking
• Team Collaboration
• Time Management
• Leadership Skills
• Adaptability
"""
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot():
    user_message = request.form["message"].lower()

    for key in career_responses:
        if key in user_message:
            return jsonify({"response": career_responses[key]})

    return jsonify({
        "response": """🤖 Hello! I can help you with:

🎯 Career Guidance
📄 Resume Tips
💼 Interview Preparation
📚 Course Recommendations
🚀 Skills Development

Try asking:
• data scientist
• resume
• interview
• courses
• skills
• ai engineer
• web developer
"""
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
