import streamlit as st
from PIL import Image
from random import randint
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '答题区'])

def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page1():
    st.write("这是本作者的兴趣推荐页:sunglasses:")
    st.image("DingJingyan_111.png")
    st.write("没有视频和音频是因为没有视频和音频的文件")
    #st.audio(".mp3")
    #st.video(".mp4")
def page2():
    st.write("图片换色小程序:question::question::question:")
    file_uploaded = st.file_uploader("上传图片", type=["png", "jpg", "jpeg", "jpe", "bmp", "ico", "xbm", "xpm", "pdf", "avif"])
    if file_uploaded:
        tab1, tab2, tab3 = st.tabs(["原图", "随机改色", "旋转90度"])
        file_name = file_uploaded.name
        file_type = file_uploaded.type
        file_size = file_uploaded.size
        img = Image.open(file_uploaded)
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, randint(0, 2), randint(0, 2), randint(0, 2)))
        with tab3:
            st.image(img.rotate(90))
def page3():
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    with open('check_out_times.txt', 'w', encoding='utf-8') as f:
        message = ''
        for k, v in times_dict.items():
            message += str(k) + '#' + str(v) + '\n'
        message = message[:-1]
        f.write(message)
    word = st.text_input("请输入您想查询的单词：")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write('查询次数：', times_dict[n])
        if word == "python":
            st.code('''
                    #恭喜你触发彩蛋
                    print("Hello,python")
                    ''')
        if word == "BH":
            st.balloons()
        if word == "BTD6":
            st.image("Y.png")
        if word == "monkey-BTD6":
            st.image("A.png")
            st.image("B.png")
            st.image("C.png")
            st.image("D.png")
            st.image("E.png")
            st.image("F.png")
            st.image("G.png")
            st.image("H.png")
            st.image("I.png")
            st.image("J.png")
            st.image("K.png")
            st.image("L.png")
            st.image("M.png")
            st.image("N.png")
            st.image("O.png")
            st.image("P.png")
            st.image("Q.png")
            st.image("R.png")
            st.image("S.png")
            st.image("T.png")
            st.image("U.png")
            st.image("V.png")
            st.image("W.png")
            st.image("X.png")

def page4():
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🐱'):
                st.write(i[1], ':', i[2])
        elif i[1] == '神秘人':
            with st.chat_message('👾'):
                st.write(i[1], ':', i[2])
        elif i[1] == '死神':
            with st.chat_message('💀'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫', '神秘人', '死神'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page5():
    st.write('答题区')
    #roading = st.progress(0, '开始答题')
    #for i in range(1, 101, 1):
    st.write('---')
    st.write('请问以下是软件的是：')
    col1, col2 = st.columns([1, 1])
    with col1:
        cb1 = st.checkbox('A.QQ')
        cb3 = st.checkbox('C.谷歌浏览器')
    with col2:
        cb2 = st.checkbox('B.游戏')
        cb4 = st.checkbox('D.python')
    b1 = st.button('回答')
    if b1:
        if cb1 == True and cb2 == False and cb3 == True and cb4 == True:
            st.write('恭喜你，答对了。')
        else :
            st.write('恭喜你，答错了。')
            st.write('有的以下是网站！')
            #roading.progress(i, '答题进度'+str(i)+'%')
    #roading.progress(100, '答题结束！')


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智能词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '答题区':
    page5()
