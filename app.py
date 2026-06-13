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
    user_message = request.form.get("message", "").lower()
    for key in career_responses:
        if key in user_message:
            return jsonify({"response": career_responses[key]})
    return jsonify({"response": "🤖 Sorry, I didn’t understand. Try asking about resume, interview, courses, or skills."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
