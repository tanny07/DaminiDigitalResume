
import streamlit as st
from PIL import Image 
from streamlit_option_menu import option_menu
import webbrowser


############################################ General Settings ####################################################################

# PAGE LAYOUT

st.set_page_config(
    page_title = "Digital Resume", 
    layout="wide",
    page_icon="✨"
) 
st.title(" Digital Resume ")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

############################################ For Title Bar (Anglais) ##############################################################


col1, col2 = st.columns(2)

with col1:
    st.header("Damini Sharma")
    st.subheader("UI UX Designer")
    st.write("Email : daminisharma9704@gmail.com")

with col2:
    image = Image.open("profile.jpg")
    st.image(image, width= 200)

############################################ Navigation Bar(Angais) ##############################################################

selection = option_menu(None, ["Profile", "Education", "Experience", "Projects"],
                    icons=['badge-tm', 'building', 'briefcase', 'bookmark-check'],
                    menu_icon="cast", default_index=0, orientation="horizontal")

############################################ Proflie Function (Angais) ##############################################################

def profile():

    resume_file = "/Users/tanmaymondkar/Desktop/DaminiDigitalResume/Damini_Resume.pdf"
    with open("Damini_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    with st.sidebar:

        st.markdown('# Links', unsafe_allow_html=True)  

        st.write(" Github : [link](https://github.com/damini29-ps)")
        st.write(" LinkedIn : [link](https://www.linkedin.com/in/daminisharma29)")
        st.write(" Address : [link](https://goo.gl/maps/W9QGsfNSiMxsdRMu7)")
        st.write(" Behance : [link](https://www.behance.net/daminisharma2905)")

        st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name= "DaminiSharmaResume.pdf",
        mime="application/octet-stream",)
       
    st.markdown('## Summary', unsafe_allow_html=True)
    st.info('''
                - I am a 22 year old UI UX Designer who enjoy's. 
                - Devoted to staying current of the newest UI Design trends while providing concepts and examples to inspire new ones. 
                - Able to solve end-user problems through user research, ideation, wireframing, prototyping, and these techniques. 
                - High ability to manage challenging projects. Innovative, problem-solving, open to exchanging ideas and learning new things.
            ''')

    st.markdown('## Skills', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1 :
        st.info('''
                    #### Hard Skills 
                    - Figma
                    - Prototyping  
                    - Wireframing
                    - Html & CSS   
                ''')

    with col2 :
        st.info('''
                    #### Soft Skills 
                    - Team Work
                    - Empathy
                    - Goal Oriented
                    - Organized
                ''')

############################################ Education Function(Angais) ##############################################################

def Education():

    st.markdown('## ', unsafe_allow_html=True)
    st.info('''
                ### MASTER'S SCIENCE IN INFORMATION TECHNOLOGY  
                - Pillai College of Arts, Commerce & Science - Panvel, Navi Mumbai ( July, 2021 - Present )

                ### BACHELOR'S SCIENCES IN INFORMATION TECHNOLOGY
                - Mumbai University, Mumbai- India ( July, 2018 - May, 2021 )
            ''')


############################################ Experience Function(Angais) ##############################################################

def Experience():

    st.markdown('## ', unsafe_allow_html=True)
    st.info('''
                ### Reczee - Effective Matchmaking for Recruitment - Freelance    
                - My responsibility was to overhaul the entire platform and give the website a more upscale appearance.
                - I redesigned the website structure including page format, buttons and colour palettes to improve user experience.
                - Softwares Used : Figma, Adobe illustrator
                - ###### OPEN PROJECT : [link](https://www.reczee.com/)        
            ''')
  
    

############################################ Projects Function (Angais) ##############################################################

def Projects():


    st.markdown('## ', unsafe_allow_html=True)
    st.info('''
                ### Event Maker Web-App UI Design
                - The event maker web application is made for restaurants and clubs and enables users to connect in a contemporary manner thanks to its dark design and distinctive button layout. 
                - Figma's smart animation is used to create interaction between the dates of matches. This uses excellent typography and colour contrasts.
                - Implemented technology: Figma, Wireframinig, Prototyping
                - ###### OPEN PROJECT : [link](https://www.behance.net/gallery/145142613/Event-Maker)
            ''')


    st.markdown('## ', unsafe_allow_html=True)
    st.info('''
                ### SHAW Academy App UI Design
                - Shaw Academy is an already-existing programme, and in this revamp I've added some new features including more imaginative user interface ideas.
                - The app's user interface is created with all age groups in mind and offers a welcoming environment.  And there are also some convenient payment options.
                - Implemented technology: Figma, Wireframinig, Prototyping
                - ###### OPEN PROJECT : [link](https://www.behance.net/gallery/127960903/App-Clone)               
            ''')

############################################ Function call(Angais) ##############################################################

if selection == 'Profile':
    profile()

if selection == 'Education':
    Education()

if selection == 'Experience':
    Experience()

if selection == 'Projects':
    Projects()



