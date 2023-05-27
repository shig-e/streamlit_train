import streamlit as st
import pandas as pd
from PIL import Image

# title
st.title("This is the TITLE")
st.caption("This is the caption")

# header
st.header("This is the header")
st.subheader("This is the subheader")
st.text("text")
st.write("write")

# magic comand
"""
# h1
## h2
### h3
#### h4

'''python
import streamlit as st

#title
st.title("This is the TITLE")
st.caption("This is the caption")
'''
"""

# code
code_python = """
#Python
print('python)
"""
st.code(code_python, language="python")

code_html = """
<!-- HTML -->
<h1>HTML</h1>
"""
st.code(code_html, language="html")

code_css = """
/* CSS */
h1 {
    color: red;
}
"""
st.code(code_css, language="css")

code_java = """
//Java
System.out.println('java')
"""
st.code(code_java, language="java")

code_php = """
//PHP
echo 'PHP';
"""
st.code(code_php, language="php")

code_ruby = """
#Ruby
puts 'Ruby'
"""
st.code(code_ruby, language="ruby")

code_sh = """
$ streamlit hello
"""
st.code(code_sh, language="sh")

# markdown
st.markdown("This is **_italic_**.")
st.markdown(":green[緑色]です")
st.markdown("これは **:red[赤色で太字]** です")

"This is **_italic_**."
":green[緑色]です"
"これは **:red[赤色で太字]** です"

#DataFrame
df = pd.DataFrame([3,2,4,2],
                  ['りんご','みかん','いちご','もも'],
                  ['売上'],)
df

# textbox
textbox = st.text_input('この下はtextboxです')
textbox

# button
submit_btn = st.button('送信')
cancel_btn = st.button('キャンセル')
if submit_btn:
    st.text('送信ボタンが押されました')
    
# input widgets with control flow
with st.form(key='sales_form'):
    # textbox
    item = st.text_input('売れた商品名を記入してください')
    number = st.text_input('売れた数量を記入してください')
    # button
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{item}が{number}個、売れました。')
        
# selectbox widgets with control flow
with st.form(key='select_form'):
    # selectbox
    item_select = st.selectbox(
        '売れた商品名を選んでください',
        ('-', 'いちご', 'もも', 'バナナ', 'りんご')
    )
    number_select = st.selectbox(
        '売れた数量を選んでください',
        ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    
    # button
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{item_select}が{number_select}つ、売れました。')
        
# radio button and selectbox widgets with control flow
with st.form(key='radio_from'):
    # raido
    item_select = st.radio(
        '売れた商品名を選んでください',
        ('-', 'いちご', 'もも', 'ばなな', 'りんご')
    )
    number_select = st.selectbox(
        '売れた数量を選んでください',
        ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    )
    # button
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{item_select}が{number_select}つ、売れました。')
        
# multiselectbox widgets with control flow
with st.form(key='multiselect_form'):
    sold_out = st.multiselect(
        '本日の売り切れ商品',
        ('-', 'いちご', 'もも', 'ばなな', 'りんご')
    )
    # radio
    item_selent = st.radio(
        '売れた商品名を選んでください',
        ('-', 'いちご', 'もも', 'ばなな', 'りんご')
    )
    number_select = st.selectbox(
        '売れた数量を選んでください',
        ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    )
    # button
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{item_select}が{number_select}つ、売れました。')
        st.text(f"{','.join(sold_out)}は売り切れています。")
        
# expander
st.write('よくあるお問い合わせ')
expander1 = st.expander('営業時間は何時から何時までですか?')
expander1.write('営業時間は10:00から18:00までです。')
expander2 = st.expander('定休日はいつですか？')
expander2.write('日曜日と祝日がお休みです')

# read_excel
st.markdown(' ### 月別売上')
sales_data = pd.read_excel('./data/sales_data.xlsx', engine='openpyxl')
sales_data

# line_chart
st.markdown(' ### 月売上推移')
st.line_chart(sales_data, x='営業月')

# bar_chart
st.bar_chart(sales_data, x='営業月')

# checkbox with multiselect
if st.checkbox('マルチセレクトを使ってグラフを比較する'):
    # エクセルデータの読み込み
    sales_data = pd.read_excel('./data/sales_data.xlsx', engine='openpyxl')
    # mutliselect
    selected_fruits = st.multiselect(
        '果物を選んでください',
        ['いちご', 'もも', 'バナナ', 'りんご'],
        ['いちご', 'もも', 'バナナ', 'りんご']
    )
    if not selected_fruits:
        st.error('表示する果物が選択だれていません。')
    else:
        st.line_chart(sales_data[selected_fruits])
        
# 2columns
if st.checkbox('カラムを2つ並べてデータを表示する'):
    col_1, col_2 = st.columns(2)
    with col_1:
        select_fruits = st.selectbox('果物を選んでください',
                                     ['いちご', 'もも', 'バナナ', 'りんご'],
                                     key=2)
        with col_2:
            st.write(sales_data[select_fruits])
            
# 3columns
if st.checkbox('カラムを3つ並べてデータを表示する'):
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        select_fruits = st.selectbox('果物を選んでください',
                                     ['いちご', 'もも', 'バナナ', 'りんご'],
                                     key=3)
    with col_2:
            st.write(sales_data[select_fruits])
    with col_3:
            st.bar_chart(sales_data[select_fruits])
            
# Image
if st.checkbox('画像を表示する'):
    image = Image.open('./img/wave.png')
    st.image(image)
    st.image(image, width=500)