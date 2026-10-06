import streamlit as st
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="General Trivia Quiz",
    page_icon="🌟",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

.question-box {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #cccccc;
    margin: 15px 0;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# GENERAL TRIVIA QUESTION BANK
# ============================================================

questions = {

    "General Knowledge": [

        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Rome", "Berlin"],
            "answer": "Paris",
            "difficulty": "Easy",
            "explanation": "Paris is the capital city of France."
        },

        {
            "question": "How many days are there in a leap year?",
            "options": ["364", "365", "366", "367"],
            "answer": "366",
            "difficulty": "Easy",
            "explanation": "A leap year has 366 days."
        },

        {
            "question": "Which is the largest ocean?",
            "options": [
                "Atlantic Ocean",
                "Indian Ocean",
                "Pacific Ocean",
                "Arctic Ocean"
            ],
            "answer": "Pacific Ocean",
            "difficulty": "Easy",
            "explanation": "The Pacific Ocean is the largest ocean on Earth."
        },

        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars",
            "difficulty": "Easy",
            "explanation": "Mars is commonly called the Red Planet."
        },

        {
            "question": "Who wrote the play Romeo and Juliet?",
            "options": [
                "William Shakespeare",
                "Charles Dickens",
                "Mark Twain",
                "Leo Tolstoy"
            ],
            "answer": "William Shakespeare",
            "difficulty": "Medium",
            "explanation": "William Shakespeare wrote Romeo and Juliet."
        },

        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "India", "Thailand"],
            "answer": "Japan",
            "difficulty": "Medium",
            "explanation": "Japan is traditionally known as the Land of the Rising Sun."
        },

        {
            "question": "Which is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "answer": "2",
            "difficulty": "Medium",
            "explanation": "2 is the smallest prime number."
        },

        {
            "question": "Which is the largest desert in the world?",
            "options": [
                "Sahara Desert",
                "Gobi Desert",
                "Antarctic Desert",
                "Arabian Desert"
            ],
            "answer": "Antarctic Desert",
            "difficulty": "Hard",
            "explanation": "Antarctica is classified as the world's largest desert."
        },

        {
            "question": "Which ancient civilization built Machu Picchu?",
            "options": ["Roman", "Inca", "Egyptian", "Greek"],
            "answer": "Inca",
            "difficulty": "Hard",
            "explanation": "Machu Picchu was built by the Inca civilization."
        },

        {
            "question": "Which language has the most native speakers worldwide?",
            "options": ["English", "Hindi", "Spanish", "Mandarin Chinese"],
            "answer": "Mandarin Chinese",
            "difficulty": "Hard",
            "explanation": "Mandarin Chinese has the largest number of native speakers."
        }
    ],

    "India": [

        {
            "question": "What is the capital of India?",
            "options": [
                "Mumbai",
                "New Delhi",
                "Hyderabad",
                "Chennai"
            ],
            "answer": "New Delhi",
            "difficulty": "Easy",
            "explanation": "New Delhi is the capital of India."
        },

        {
            "question": "Which is the national animal of India?",
            "options": ["Lion", "Tiger", "Elephant", "Peacock"],
            "answer": "Tiger",
            "difficulty": "Easy",
            "explanation": "The Bengal Tiger is India's national animal."
        },

        {
            "question": "Which is the national bird of India?",
            "options": ["Eagle", "Parrot", "Peacock", "Swan"],
            "answer": "Peacock",
            "difficulty": "Easy",
            "explanation": "The Indian Peacock is India's national bird."
        },

        {
            "question": "Which festival is known as the Festival of Lights?",
            "options": ["Holi", "Diwali", "Eid", "Pongal"],
            "answer": "Diwali",
            "difficulty": "Easy",
            "explanation": "Diwali is popularly known as the Festival of Lights."
        },

        {
            "question": "Who was the first Prime Minister of India?",
            "options": [
                "Mahatma Gandhi",
                "Jawaharlal Nehru",
                "Sardar Patel",
                "Dr. B. R. Ambedkar"
            ],
            "answer": "Jawaharlal Nehru",
            "difficulty": "Medium",
            "explanation": "Jawaharlal Nehru was India's first Prime Minister."
        },

        {
            "question": "Which city is known as the Pink City of India?",
            "options": ["Jaipur", "Delhi", "Agra", "Pune"],
            "answer": "Jaipur",
            "difficulty": "Medium",
            "explanation": "Jaipur is popularly called the Pink City."
        },

        {
            "question": "Who wrote the Indian national anthem?",
            "options": [
                "Rabindranath Tagore",
                "Bankim Chandra Chattopadhyay",
                "Sarojini Naidu",
                "Subhash Chandra Bose"
            ],
            "answer": "Rabindranath Tagore",
            "difficulty": "Medium",
            "explanation": "Rabindranath Tagore wrote Jana Gana Mana."
        },

        {
            "question": "Which Indian state has the longest coastline?",
            "options": [
                "Tamil Nadu",
                "Gujarat",
                "Kerala",
                "Andhra Pradesh"
            ],
            "answer": "Gujarat",
            "difficulty": "Hard",
            "explanation": "Gujarat has the longest coastline among Indian states."
        },

        {
            "question": "Who was the first Indian to win a Nobel Prize?",
            "options": [
                "C. V. Raman",
                "Rabindranath Tagore",
                "Mother Teresa",
                "Amartya Sen"
            ],
            "answer": "Rabindranath Tagore",
            "difficulty": "Hard",
            "explanation": "Rabindranath Tagore won the Nobel Prize in Literature in 1913."
        },

        {
            "question": "Which is the oldest mountain range in India?",
            "options": [
                "Himalayas",
                "Western Ghats",
                "Aravalli Range",
                "Eastern Ghats"
            ],
            "answer": "Aravalli Range",
            "difficulty": "Hard",
            "explanation": "The Aravalli Range is one of the oldest mountain ranges in India."
        }
    ],

    "Science": [

        {
            "question": "What gas do humans need for respiration?",
            "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
            "answer": "Oxygen",
            "difficulty": "Easy",
            "explanation": "Humans need oxygen for cellular respiration."
        },

        {
            "question": "What is H2O commonly called?",
            "options": ["Salt", "Water", "Oxygen", "Hydrogen"],
            "answer": "Water",
            "difficulty": "Easy",
            "explanation": "H2O is the chemical formula for water."
        },

        {
            "question": "How many bones are there in an adult human body?",
            "options": ["196", "206", "216", "226"],
            "answer": "206",
            "difficulty": "Easy",
            "explanation": "A typical adult human skeleton has 206 bones."
        },

        {
            "question": "Which organ pumps blood through the body?",
            "options": ["Brain", "Liver", "Heart", "Lung"],
            "answer": "Heart",
            "difficulty": "Easy",
            "explanation": "The heart pumps blood throughout the body."
        },

        {
            "question": "What force pulls objects toward Earth?",
            "options": ["Friction", "Gravity", "Magnetism", "Pressure"],
            "answer": "Gravity",
            "difficulty": "Medium",
            "explanation": "Gravity attracts objects toward Earth."
        },

        {
            "question": "Which planet has the most prominent ring system?",
            "options": ["Mars", "Saturn", "Earth", "Mercury"],
            "answer": "Saturn",
            "difficulty": "Medium",
            "explanation": "Saturn is famous for its extensive ring system."
        },

        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Ag", "Au", "Gd", "Go"],
            "answer": "Au",
            "difficulty": "Medium",
            "explanation": "Au is the chemical symbol for gold."
        },

        {
            "question": "What is the speed of light in vacuum approximately?",
            "options": [
                "300,000 km/s",
                "30,000 km/s",
                "3,000 km/s",
                "3,000,000 km/s"
            ],
            "answer": "300,000 km/s",
            "difficulty": "Hard",
            "explanation": "Light travels through vacuum at approximately 300,000 km/s."
        },

        {
            "question": "Which particle has a negative electric charge?",
            "options": ["Proton", "Neutron", "Electron", "Photon"],
            "answer": "Electron",
            "difficulty": "Hard",
            "explanation": "Electrons carry a negative electric charge."
        },

        {
            "question": "What is the hardest natural substance?",
            "options": ["Iron", "Diamond", "Quartz", "Graphite"],
            "answer": "Diamond",
            "difficulty": "Hard",
            "explanation": "Diamond is the hardest naturally occurring material on the Mohs scale."
        }
    ],

    "Sports": [

        {
            "question": "How many players are on the field for one cricket team?",
            "options": ["9", "10", "11", "12"],
            "answer": "11",
            "difficulty": "Easy",
            "explanation": "A cricket team has 11 players on the field."
        },

        {
            "question": "Which sport uses a shuttlecock?",
            "options": ["Tennis", "Badminton", "Football", "Hockey"],
            "answer": "Badminton",
            "difficulty": "Easy",
            "explanation": "Badminton is played using a shuttlecock."
        },

        {
            "question": "How many rings are on the Olympic flag?",
            "options": ["4", "5", "6", "7"],
            "answer": "5",
            "difficulty": "Easy",
            "explanation": "The Olympic flag contains five interlocking rings."
        },

        {
            "question": "Which sport is associated with Wimbledon?",
            "options": ["Cricket", "Tennis", "Golf", "Football"],
            "answer": "Tennis",
            "difficulty": "Easy",
            "explanation": "Wimbledon is a famous tennis tournament."
        },

        {
            "question": "How many points is a free throw worth in basketball?",
            "options": ["1", "2", "3", "4"],
            "answer": "1",
            "difficulty": "Medium",
            "explanation": "A successful free throw is worth one point."
        },

        {
            "question": "Which country hosted the first modern Olympic Games?",
            "options": ["France", "Greece", "Italy", "USA"],
            "answer": "Greece",
            "difficulty": "Medium",
            "explanation": "The first modern Olympic Games were held in Athens, Greece, in 1896."
        },

        {
            "question": "In football, how long is a standard match?",
            "options": [
                "60 minutes",
                "75 minutes",
                "90 minutes",
                "120 minutes"
            ],
            "answer": "90 minutes",
            "difficulty": "Medium",
            "explanation": "A standard football match consists of 90 minutes of regulation time."
        },

        {
            "question": "Which country has won the most men's Cricket World Cups?",
            "options": ["India", "Australia", "England", "Pakistan"],
            "answer": "Australia",
            "difficulty": "Hard",
            "explanation": "Australia has won the men's Cricket World Cup more times than any other country."
        },

        {
            "question": "Which chess piece can move in an L-shape?",
            "options": ["Bishop", "Knight", "Rook", "Queen"],
            "answer": "Knight",
            "difficulty": "Hard",
            "explanation": "The knight moves in an L-shaped pattern."
        },

        {
            "question": "In tennis, what is the term for a score of zero?",
            "options": ["Nil", "Love", "Zero", "Blank"],
            "answer": "Love",
            "difficulty": "Hard",
            "explanation": "In tennis scoring, zero is called love."
        }
    ],

    "Movies": [

        {
            "question": "Which movie features the character Jack Sparrow?",
            "options": [
                "Titanic",
                "Pirates of the Caribbean",
                "Avatar",
                "Jurassic Park"
            ],
            "answer": "Pirates of the Caribbean",
            "difficulty": "Easy",
            "explanation": "Jack Sparrow is the main character of Pirates of the Caribbean."
        },

        {
            "question": "Which superhero is also known as Peter Parker?",
            "options": ["Iron Man", "Spider-Man", "Batman", "Superman"],
            "answer": "Spider-Man",
            "difficulty": "Easy",
            "explanation": "Peter Parker is the secret identity of Spider-Man."
        },

        {
            "question": "Which movie is about a ship called Titanic?",
            "options": ["Titanic", "Avatar", "Inception", "Gladiator"],
            "answer": "Titanic",
            "difficulty": "Easy",
            "explanation": "Titanic is a film based around the famous ocean liner."
        },

        {
            "question": "Who played Iron Man in the Marvel Cinematic Universe?",
            "options": [
                "Chris Evans",
                "Robert Downey Jr.",
                "Chris Hemsworth",
                "Tom Holland"
            ],
            "answer": "Robert Downey Jr.",
            "difficulty": "Easy",
            "explanation": "Robert Downey Jr. played Tony Stark/Iron Man."
        },

        {
            "question": "Which movie features the fictional world of Pandora?",
            "options": ["Avatar", "The Matrix", "Inception", "Interstellar"],
            "answer": "Avatar",
            "difficulty": "Medium",
            "explanation": "Pandora is the fictional moon featured in Avatar."
        },

        {
            "question": "Who directed the movie Titanic?",
            "options": [
                "Christopher Nolan",
                "James Cameron",
                "Steven Spielberg",
                "Peter Jackson"
            ],
            "answer": "James Cameron",
            "difficulty": "Medium",
            "explanation": "James Cameron directed Titanic."
        },

        {
            "question": "Which film series features Hogwarts?",
            "options": [
                "Harry Potter",
                "The Hunger Games",
                "The Matrix",
                "Star Wars"
            ],
            "answer": "Harry Potter",
            "difficulty": "Medium",
            "explanation": "Hogwarts is the wizarding school in Harry Potter."
        },

        {
            "question": "Which film won the Academy Award for Best Picture in 1998?",
            "options": [
                "Titanic",
                "The Matrix",
                "Saving Private Ryan",
                "Gladiator"
            ],
            "answer": "Titanic",
            "difficulty": "Hard",
            "explanation": "Titanic won Best Picture at the 70th Academy Awards."
        },

        {
            "question": "Which director made Inception and Interstellar?",
            "options": [
                "James Cameron",
                "Christopher Nolan",
                "Steven Spielberg",
                "Ridley Scott"
            ],
            "answer": "Christopher Nolan",
            "difficulty": "Hard",
            "explanation": "Christopher Nolan directed both Inception and Interstellar."
        },

        {
            "question": "Which Indian film won the Oscar for Best Original Song for 'Naatu Naatu'?",
            "options": [
                "RRR",
                "Baahubali",
                "Pushpa",
                "KGF"
            ],
            "answer": "RRR",
            "difficulty": "Hard",
            "explanation": "The song Naatu Naatu from RRR won the Academy Award for Best Original Song."
        }
    ],

    "Technology": [

        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Control Processing User"
            ],
            "answer": "Central Processing Unit",
            "difficulty": "Easy",
            "explanation": "CPU stands for Central Processing Unit."
        },

        {
            "question": "Which device is commonly used to move the pointer on a computer?",
            "options": ["Keyboard", "Mouse", "Printer", "Speaker"],
            "answer": "Mouse",
            "difficulty": "Easy",
            "explanation": "A mouse is commonly used to control the pointer."
        },

        {
            "question": "What does Wi-Fi allow devices to do?",
            "options": [
                "Connect wirelessly to a network",
                "Print without electricity",
                "Increase screen size",
                "Store physical files"
            ],
            "answer": "Connect wirelessly to a network",
            "difficulty": "Easy",
            "explanation": "Wi-Fi enables wireless network connectivity."
        },

        {
            "question": "Which company developed the Android operating system?",
            "options": ["Google", "Microsoft", "IBM", "Intel"],
            "answer": "Google",
            "difficulty": "Easy",
            "explanation": "Android is developed and maintained by Google."
        },

        {
            "question": "What does URL stand for?",
            "options": [
                "Uniform Resource Locator",
                "Universal Reference Link",
                "User Resource Location",
                "Uniform Routing Link"
            ],
            "answer": "Uniform Resource Locator",
            "difficulty": "Medium",
            "explanation": "URL stands for Uniform Resource Locator."
        },

        {
            "question": "Which storage device uses flash memory?",
            "options": ["SSD", "CD-ROM", "Floppy Disk", "Tape"],
            "answer": "SSD",
            "difficulty": "Medium",
            "explanation": "SSDs use flash memory to store data."
        },

        {
            "question": "Which company created Windows?",
            "options": ["Apple", "Microsoft", "Google", "Oracle"],
            "answer": "Microsoft",
            "difficulty": "Medium",
            "explanation": "Microsoft developed the Windows operating system."
        },

        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Information",
                "Artificial Internet"
            ],
            "answer": "Artificial Intelligence",
            "difficulty": "Hard",
            "explanation": "AI stands for Artificial Intelligence."
        },

        {
            "question": "Which protocol is commonly used to securely browse websites?",
            "options": ["HTTP", "HTTPS", "FTP", "SMTP"],
            "answer": "HTTPS",
            "difficulty": "Hard",
            "explanation": "HTTPS provides encrypted communication for web browsing."
        },

        {
            "question": "Which technology is commonly used for decentralized digital ledgers?",
            "options": [
                "Blockchain",
                "Bluetooth",
                "HTML",
                "RAM"
            ],
            "answer": "Blockchain",
            "difficulty": "Hard",
            "explanation": "Blockchain is a technology used to maintain decentralized digital ledgers."
        }
    ]
}

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "started": False,
    "finished": False,
    "quiz_questions": [],
    "current_question": 0,
    "score": 0,
    "submitted": False,
    "selected_answer": None,
    "answers": [],
    "history": [],
    "category": "",
    "difficulty": "Easy",
    "username": "Player"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# FUNCTIONS
# ============================================================

def reset_quiz():

    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.quiz_questions = []
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.submitted = False
    st.session_state.selected_answer = None
    st.session_state.answers = []


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+", "Outstanding 🌟"

    elif percentage >= 80:
        return "A", "Excellent 🎉"

    elif percentage >= 70:
        return "B", "Very Good 👍"

    elif percentage >= 60:
        return "C", "Good 😊"

    elif percentage >= 50:
        return "D", "Needs Improvement 📚"

    else:
        return "F", "Keep Practicing 💪"


def chatbot_message(percentage):

    if percentage >= 90:
        return "🤖 Amazing! You are a Trivia Master! 🏆"

    elif percentage >= 80:
        return "🤖 Great job! Your general knowledge is excellent!"

    elif percentage >= 60:
        return "🤖 Good work! Keep playing and learning!"

    elif percentage >= 50:
        return "🤖 Nice try! You can improve your score with more practice."

    else:
        return "🤖 Don't worry! Try another quiz and have fun learning!"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🌟 Trivia Quiz")

    page = st.radio(
        "Choose a section:",
        [
            "🏠 Home",
            "🎯 Quiz",
            "🏆 History"
        ]
    )

    st.divider()

    st.write("### 📚 Categories")

    for category_name in questions:
        st.write(f"• {category_name}")

    st.divider()

    st.caption("🌟 General Trivia Quiz")
    st.caption("Powered by Streamlit")


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🌟 General Trivia Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Test your knowledge with fun general questions!'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Categories", len(questions))

    with col2:

        total_questions = sum(
            len(items)
            for items in questions.values()
        )

        st.metric("❓ Questions", total_questions)

    with col3:
        st.metric("🎯 Levels", 3)

    with col4:
        st.metric("🌟 Type", "Trivia")

    st.divider()

    st.subheader("✨ Quiz Features")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### 📚 Multiple Categories")
        st.write(
            "General Knowledge, India, Science, Sports, "
            "Movies and Technology."
        )

        st.write("### 🎯 Three Difficulty Levels")
        st.write("Easy, Medium and Hard.")

        st.write("### 🔀 Random Questions")
        st.write("Questions are randomly selected for every quiz.")

    with col2:

        st.write("### 🚫 No Repeated Questions")
        st.write(
            "The same question will not appear twice "
            "in one quiz."
        )

        st.write("### 💡 Explanations")
        st.write(
            "Learn why the correct answer is correct."
        )

        st.write("### 🏆 Quiz History")
        st.write(
            "View your previous quiz scores."
        )

    st.divider()

    st.info(
        "👉 Select **🎯 Quiz** from the sidebar to start."
    )


# ============================================================
# QUIZ PAGE
# ============================================================

elif page == "🎯 Quiz":

    # --------------------------------------------------------
    # START QUIZ
    # --------------------------------------------------------

    if not st.session_state.started and not st.session_state.finished:

        st.title("🎯 Start Trivia Quiz")

        st.write(
            "Choose a category, difficulty and number of questions."
        )

        st.divider()

        username = st.text_input(
            "👤 Enter your name:",
            value="Player"
        )

        category = st.selectbox(
            "📚 Select Category:",
            list(questions.keys())
        )

        difficulty = st.selectbox(
            "🎯 Select Difficulty:",
            ["Easy", "Medium", "Hard"]
        )

        number_of_questions = st.slider(
            "🔢 Number of Questions:",
            min_value=1,
            max_value=10,
            value=5
        )

        st.divider()

        if st.button(
            "🚀 Start Trivia Quiz",
            use_container_width=True
        ):

            available_questions = [
                q
                for q in questions[category]
                if q["difficulty"] == difficulty
            ]

            if len(available_questions) == 0:

                st.error(
                    "No questions are available for this level."
                )

            else:

                # Randomly select UNIQUE questions
                selected_questions = random.sample(
                    available_questions,
                    min(
                        number_of_questions,
                        len(available_questions)
                    )
                )

                # Make separate option lists
                for q in selected_questions:

                    q["options"] = q["options"].copy()

                    random.shuffle(
                        q["options"]
                    )

                st.session_state.username = username
                st.session_state.category = category
                st.session_state.difficulty = difficulty
                st.session_state.quiz_questions = selected_questions
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.started = True
                st.session_state.finished = False
                st.session_state.submitted = False
                st.session_state.selected_answer = None
                st.session_state.answers = []

                st.rerun()


    # --------------------------------------------------------
    # QUIZ IN PROGRESS
    # --------------------------------------------------------

    elif (
        st.session_state.started
        and not st.session_state.finished
    ):

        total_questions = len(
            st.session_state.quiz_questions
        )

        question_number = (
            st.session_state.current_question
        )

        question_data = (
            st.session_state.quiz_questions[
                question_number
            ]
        )

        st.title("🌟 Trivia Quiz")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(
                f"👤 **{st.session_state.username}**"
            )

        with col2:
            st.write(
                f"📚 **{st.session_state.category}**"
            )

        with col3:
            st.write(
                f"🎯 **{st.session_state.difficulty}**"
            )

        st.divider()

        st.write(
            f"### Question {question_number + 1} "
            f"of {total_questions}"
        )

        progress = (
            (question_number + 1)
            / total_questions
        )

        st.progress(progress)

        st.write(
            f"Progress: {int(progress * 100)}%"
        )

        st.markdown(
            f"""
            <div class="question-box">
                <h2>❓ {question_data['question']}</h2>
                <p>
                    Difficulty:
                    <b>{question_data['difficulty']}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # No "Choose your answer" text
        selected = st.radio(
            "",
            question_data["options"],
            key=f"answer_{question_number}"
        )

        if not st.session_state.submitted:

            if st.button(
                "✅ Submit Answer",
                use_container_width=True
            ):

                st.session_state.selected_answer = selected

                st.session_state.submitted = True

                is_correct = (
                    selected
                    == question_data["answer"]
                )

                if is_correct:
                    st.session_state.score += 1

                st.session_state.answers.append(
                    {
                        "question": question_data["question"],
                        "selected": selected,
                        "correct": question_data["answer"],
                        "is_correct": is_correct,
                        "explanation": question_data["explanation"]
                    }
                )

                st.rerun()

        else:

            if (
                st.session_state.selected_answer
                == question_data["answer"]
            ):

                st.success("🎉 Correct Answer!")

            else:

                st.error(
                    f"❌ Wrong Answer! "
                    f"Correct answer: "
                    f"**{question_data['answer']}**"
                )

            st.info(
                f"💡 **Explanation:** "
                f"{question_data['explanation']}"
            )

            if question_number < total_questions - 1:

                if st.button(
                    "➡️ Next Question",
                    use_container_width=True
                ):

                    st.session_state.current_question += 1
                    st.session_state.submitted = False
                    st.session_state.selected_answer = None

                    st.rerun()

            else:

                if st.button(
                    "🏆 Finish Quiz",
                    use_container_width=True
                ):

                    st.session_state.finished = True
                    st.session_state.started = False

                    percentage = (
                        st.session_state.score
                        / total_questions
                    ) * 100

                    grade, feedback = calculate_grade(
                        percentage
                    )

                    st.session_state.history.append(
                        {
                            "name": st.session_state.username,
                            "category": st.session_state.category,
                            "difficulty": st.session_state.difficulty,
                            "score": st.session_state.score,
                            "total": total_questions,
                            "percentage": percentage,
                            "grade": grade
                        }
                    )

                    st.rerun()


    # --------------------------------------------------------
    # RESULT PAGE
    # --------------------------------------------------------

    elif st.session_state.finished:

        st.title("🏆 Trivia Quiz Result")

        total_questions = len(
            st.session_state.quiz_questions
        )

        score = st.session_state.score

        percentage = (
            score / total_questions
        ) * 100

        grade, feedback = calculate_grade(
            percentage
        )

        st.success(
            f"🎉 Well done, {st.session_state.username}!"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🏆 Score",
                f"{score}/{total_questions}"
            )

        with col2:
            st.metric(
                "📊 Percentage",
                f"{percentage:.1f}%"
            )

        with col3:
            st.metric(
                "🎓 Grade",
                grade
            )

        with col4:
            st.metric(
                "🎯 Level",
                st.session_state.difficulty
            )

        st.write(f"### {feedback}")

        st.info(
            chatbot_message(percentage)
        )

        st.divider()

        st.subheader("📋 Answer Review")

        for index, answer in enumerate(
            st.session_state.answers,
            start=1
        ):

            st.write(
                f"### Question {index}"
            )

            st.write(
                answer["question"]
            )

            if answer["is_correct"]:

                st.success(
                    f"✅ Your answer: "
                    f"{answer['selected']}"
                )

            else:

                st.error(
                    f"❌ Your answer: "
                    f"{answer['selected']}"
                )

                st.info(
                    f"Correct answer: "
                    f"{answer['correct']}"
                )

            st.caption(
                f"💡 {answer['explanation']}"
            )

            st.divider()

        result_text = f"""
GENERAL TRIVIA QUIZ RESULT
==========================

Player: {st.session_state.username}
Category: {st.session_state.category}
Difficulty: {st.session_state.difficulty}

Score: {score}/{total_questions}
Percentage: {percentage:.1f}%
Grade: {grade}

{feedback}
"""

        st.download_button(
            "📥 Download Result",
            result_text,
            file_name="trivia_quiz_result.txt",
            mime="text/plain",
            use_container_width=True
        )

        if st.button(
            "🔄 Play Again",
            use_container_width=True
        ):

            reset_quiz()
            st.rerun()


# ============================================================
# HISTORY PAGE
# ============================================================

elif page == "🏆 History":

    st.title("🏆 Trivia Quiz History")

    if len(st.session_state.history) == 0:

        st.info(
            "No quiz attempts yet. Start a Trivia Quiz!"
        )

    else:

        for index, result in enumerate(
            reversed(st.session_state.history),
            start=1
        ):

            st.write(
                f"### 🎯 Attempt {index}"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write(
                    f"👤 {result['name']}"
                )

            with col2:
                st.write(
                    f"📚 {result['category']}"
                )

            with col3:
                st.write(
                    f"🏆 {result['score']}/{result['total']}"
                )

            with col4:
                st.write(
                    f"📊 {result['percentage']:.1f}%"
                )

            st.divider()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        🌟 <b>General Trivia Quiz</b><br>
        Test your knowledge • Learn • Have Fun 🎉
    </div>
    """,
    unsafe_allow_html=True
)