#stream lit 
import streamlit as st

st.set_page_config(page_title="Growth MindSet Projest",project_icon=" ✯ ")


st.title(" Growth MindSet AI Projest")
st.head(" WELCOME TO  YOUR GROWTH JOURNEY!")
st.write("Embarace Challenge , learn from mistake , and unlock your full potential . this AI-powered app helps you to build a growth mindset with reflection , challenges, and achievements!")



#quest section
st.header("  Today Growth Minset Quotes")
st.write("Success Is Not a Final , Failure is not a Fetsl : it is the courage to continue that counts .")

st.header(" Whats Your Challenge Today ?")
user_input = st.text_input("Describe The Challenge you are facing  :")




#conditions....


if user_input:
    st.success(f"you are facing :{user_input}. keep pushing forrwad towords yours goals!")
else:
        st.warning("tell us about your challenge to get started!")

#reflexing 
st.header("reflect on your learninig")
reflection= st.text_area("wwrite your reflection here ........")

if reflection:
    st.success(f"GREATE INSIDE ! your reflection : {reflection}")
else:
    st.info("Reflection on past experience help to grow! share your difficulties...")


 #achievemnt

st.header("celebrate yours wins")
achievements=st.text_input("share something you are recently accomplished:")

if achievements:
    st.success(f"CONGRATULATIONS ! you have achieved:{achievements}")
else:
      st.info("Big or small , every acheivement counts! share one now !") 

      #footer...


st.write("- - - ") 
st.write ("keep believing your self, Growth is a journey , not a destination !")
st.write(" Created By Inshal")



