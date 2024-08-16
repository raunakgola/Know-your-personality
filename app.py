import streamlit as st
import time
import torch

# #Load your trained PyTorch model
model = torch.load('clfr.pth')
model.eval()

# # Define the input preprocessing function
def preprocess_inputs(input: list):
    # Convert inputs to tensor
    inputs = torch.tensor(input, dtype=torch.float32)
    return inputs.unsqueeze(0)  # Add batch dimension

# # Define the prediction function
def predict(inputs, model):
    with torch.no_grad():
        outputs = model(inputs)
    _, predicted = torch.max(outputs, 1)
    return predicted.item()


## UI CODE
INTJ = """INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. 
These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. 
Their inner world is often a private, complex one.
"""
INTP = """INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. 
These flexible thinkers enjoy taking an unconventional approach to many aspects of life. 
They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
"""
ENTJ = """ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits. 
They are decisive people who love momentum and accomplishment. 
They gather information to construct their creative visions but rarely hesitate for long before acting on them.
"""
ENFP = """ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits. 
These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. 
Their vibrant energy can flow in many directions.
"""
ENTP = """ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits. 
They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. 
They pursue their goals vigorously despite any resistance they might encounter.
"""
ESFJ = """ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits. 
They are attentive and people-focused, and they enjoy taking part in their social community. 
Their achievements are guided by decisive values, and they willingly offer guidance to others.
"""
ESFP = """ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits. 
These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. 
They can be very social, often encouraging others into shared activities.
"""
ESTJ = """ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits. 
They possess great fortitude, emphatically following their own sensible judgment. 
They often serve as a stabilizing force among others, able to offer solid direction amid adversity.
"""
ESTP = """ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits. 
They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. 
They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
"""
INFJ = """INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. 
They tend to approach life with deep thoughtfulness and imagination. 
Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.
"""
INFP = """INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. 
These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.
"""
ENFJ = """ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. 
These warm, forthright types love helping others, and they tend to have strong ideas and values. 
They back their perspective with the creative energy to achieve their goals.
"""
ISFJ = """ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits. 
These people tend to be warm and unassuming in their own steady way. 
They’re efficient and responsible, giving careful attention to practical details in their daily lives.
"""
ISFP = """ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits. 
They tend to have open minds, approaching life, new experiences, and people with grounded warmth. 
Their ability to stay in the moment helps them uncover exciting potentials.
"""
ISTJ = """ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits. 
These people tend to be reserved yet willful, with a rational outlook on life. 
They compose their actions carefully and carry them out with methodical purpose.
"""
ISTP = """ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits. 
They tend to have an individualistic mindset, pursuing goals without needing much external connection. 
They engage in life with inquisitiveness and personal skill, varying their approach as needed.
"""
## helper func
fn = lambda x: {
            3: 'Fully Agree',
            2: 'Partially Agree',
            1: 'Slightly Agree',
            0: 'Neutral',
            -1: 'Slightly Disagree',
            -2: 'Partially Disagree',
            -3: 'Fully Disagree'
        }[x]

def stream_data(f):
    text = f
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.2)

def display(title:str,header:str,write1:str,write2,img:str):
    with col1:
        st.title(title)
        st.subheader(header)
        st.write(write1)
        st.write_stream(stream_data(write2))
    with col2:
        st.image(img)


st.set_page_config("Fashion Station",layout='wide')
st.title("Know your personality by giving some answers of question")
col1, col2 = st.columns(2)
with st.sidebar:
    q1 = st.radio('Q1 You regularly make new friends.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q2 = st.radio('Q2 You spend a lot of your free time exploring various random topics that pique your interest', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q3 = st.radio('Q3 Seeing other people cry can easily make you feel like you want to cry too', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q4 = st.radio('Q4 At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q5 = st.radio('Q5 You prefer to completely finish one project before starting another.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q6 = st.radio('Q6 You are very sentimental.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q7 = st.radio('Q7 You like to use organizing tools like schedules and lists.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q8 = st.radio('Q8 You feel comfortable just walking up to someone you find interesting and striking up a conversation.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q9 = st.radio('Q9 You are not too interested in discussing various interpretations and analyses of creative works.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q10 = st.radio('Q10 You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q11 = st.radio('Q11 You rarely worry about whether you make a good impression on people you meet.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q12 = st.radio('Q12 You like books and movies that make you come up with your own interpretation of the ending.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q13 = st.radio('Q13 Your happiness comes more from helping others accomplish things than your own accomplishments.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q14 = st.radio('Q14 You are interested in so many things that you find it difficult to choose what to try next.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q15 = st.radio('Q15 You are prone to worrying that things will take a turn for the worse.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q16 = st.radio('Q15 You avoid leadership roles in group settings.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q17 = st.radio('Q16 You are definitely not an artistic type of person.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q18 = st.radio('Q17 You prefer to do your chores before allowing yourself to relax.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q19 = st.radio('Q18 You enjoy watching people argue.',[-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q20 = st.radio('Q19 You lose patience with people who are not as efficient as you.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q21 = st.radio('Q20 You become bored or lose interest when the discussion gets highly theoretical.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q22 = st.radio('Q21 You usually postpone finalizing decisions for as long as possible.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q23 = st.radio('Q22 After a long and exhausting week, a lively social event is just what you need.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q24 = st.radio('Q23 You enjoy going to art museums.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q25 = st.radio('Q24 You often have a hard time understanding other people’s feelings.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q26 = st.radio('Q25 You rarely feel insecure.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q27 = st.radio('Q26 You avoid making phone calls.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q28 = st.radio('Q27 You are still bothered by mistakes that you made a long time ago.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q29 = st.radio('Q28 You take great care not to make people look bad, even when it is completely their fault.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q30 = st.radio('Q29 You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q31 = st.radio('Q30 You complete things methodically without skipping over any steps.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q32 = st.radio('Q32 You struggle with deadlines.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    q33 = st.radio('Q33 You feel confident that things will work out for you.', [-3,-2,-1,0,1,2,3], format_func=fn,horizontal=True)
    l = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24,q25, q26, q27, q28, q29, q30, q31, q32, q33]

    inputs = preprocess_inputs(l)

    pred = predict(inputs,model)
    if st.button("Predict"):
        if pred==0:
            display("Protagonist","__ENFJ Personality__","**Extraverted Intuitive Feeling  Judging**",ENFJ,"Images/protagonist-desktop1.png")
        elif pred==1:
            display("Campaigner","__ENFP Personality__","**Extraverted Intuitive Feeling Prospecting**",ENFP,"Images/campaigner-desktop1.png")
        elif pred ==2:
            display("Commander","_ENTJ Personality_","**Extraverted Intuitive Thinking Judging**",ENTJ,"Images/commander-desktop1.png")
        elif pred ==3:
            display("Debater","_ENTP Personality_","**Extraverted Intuitive Thinking Prospecting **",ENTP,"Images/debater-desktop1.png")
        elif pred==4:
            display("Consul","__ESFJ Personality__","**Extraverted Observant Feeling Judging**",ESFJ,"Images/consul-desktop1.png")
        elif pred==5:
            display("Entertainer","__ESFP Personality__","** Extraverted Observant Feeling Prospecting**",ESFP,"Images/entertainer-desktop1.png")
        elif pred==6:
            display("Executive","__ESTJ Personality__","**Extraverted Observant Thinking Judging**",ESTJ,"Images/executive-desktop1.png")
        elif pred==7:
            display("Entrepreneur","__ESTP Personality__","**Extraverted Observant Thinking Prospecting**",ESTP,"Images/entrepreneur-desktop1.png")
        elif pred==8:
            display("Advocate","__INFJ Personality__","**Introverted Intuitive Feeling Judging **",INFJ,"Images/advocate-desktop1.png")
        elif pred==9:
            display("Mediator","__INFP Personality__","**Introverted Intuitive Feeling Prospecting**",INFP,"Images/mediator-desktop1.png")
        if pred ==10:
            display("Architect","_INTJ Personality_","**Introverted Intuitive Thinking Judging**",INTJ,"Images/architect-desktop1.png")
        elif pred ==11:
            display("Logician","_INTP Personality_","** Introverted Intuitive Thinking Prospecting **",INTP,"Images/logician-desktop1.png")
        elif pred==12:
            display("Defender","__ISFJ Personality__","**Introverted Observant Feeling Judging**",ISFJ,"Images/defender-desktop1.png")
        elif pred==13:
            display("Adventurer","__ISFP Personality__","** Introverted Observant Feeling Prospecting**",ISFP,"Images/adventurer-desktop1.png")
        elif pred==14:
            display("Logistician","__ISTJ Personality__","**Introverted Observant Thinking Judging**",ISTJ,"Images/logistician-desktop1.png")
        elif pred==15:
            display("Virtuoso","__ISTP Personality__","** Introverted Observant Thinking Prospecting**",ISTP,"Images/virtuoso-desktop1.png")
