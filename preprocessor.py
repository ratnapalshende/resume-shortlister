from tika import parser
import nltk
import re

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords

def clean(text):
    line_words = re.sub(pattern=r'[^a-zA-Z]+', repl=' ', string=text).lower().split()
    line_words = [word for word in line_words if (not word in set(stopwords.words('english')))]
    return " ".join(set(line_words))

def read_pdf(file):
    parsed = parser.from_buffer(file)
    text = parsed["content"]
    cleaned_text = clean(text)
    return cleaned_text
    

def get_score(skills, resume_text):
    # Regular expression to detect words
    words = re.findall(r'\b[a-zA-Z]+\b', skills)
    matched_skill_count = 0
    for skill in words:
        if skill.lower() in resume_text :
            print("matched_skill:",skill.lower())
            matched_skill_count +=1
    matching_score = (matched_skill_count / len(words)) * 100
    return matching_score
    #print(f"Matching score: {matching_score:.2f}%")

# test = 'C, Python, Java, Git, Github, Django, Machine learning, Shell scripting, Linux, Networking, Operating System, HTML, CSS'
# print(get_score(test,read_pdf('Ratnapal_shende_resume.pdf')))
