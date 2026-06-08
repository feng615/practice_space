import streamlit as st

# 页面布局
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("Streamlit入门测试")
st.header("二级标题")
st.subheader("三级标题")

# 段落文字
st.subheader("简介：")
st.write("东北虎（学名：Panthera tigris altaica），又称西伯利亚虎，是现存体型最大的猫科动物，也是虎的亚种中体型最大者")
#图片
st.image("resource/东北虎.jpg")

# # 音频
# st.audio("")
#
# # 视频
# st.video("")
#
# # Logo
# st.logo("")

# 表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
# 三级标题
st.table(student_data)
# 段落文字
st.subheader("基本特征")
st.write("体型：成年雄性体长可达2.5-3米（含尾），体重180-300公斤；雌性较小，体重约100-160公斤")
st.write("毛色：橙黄色底色，黑色条纹稀疏且间距较宽，腹部白色；冬季毛色较浅、毛被更厚密以适应严寒")
st.write("分布：主要分布于俄罗斯远东地区（西伯利亚）、中国东北（黑龙江、吉林）及朝鲜半岛北部")


