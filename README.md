# Insightify

<div align="center">

![Insightify](static/logo/symbol_blue.png)

**An AI-Powered Educational Tool for Filipino Students**

*Bridging the reading comprehension gap through technology*

[![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)](LICENSE)

</div>

---

## 📖 About the Project

Insightify is a mobile application and web platform designed to assist Filipino students in comprehending complex texts, addressing the educational challenges highlighted by the Philippines' consistently low rankings in international student reading assessments by the Organization for Economic Co-operation and Development (OECD). 

Despite the widespread use of smartphones in education, this study recognizes that technology access alone does not guarantee improved learning outcomes. Insightify bridges this gap by leveraging cutting-edge **Artificial Intelligence (AI)**, **Natural Language Processing (NLP)**, and **Optical Character Recognition (OCR)** technologies to create an accessible, user-friendly educational tool.

This project contributes to achieving **UN Sustainable Development Goal (SDG) 4: Quality Education** by empowering students with tools to better understand and engage with educational content.

### 🎯 Project Goals

- **Address Reading Comprehension Challenges** - Help Filipino students understand complex academic texts
- **Leverage Mobile Technology** - Utilize the high mobile phone usage rate in the Philippines
- **Seamless User Experience** - Integrate NLP and OCR for intuitive text processing
- **Support Quality Education** - Contribute to UN SDG 4: Quality Education
- **User-Centered Design** - Prioritize feedback and continuous improvement

---

## ✨ Key Features

### Core Text Processing Tools
- **✨ Text Simplification** - Transform complex texts into easier-to-understand content using AI
- **🔄 Paraphrasing** - Rewrite sentences while maintaining original meaning
- **🌐 Translation** - Convert text between multiple languages, supporting multilingual learners
- **📝 Citation Generator** - Generate proper academic citations
- **📚 Flashcard Creation** - Create custom study flashcards for better retention
- **✅ Assessment Tools** - Test comprehension with AI-generated quizzes

### Document Processing Capabilities
- **📸 OCR Support** - Extract text from images and scanned documents
- **📄 PDF Processing** - Import and process PDF documents seamlessly
- **📝 Word Document Support** - Handle .doc and .docx files
- **🖼️ Image-to-Text** - Convert images containing text into editable format

### Learning Management
- **📊 User Dashboard** - Track learning progress and usage statistics
- **💾 Collection Management** - Organize and save processed texts and study materials
- **📱 Mobile-Responsive** - Optimized for smartphones and tablets
- **👥 User Accounts** - Personalized learning experience with secure authentication

---

## 🛠️ Technologies & Architecture

### Backend Framework
- **Django 5.0.6** - Robust Python web framework
- **Django REST Framework** - RESTful API development
- **Python 3.8+** - Core programming language
- **SQLite / PostgreSQL** - Database management

### AI & Natural Language Processing
- **Google Gemini 1.5 Pro** - Advanced AI model for text generation and processing
- **Natural Language Processing (NLP)** - Text analysis and transformation
- **Optical Character Recognition (OCR)** - Document digitization via Tesseract.js
- **Safety Filters** - Content moderation and appropriate output generation

### Frontend Technologies
- **HTML5 / CSS3** - Modern web standards
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **jQuery** - DOM manipulation and AJAX
- **Font Awesome** - Icon library
- **Owl Carousel** - Interactive carousels

### Document Processing Libraries
- **Tesseract.js** - Client-side OCR engine
- **PDF.js** - PDF rendering and text extraction
- **Mammoth.js** - Word document conversion

### DevOps & Configuration
- **python-dotenv** - Environment variable management
- **dj-database-url** - Database configuration for deployment
- **WSGI** - Production-ready deployment

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key ([Get one here](https://ai.google.dev/))
- Git

### Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/benson09121/insig.git
cd insig
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file in the project root:
```env
SECRET_KEY=your_django_secret_key_here
DEBUG=True
GEMINI_API_KEY=your_google_gemini_api_key
# Optional: PostgreSQL configuration
# POSTGRES=your_database_url
```

5. **Run Database Migrations**
```bash
python manage.py migrate
```

6. **Create Superuser (Optional)**
```bash
python manage.py createsuperuser
```

7. **Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

8. **Start Development Server**
```bash
python manage.py runserver
```

9. **Access the Application**
- Open your browser and navigate to: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🚀 Usage Guide

### For Students

#### Text Simplification
1. **Sign up** or **log in** to your account
2. Navigate to the **Dashboard**
3. Select the **Simplify** feature
4. Enter or paste complex text, or upload a document
5. Click **Generate** to simplify the content
6. Review the simplified text and save to your collection

#### Document Upload
- **Images**: Upload photos of textbook pages or handwritten notes
- **PDFs**: Import PDF textbooks or study materials
- **Word Documents**: Process .doc and .docx files directly

#### Study Tools
- Create **flashcards** from simplified content
- Take **assessments** to test comprehension
- **Organize** materials by subject or topic
- **Track progress** through your dashboard

### For Educators

Insightify can be used to:
- Create simplified reading materials for students
- Generate study guides and assessments
- Translate educational content for multilingual classrooms
- Monitor student engagement through the platform

---

## 🔬 Research Methodology

This project was developed using an **Agile methodology**, emphasizing:
- **Iterative Development** - Regular development cycles with continuous improvement
- **User Feedback Integration** - Prioritizing user input for feature refinement
- **Adaptability** - Flexible response to changing requirements
- **User-Centered Design** - Focus on usability and accessibility

### Evaluation Results

User evaluation of Insightify revealed:
- ✅ **High satisfaction** with functionality and user-friendliness
- 📱 **Positive feedback** on mobile responsiveness
- 🎯 **Areas for improvement**: Assessment design, UX enhancements, AI content quality

---

## 🎓 Educational Impact

### Addressing SDG 4: Quality Education

Insightify contributes to UN Sustainable Development Goal 4 by:
- **Improving Access** - Making complex educational content more accessible
- **Supporting Comprehension** - Helping students understand difficult materials
- **Leveraging Technology** - Using AI to democratize quality education
- **Empowering Students** - Providing tools for independent learning

### Target Audience
- **Primary**: Filipino students at various educational levels
- **Secondary**: Educators creating accessible learning materials
- **Tertiary**: ESL learners and multilingual students

---

## 📄 License

This project is developed for educational and research purposes. Please contact the author for usage permissions.

---

## 🔒 Security & Privacy

**Important Notes:**
- 🔐 Keep your `GEMINI_API_KEY` secure and never commit it to version control
- 🛡️ Use environment variables for all sensitive information
- 👤 User data is stored securely and not shared with third parties
- 🔒 API requests are processed with content safety filters

---

<div align="center">

*Empowering education through technology*

</div>
