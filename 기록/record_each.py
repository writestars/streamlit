import streamlit as st
import sqlite3

con = sqlite3.connect('records.db')
cur = con.cursor()

menu = st.sidebar.selectbox('메뉴',
                            options=['기록 작성 ','기록 보기'])


    with st.form
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        foodname = st.text_input('음식 종류를 적어보세요')
        calories = st.in_input('비밀번호 확인', type='password')
        time = st.radio('먹은 시간', options=['아침','점심', '저녁','야식'],
                       horizontal=True)
        day = st.date_input('먹은 날짜')
        imagefile = st.image_input('사진을 추가하세요.')

#
        submitted = st.form_submit_button('식단 추가하기')
        if submitted:
            st.success(f'{foodname} {calories} {time} {day} {imagefile} {imageopen}');
            cur.execute(f"INSERT INTO users VALUES("
                        f" '{foodname}','{calories}','{time}','{day}',"
                         f"'{imagefile}','{imageopen}',CURRENT_DATE)")
            con.commit()




