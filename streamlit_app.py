import requests
import streamlit as st
from streamlit_lottie import st_lottie
from annotated_text import annotated_text
from streamlit_option_menu import option_menu
import sqlite3
import datetime
import pandas as pd
from PIL import Image
import streamlit_survey as ss



conn = sqlite3.connect('data.db')
c = conn.cursor()
user = ""
count = 0
user = ""
user_type = ""
servicetype = ""

if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'
st.set_page_config(page_title="RK mainpage", page_icon=":satellite:", layout="wide", initial_sidebar_state=st.session_state.sidebar_state)

def feedback(feedback_type, worker_name = ''):
    if feedback_type is not "select":
        q = survey.radio("Likert scale:", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)
        out =""
        if q != "NA":
            if q == "😞":
                out = 1
            if q == "🙁":
                out = 2
            if q == "😐":
                out = 3
            if q == "🙂":
                out = 4
            if q == "😀":
                out = 5

        rating = out
        comments = survey.text_area("Area input:")
        feedback_button = st.button("Submit")
        if rating and feedback_button:
            feedback_table()
            feedback_table1()
            if worker_name == '':
                add_feedback(feedback_type, rating, comments)
                st.success("Thankyou for the feedback")
            else:
                add_feedback1(feedback_type, worker_name, rating, comments)
                st.success("Thankyou for the feedback")

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT,user_type TEXT)')
def add_userdata(username, password, user_type):
    c.execute('INSERT INTO userstable(username,password,user_type) VALUES (?,?,?)', (username, password, user_type))
    conn.commit()


def login_user(username, password, user_type):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ? AND user_type = ?', (username, password, user_type))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data




def create_table4():
    c.execute('CREATE TABLE IF NOT EXISTS userstable41(servicetype TEXT,username TEXT,worker_name TEXT,date TEXT, mobile TEXT,location TEXT, other_comments TEXT)')


def add_userdata4(servicetype, username, worker_name, date, mobile, location, other_comments):
    c.execute('INSERT INTO userstable41(servicetype,username,worker_name,date,mobile,location,other_comments) VALUES (?,?,?,?,?,?,?)', (servicetype, username, worker_name, date, mobile, location, other_comments))
    conn.commit()


def login_user4(servicetype, username, worker_name, date, mobile, location, other_comments):
    c.execute('SELECT * FROM userstable41 WHERE servicetype =? AND username =? AND worker = ? AND date = ? AND location = ? AND mobile = ? AND other_comments = ?', (servicetype, username, worker_name, date, mobile, location, other_comments))
    data = c.fetchall()
    return data

def view_all_users4():
    c.execute('SELECT * FROM userstable41')
    data = c.fetchall()
    return data
def create_table5():
    c.execute('CREATE TABLE IF NOT EXISTS userstable5(appply_service_type TEXT, name TEXT,mobile TEXT, adhar TEXT, apply_date TEXT, age TEXT, experience TEXT, adress TEXT)')


def add_userdata5(appply_service_type, name, mobile, adhar, apply_date, age, experience, adress):
    c.execute('INSERT INTO userstable5(appply_service_type, name, mobile, adhar, apply_date, age, experience, adress) VALUES (?,?,?,?,?,?,?,?)', (appply_service_type, name, mobile, adhar, apply_date, age, experience, adress))
    conn.commit()


def login_user5(appply_service_type, name, mobile, adhar, apply_date, age, experience, adress):
    c.execute('SELECT * FROM userstable5 WHERE appply_service_type =? AND name =? AND mobile =? AND adhar = ? AND apply_date = ? AND age = ? AND experience = ? AND adress = ?', (appply_service_type, name, mobile, adhar, apply_date, age, experience, adress))
    data = c.fetchall()
    return data

def view_all_users5():
    c.execute('SELECT * FROM userstable5')
    data = c.fetchall()
    return data


def create_table3():
    c.execute('CREATE TABLE IF NOT EXISTS userstable3(username TEXT,password TEXT,user_type TEXT)')


def add_userdata3(username, password, user_type):
    c.execute('INSERT INTO userstable3(username,password,user_type) VALUES (?,?,?)', (username, password, user_type))
    conn.commit()


def login_user3(username, password, user_type):
    c.execute('SELECT * FROM userstable3 WHERE username =? AND password = ? AND user_type = ?', (username, password, user_type))
    data = c.fetchall()
    return data

def feedback_table():
    c.execute('CREATE TABLE IF NOT EXISTS feedback_table(user_type TEXT, rating TEXT, comments TEXT)')


def add_feedback(user_type,rating,comments):
    c.execute('INSERT INTO feedback_table(user_type,rating,comments) VALUES (?,?,?)', (user_type,rating,comments))
    conn.commit()


def login_feedback(user_type,rating,comments):
    c.execute('SELECT * FROM feedback_table WHERE user_type =? AND rating = ? AND comments = ?', (user_type,rating,comments))
    data = c.fetchall()
    return data
def view_all_feebacks():
    c.execute('SELECT * FROM feedback_table')
    data = c.fetchall()
    return data

def feedback_table1():
    c.execute('CREATE TABLE IF NOT EXISTS feedback_table1(user_type TEXT, name TEXT, rating TEXT, comments TEXT)')


def add_feedback1(user_type,name,rating,comments):
    c.execute('INSERT INTO feedback_table1(user_type,name,rating,comments) VALUES (?,?,?,?)', (user_type,name,rating,comments))
    conn.commit()


def login_feedback1(user_type,name,rating,comments):
    c.execute('SELECT * FROM feedback_table1 WHERE user_type =? AND name = ? AND rating = ? AND comments = ?', (user_type,name,rating,comments))
    data = c.fetchall()
    return data
def view_all_feebacks1():
    c.execute('SELECT * FROM feedback_table1')
    data = c.fetchall()
    return data

def login():
    with st.container():
        left_column1, right_column2, left_column3, right_column4 = st.columns(4)
        with right_column4:
            choice = st.selectbox('login/signup', ['select', 'login', 'signup', 'logout'])
            if choice == "login":
                st.sidebar.subheader(choice)
                with st.sidebar:
                    st.sidebar.subheader("login section")
                    usertype = st.sidebar.selectbox('usertype', ['select', 'admin', 'worker', 'user', "contractor"])
                    username = st.sidebar.text_input("user name")
                    password = st.sidebar.text_input("password", type='password')

                    if st.sidebar.checkbox("login"):
                        create_table()
                        result = login_user(username, password, usertype)
                        if result:
                            st.sidebar.success("logged in as {}".format(username))
                            st.session_state.sidebar_state = 'collapsed'
                            global user
                            user = username
                            global user_type
                            user_type = usertype
                        else:
                            st.sidebar.warning("incorrect username/password")
            if choice == 'signup':
                with st.sidebar:
                    st.sidebar.subheader("create an account")
                    user_type = st.sidebar.selectbox('usertype', ['select', 'admin',  'worker', 'user', "contractor"])
                    if user_type != "select":
                        new_user = st.sidebar.text_input("new_user name")
                        new_user_mail = st.sidebar.text_input("new_user email")
                        new_password = st.sidebar.text_input("new_password", type="password")
                        if user_type == 'admin':
                            new_code = st.sidebar.text_input("Code", type="password")
                        if st.sidebar.checkbox("signup"):
                            if not new_user and not new_user_mail and not new_password:
                                st.sidebar.warning("please enter the details")
                            else:
                                if user_type == 'admin':
                                    if new_code != str(9652):
                                        st.sidebar.warning("incorrect code")
                                    else:
                                        create_table()
                                        result = login_user(new_user, new_password, user_type)
                                        if result:
                                            st.sidebar.info(
                                                "account already exists. please got to login menu to login ")
                                        else:
                                            add_userdata(new_user, new_password, user_type)
                                            st.sidebar.success("you have successfully created an valid account")
                                            st.sidebar.info("go to login menu to login")
                                else:
                                    create_table()
                                    result = login_user(new_user, new_password, user_type)
                                    if result:
                                        st.sidebar.info("account already exists. please got to login menu to login ")
                                    else:
                                        add_userdata(new_user, new_password, user_type)
                                        st.sidebar.success("you have successfully created an valid account")
                                        st.sidebar.info("go to login menu to login")
        with left_column3:
            with st.container():

                left_column1, right_column2 = st.columns(2)
                with right_column2:
                    annotated_text(
                        ("Contact us"),
                    )
                    if st.button("contact us"):
                        with st.sidebar:
                            st.sidebar.subheader("Contact through form")
                            contact_us = """
                            <form action="https://formsubmit.co/rakeshreddykare1234@gmial.com" method="POST">
                                <input type="hidden" name="_captcha" value ="false">
                                <input type="text" name="name" placeholder = "your name" required>
                                <input type="email" name="email" placeholder = "your email" required>
                                <textarea name="message" placeholder = "you message here" required></textarea>
                                <button type="submit">Send</button>
                                </form>
                                """
                            st.markdown(contact_us, unsafe_allow_html=True)

                            def local_css(file_name):
                                with open(file_name) as f:
                                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

                            local_css("style/style.css")
login()
final_results3 = []
final_results4 = []
def feed_back_details(user_type,feedback_type, worker_name =""):
    if user_type == "admin" and feedback_type != "select":
        feedback_detail = st.checkbox('click to see feedback details', key='42')
        if feedback_detail:
            if worker_name == '':
                for service in view_all_feebacks():
                    if feedback_type == service[0]:
                        final_results3.append(service)
                clean_db = pd.DataFrame(tuple(final_results3),
                                        columns=["service_type", "ratings", "comments", ])
                st.dataframe(clean_db)
            else:
                for service in view_all_feebacks1():
                    if feedback_type == service[0]:
                        final_results3.append(service)
                clean_db = pd.DataFrame(tuple(final_results3),
                                        columns=["service_type", "worker_name", "ratings", "comments", ])
                st.dataframe(clean_db)
def feedback_rating(servicetype, worker_name = ''):
    rating = []
    if worker_name == '':
        for i in view_all_feebacks():
            if i[0] == servicetype:
                rating.append(int(i[1]))

    else:
        for i in view_all_feebacks1():
            if i[1] == worker_name and servicetype == i[0]:
                rating.append(int(i[2]))
                st.write(worker_name)
    if rating:
        final_rating = sum(rating) / len(rating)
        rating2 = ""
        if final_rating:
            for i2 in range(int(final_rating)):
                rating2 = rating2 + "⭐"
        st.success("Rating: " + rating2)
def application_details(apply_type):
    if user_type == "worker" or "user":
        if user_type != "admin":
            for user_tupple in view_all_users5():

                booked_user = list(user_tupple)[0]
                if booked_user == booking_user:
                    final_results3.append(list(user_tupple))
            st.write( final_results3)
            for service in final_results3:

                if apply_type == service[0]:
                    final_results4.append(service)
            clean_db2 = pd.DataFrame(tuple(final_results4),

                                     columns=["name", "mobile", "adhaar number", "apply_date", "age", "experience", "address", "apply_service_type"])
            st.dataframe(clean_db2)
    if user_type == "admin":
        for service in  view_all_users5():
            if apply_type == service[7]:
                final_results3.append(service)
        clean_db = pd.DataFrame(tuple(final_results3),
                                columns=["name", "mobile", "adhaar", "apply_date", "age", "experience", "adress","apply_service_type"])
        st.dataframe(clean_db)

def application(apply_serice_type):
    name = st.text_input("full name")
    mobile = st.text_input("mobile number")
    adhar = st.text_input("enter adhaar no")
    apply_date = st.date_input(
        "select date",
        datetime.date(2023, 6, 12))
    age = st.text_input("enter age")
    experience = st.text_input("experience")
    adress = st.text_input("address here")
    Booking = st.button('click to apply')
    if Booking:
        if experience=="" and age == "" and name == "":
            st.warning("please enter the details")
        else:
            if int(age) > 56 and int(experience) < 1:
                st.info("your not eligible to apply. please check requirements and entered details!!")
            else:
                create_table5()
                result = login_user5(name, mobile, adhar, apply_date, age, experience, adress, apply_serice_type)
                if result:
                    st.info("already applied for this serivce")
                else:
                    add_userdata5(name, mobile, adhar, apply_date, age, experience, adress, apply_serice_type)
                    st.success('You applied successfully')

def booking_details(service_type):
    servicetype = service_type
    if user_type == "worker" or "user":
        if user_type != "admin" and user_type != "contractor":
            for user_tupple in view_all_users4():
                booked_user = list(user_tupple)[1]
                if booked_user == booking_user:
                    final_results.append(list(user_tupple))

            for service in final_results:
                if servicetype == service[0]:
                    final_results2.append(service)
            clean_db2 = pd.DataFrame(tuple(final_results2),
                                     columns=["service_type", "Booking_customer", "Booked_Contractor", "date", "contact_number", "location", "other comments"])
            st.dataframe(clean_db2)
    if user_type == "admin" or  "contractor":
        for service in view_all_users4():
            if servicetype == service[0]:
                final_results2.append(service)
                for data in final_results2:
                    if data[6].isnumeric():
                        contractor_results.append(data)
                    else:
                        workers_results.append(data)
                        st.header(data[6])
        clean_db = pd.DataFrame(tuple(workers_results),
                                columns=["service_type", "Booking_customer", "Booked_worker", "date",
                                         "contact_number", "location", "other comments"])
        st.dataframe(clean_db)
        st.header("Contractor booking details")
        clean_db2 = pd.DataFrame(tuple(contractor_results),
                                 columns=["service_type", "Booking_customer", "Booked_Contractor", "date",
                                          "contact_number", "location", "number of workers"])
        st.dataframe(clean_db2)

def booking(service_type, worker, contractor = ""):
    booking_date = st.date_input(
        "select date",
        datetime.date(2023, 6, 12))
    mobile = st.text_input("mobile number here")
    location = st.text_input("location here")
    if contractor == "":
        comments = st.text_input("other comments")
    else:
        comments = st.text_input("enter many workers need")

    Booking = st.button('click to Book')
    if Booking:
        create_table4()
        create_table3()
        result = login_user3(worker, booking_date, location)
        if result:
            st.info("already booked on this date. please book any other date ")

        else:
            if not location and not comments:
                st.info("please enter details correctly")
            else:
                add_userdata3(worker, booking_date, location)
                add_userdata4(service_type,booking_user, worker, booking_date, mobile, location,comments)
                st.write('You booked on :', booking_date)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container():
    st.subheader("Hello:wave: welcome to all in one family")

    st.write(
        "Labor is the source of all wealth")
def load_lottieurl (url):
    r = requests.get(url, verify=False)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qcrbuch7.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("OUR VISION")

        st.write(
            """
            Our vision is to create a comprehensive and user-friendly website that will bridge the gap between daily wage laborers and employers, by providing a centralized hub for efficient, fair, and transparent labor management by creating job opportunities for the daily wage laborer's.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


book = None
if user:
    selected = option_menu(
        menu_title=None,
        options=["HOME", "SERVICES", "CARRIER", "FEEDBACK"],
        default_index=0,
        orientation="horizontal",
    )
    if selected == "HOME":

        st.title(f"You have selected {selected}")
        st.write(
            """
            Welcome to our website dedicated to daily wage laborers! Here, our aim is to provide a comprehensive platform that caters to the needs of both employers and workers in the realm of daily wage labores. \n
            """
        )
        with st.container():
            column_1, column_2, column_3, = st.columns(3)
            with column_1:
                st.header("Services Offered")
                servicetype = "Construction"
                st.write(
                    """
                    Our website typically acts as a platform that connects workers who are looking for short-term or temporary employment with employers or individuals who need labor for specific tasks. \n
                    Below are the list of services provided by this website\n
                    1)Construction workers \n
                    2)Electricians \n
                    3)Agriculture and farm workers \n
                    4)General Workers
                    """
                )
            with column_2:
                st.header("Carrier")
                st.write(
                    """
                    The carrier details section typically provides information about the skills, experience, and availability of workers seeking employment. \n
                    This section allows workers to showcase their qualifications and highlight the type of work they are skilled in, making it easier for employers to find suitable candidates for their job requirements.
                    """
                )

            with column_3:
                st.header("Feedback")
                st.write(
                    """
                    The feedback details section in a daily wage labor website provides a platform for both employers and workers to share their experiences and provide feedback on their interactions and work performance.
                    \nIt serves as a valuable tool for building trust, credibility, and transparency within the community
                    """
                )

    elif selected == "SERVICES":
        st.title(f"You have selected {selected}")
        with st.container():
            st.write("---")
            left_column_1, left_column_2, right_column_1, right_column_2 = st.columns(4)
            with left_column_1:
                st.header("Construction")
                servicetype = "Construction"
                st.write(
                    """
                    The construction industry is a great contribution to the economic and social development of a country, particularly due to the number of direct and indirect jobs generated.
                    """
                )

                with st.container():
                    left_column_8, right_column_9 = st.columns(2)
                    with left_column_8:
                        lottie_construction = load_lottieurl(
                            "https://assets6.lottiefiles.com/packages/lf20_1lvsledo.json")
                        st_lottie(lottie_construction, height=300, key='construction')
                        Booking = st.checkbox('Book_constructors', key='construction1')
                        if Booking:
                            book = "Construction"
                        feedback_rating(servicetype)

            with left_column_2:
                st.header("Electricity")
                servicetype = "Electricity"
                st.write(
                    """
                    An electrician is a tradeperson specializing in installing electrical wiring in buildings and poles, troubleshooting malfunctions and blackouts and repairing appliances.
                    """
                )
                with st.container():
                    left_column_10, right_column_11 = st.columns(2)
                    with left_column_10:
                        lottie_construction = load_lottieurl(
                            "https://assets9.lottiefiles.com/packages/lf20_JYTmNnDLrS.json")
                        st_lottie(lottie_construction, height=300, key='electricity')
                Booking = st.checkbox('Book_electricity', key="Electricity1")
                if Booking:
                    book = "Electricity"
                feedback_rating(servicetype)
            with right_column_1:
                st.header("Agriculture")
                servicetype = "Agriculture"
                st.write(
                    """
                     Agricultural labourers are landless labourers who work on other's land to earn a livelihood and they perform activities like cultivation and production of crops and agricultural establishments.
                    """
                )
                with st.container():
                    left_column_12, right_column_13 = st.columns(2)
                    with left_column_12:
                        lottie_construction = load_lottieurl(
                            "https://assets2.lottiefiles.com/datafiles/eZXzHZZ2e9Apt25/data.json")
                        st_lottie(lottie_construction, height=300, key='farming')
                Booking = st.checkbox('Book_farming_labors', key='farming1')
                if Booking:
                    book = "Agriculture"
                feedback_rating(servicetype)

            with right_column_2:
                st.header("General Workers")
                servicetype = "General Workers"
                st.write(
                    """
                    General laborers are supporting the daily tasks which includes workers like painters, plumbers, housekeepers, security guardss, mechanics etc... 
                    """
                )
                left_column_14, right_column_15 = st.columns(2)
                with left_column_14:
                    lottie_construction = load_lottieurl(
                        "https://assets3.lottiefiles.com/packages/lf20_twxv8mn4.json")
                    st_lottie(lottie_construction, height=300, key='workers')
                    Booking = st.checkbox('Book_Generalworkers', key='workers1')
                    if Booking:
                        book = "General Workers"

                    feedback_rating(servicetype)

    elif selected == "CARRIER":
        st.title(f"You have selected {selected}")
        with st.container():
            st.write("---")
            left_column_1, left_column_2, right_column_1, right_column_2 = st.columns(4)
            with left_column_1:
                st.header("Construction")
                apply_serice_type = "Construction"
                st.write(
                    """
                    agdagdaggg \n
                    ***************Content here************* \n
                    adgaGgg
                    """
                )
                apply = st.checkbox('click to apply', key='apply1')
                if apply:
                    application(apply_serice_type)
                apply_detail = st.checkbox('click to see application details', key='apply2')
                if apply_detail:
                    application_details(apply_serice_type)
            with left_column_2:
                st.header("Electricity")
                apply_serice_type = "Electricity"
                st.write(
                    """
                    agdagdaggg \n
                    ***************Content here************* \n
                    adgaGgg
                    """
                )
                apply = st.checkbox('click to apply', key='apply3')
                if apply:
                    application(apply_serice_type)
                apply_detail = st.checkbox('click to see application details', key='apply4')
                if apply_detail:
                    application_details(apply_serice_type)

            with right_column_1:
                st.header("Agriculture")
                apply_serice_type = "Agriculture"
                st.write(
                    """
                    agdagdaggg \n
                    ***************Content here************* \n
                    adgaGgg
                    """
                )
                apply = st.checkbox('click to apply', key='apply5')
                if apply:
                    application(apply_serice_type)
                apply_detail = st.checkbox('click to see application details', key='apply6')
                if apply_detail:
                    application_details(apply_serice_type)

            with right_column_2:
                st.header("General Workers")
                apply_serice_type = "General Workers"
                st.write(
                    """
                    agdagdaggg \n
                    ***************Content here************* \n
                    adgaGgg
                    """
                )
                apply = st.checkbox('click to apply', key='apply7')
                if apply:
                    application(apply_serice_type)
                apply_detail = st.checkbox('click to see application details', key='apply8')
                if apply_detail:
                    application_details(apply_serice_type)

    else:
        st.title(f"You have selected {selected}")
        lottie_construction = load_lottieurl(
            "https://assets8.lottiefiles.com/packages/lf20_ytuahfq7.json")
        st_lottie(lottie_construction, height=300, key='General Workers')
        survey = ss.StreamlitSurvey("Survey Example")
        with st.container():

            left_column_1, left_column_2, right_column_1, right_column_2 = st.columns(4)
            with left_column_1:
                st.header("services")
                feedback_type = st.selectbox('service_type', ['select', 'Construction', 'Electricity', 'Agriculture', 'General Workers'], key="feedback1")
                feedback(feedback_type)
                feed_back_details(user_type, feedback_type)
            with left_column_2:
                st.header("contractor")
                feedback_type = st.selectbox('service_type',
                                             ['select', 'Construction', 'Electricity', 'Agriculture', 'General Workers'],
                                             key="back1")
                if feedback_type != "select":
                    names = ['select']
                    data = view_all_users4()
                    for i in data:
                        if i[0] == feedback_type:
                            if i[2] not in names and i[6].isnumeric():
                                names.append(i[2])
                    workers_name = st.selectbox('select contractor name', names, key="feebac3")
                    if workers_name != "select":
                        feedback(feedback_type, workers_name)
                        feed_back_details(user_type, feedback_type, workers_name)
            with right_column_1:
                st.header("workers")
                feedback_type = st.selectbox('service_type',
                                             ['select', 'Construction', 'Electricity', 'Agriculture', 'General Workers'],
                                             key="feedback2")
                if feedback_type != "select":
                    names = ['select']
                    data = view_all_users4()
                    for i in data:
                        if i[0] == feedback_type:
                            if i[2] not in names and not i[6].isnumeric():
                                names.append(i[2])
                    workers_name = st.selectbox('select worker name',names,key="feedbac3")
                    if workers_name != "select":
                        feedback(feedback_type,workers_name)
                        feed_back_details(user_type, feedback_type, workers_name)
            with right_column_2:
                st.header("Website")
                others_feedback = "Website"
                feedback_type = st.selectbox('Website',
                                             ['select', 'What did you love about your experience?', 'Tell us what’s missing?', 'What are your main concerns or questions about [carrier or service]?', 'How can we make this page better?', "others comments"],
                                             key="feedck2")
                if feedback_type != "select":
                    comments = survey.text_area("Area input:", key="fj")
                    feedback_button = st.button("Submit", key="yu87")
                    feed_back_details(user_type, others_feedback)
                    if feedback_button:
                        st.success("thank you for the feedback")
                        add_feedback(others_feedback, feedback_type, comments)



final_results  = []
final_results2 = []
contractor_results = []
workers_results = []
booking_user = user

if book:
    selected = option_menu(
        menu_title=None,
        options=["Booking Area", "Booking details"],
        default_index=0,
        orientation="horizontal",
    )
    if selected == "Booking Area":
        if book == 'Construction':
            servicetype = book
            with st.container():
                st.write("---")
                left_columnc1, right_columnc2 = st.columns(2)
                with left_columnc1:
                    image = Image.open('con2.png')
                    contractor_Id = "Arjun"
                    st.image(image, caption='Arjun')
                    st.write(
                        """
                        \n
                        ***************contractor details************* \n
                        Experience: 10 years in construction field \n
                        Age: 45 years \n
                        Mobile Number: 9657825677
                        """
                    )

                    Booking = st.checkbox('click to Book', key='tion1')
                    feedback_rating(servicetype, contractor_Id)
                    if Booking:
                        booking(servicetype,contractor_Id , contractor="Arjun")
                with right_columnc2:
                    with st.container():
                        left_columnw1, right_columnw2 = st.columns(2)
                        with left_columnw1:
                            image = Image.open('co2.jpg.png')
                            worker = "Rickwith"

                            st.image(image, caption='Rickwith')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Conction1')
                            if Booking:
                                booking(servicetype, worker)
                        with right_columnw2:
                            image = Image.open('co3.jpg.png')
                            worker = "pavan"
                            st.image(image, caption='pavan')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='truction2')
                            if Booking:
                                booking(servicetype, worker)
                    with st.container():
                        left_columnw3, right_columnw4 = st.columns(2)
                        with left_columnw3:
                            image = Image.open('co4.jpg.png')
                            worker = "sreekanth"
                            st.image(image, caption='sreekanth')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Construction3')
                            if Booking:
                                booking(servicetype, worker)
                        with right_columnw4:
                            image = Image.open('c6.jpg')
                            worker = "ramesh"
                            st.image(image, caption='ramesh')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Construction4')
                            if Booking:
                                booking(servicetype, worker)
        if book == 'Electricity':
            servicetype = book
            with st.container():
                st.write("---")
                left_columnc1, right_columnc2 = st.columns(2)
                with left_columnc1:
                    image = Image.open('con1.jpg')

                    st.image(image, caption='Abhi')
                    contractor_Id = "Abhi"
                    st.write(
                        """
                        \n
                        ***************contractor details************* \n
                        Experience: 10 years in Electric field \n
                        Age: 40 years \n
                        Mobile Number: 9678994456
                        """
                    )
                    Booking = st.checkbox('click to Book', key='ction1')
                    feedback_rating(servicetype, contractor_Id)
                    if Booking:
                        booking(servicetype,contractor_Id , contractor="arjun")
                with right_columnc2:
                    with st.container():
                        left_columnw1, right_columnw2 = st.columns(2)
                        with left_columnw1:
                            image = Image.open('e1.jpg')
                            worker = "suresh"
                            st.image(image, caption='suresh')
                            feedback_rating(servicetype, worker)
                            # st.write(worker)
                            Booking = st.checkbox('click to Book', key='tricity1')
                            if Booking:
                                booking(servicetype, worker)
                        with right_columnw2:
                            image = Image.open('e2.jpg')
                            worker = "pavan"
                            st.image(image, caption='pavan')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='ectricity2')
                            if Booking:
                                booking(servicetype, worker)
                    with st.container():
                        left_columnw3, right_columnw4 = st.columns(2)
                        with left_columnw3:
                            image = Image.open('e3.jpg')
                            worker = "radha"
                            st.image(image, caption='radha')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Electric3')
                            if Booking:
                                booking(servicetype, worker)
                        with right_columnw4:
                            image = Image.open('e4.jpg')
                            worker = "Akshay"
                            st.image(image, caption='Akshay')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Electty4')
                            if Booking:
                                booking(servicetype, worker)
        if book == 'Agriculture':
            servicetype = book
            with st.container():
                st.write("---")
                left_columnc1, right_columnc2 = st.columns(2)
                with left_columnc1:
                    image = Image.open('con3.jpg')

                    st.image(image, caption='shoba')
                    contractor_Id = "shoba"
                    st.write(
                        """
                        \n
                        ***************contractor details************* \n
                        Experience: 8 years in Agricultural field \n
                        Age: 35 years \n
                        Mobile Number: 9672345676
                        """
                    )
                    feedback_rating(servicetype, contractor_Id)
                    Booking = st.checkbox('click to Book', key='ctition1')
                    if Booking:
                        booking(servicetype,contractor_Id , contractor="sneha")
                with right_columnc2:
                    with st.container():
                        left_columnw1, right_columnw2 = st.columns(2)
                        with left_columnw1:
                            image = Image.open('f1.jpg')
                            worker = "rakesh"
                            st.image(image, caption='rakesh')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Wter1')
                            if Booking:
                                booking(servicetype,worker)
                        with right_columnw2:
                            image = Image.open('f3.jpg')
                            worker = "naveena"
                            st.image(image, caption='naveena')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='War2')
                            if Booking:
                                booking(servicetype,worker)
                    with st.container():
                        left_columnw3, right_columnw4 = st.columns(2)
                        with left_columnw3:
                            image = Image.open('f4.jpg')
                            worker = "vineetha"
                            st.image(image, caption='vineetha')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='Wate')
                            if Booking:
                                booking(servicetype,worker)
                        with right_columnw4:
                            image = Image.open('f2.jpg')
                            worker = "shoba"
                            st.image(image, caption='shoba')
                            feedback_rating(servicetype, worker)

                            Booking = st.checkbox('click to Book', key='ter')
                            if Booking:
                                booking(servicetype,worker)
        if book == 'General Workers':
            servicetype = book
            with st.container():
                st.write("---")
                left_columnc1, right_columnc2 = st.columns(2)
                with left_columnc1:
                    image = Image.open('c1.jpg.png')

                    st.image(image, caption='contractor')
                    contractor_Id = "Amruta"
                    st.write(
                        """
                        agdagdaggg \n
                        ***************contractor details************* \n
                        adgaGgg
                        """
                    )
                    feedback_rating(servicetype, contractor_Id)
                    Booking = st.checkbox('click to Book', key='fgjtion1')
                    if Booking:
                        booking(servicetype,contractor_Id , contractor="Amruta")
                with right_columnc2:
                    with st.container():
                        left_columnw1, right_columnw2 = st.columns(2)
                        with left_columnw1:
                            image = Image.open('plumber1.jpg')
                            worker = "john"
                            st.image(image, caption='john')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='General Workers1')
                            if Booking:
                                booking(servicetype,worker)
                        with right_columnw2:
                            image = Image.open('painter1.jpg')
                            worker = "amaljith"
                            st.image(image, caption='amaljith')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='General Workers2')
                            if Booking:
                                booking(servicetype,worker)
                    with st.container():
                        left_columnw3, right_columnw4 = st.columns(2)
                        with left_columnw3:
                            image = Image.open('m1.jpg')
                            worker = "barath"
                            st.image(image, caption='barath')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='General Workers3')
                            if Booking:
                                booking(servicetype,worker)
                        with right_columnw4:
                            image = Image.open('maid1.jpg')
                            worker = "totirani"
                            st.image(image, caption='totirani')
                            feedback_rating(servicetype, worker)
                            Booking = st.checkbox('click to Book', key='General Workers4')
                            if Booking:
                                booking(servicetype, worker)

    if selected == "Booking details":

        with st.container():
            left_column_1, left_column_2, right_column_1, right_column_2 = st.columns(4)
            with left_column_1:
                st.header("Construction")
                if book == 'Construction':
                    servicetype = 'Construction'
                    booking_details(servicetype)
            with left_column_2:
                st.header("Electricity")
                if book == 'Electricity':
                    servicetype = 'Electricity'
                    booking_details(servicetype)
            with right_column_1:
                st.header("Agriculture")
                if book == 'Agriculture':
                    servicetype = 'Agriculture'
                    booking_details(servicetype)
            with right_column_2:
                st.header("General Workers")
                if book == 'General Workers':
                    servicetype = 'General Workers'
                    booking_details(servicetype)
