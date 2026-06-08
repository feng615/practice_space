# 导入模块
import requests
from lxml import html
import csv

#常量
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" #获取电影榜单(默认获取第一页的内容)
TMDPB_follow_url = "https://www.themoviedb.org/discover/movie/items"#获取后续的电影榜单(即第二页以后)
# 获取电影详情数据
def get_movie_detail(movie_detail_url):
    # 获取网页数据
    request = requests.get(movie_detail_url)
    print(f"发送请求{movie_detail_url},获取电影详情中~")
    # 解析数据
    movie_doc = html.fromstring(request.text)
    # 获取电影名称
    all_movie_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    all_movie_year = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    all_movie_datetime = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    all_movie_type = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    all_movie_time = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    # 评分数据加密了，需要先获取元素，再切片获取数据
    all_movie_score = movie_doc.xpath("//*[@id ='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_scores = all_movie_score[0]
    all_movie_language = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    all_movie_director = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    all_movie_author = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    all_movie_actor = movie_doc.xpath("//*[@id='cast_scroller']/ol/li[@class='card']/p[1]/a/text()")
    all_movie_introduction = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    all_movie_slogan = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")

    # 返回电影详情——字典存储
    movie_info ={
        "电影名":all_movie_name[0].strip() if all_movie_name else "",
        "上映年份":all_movie_year[0].strip() if all_movie_year else "",
        "上映时间":all_movie_datetime[0].strip() if all_movie_datetime else "",
        "电影类型":",".join(all_movie_type) if all_movie_type else "",
        "电影时长":all_movie_time[0].strip() if all_movie_time else "",
        "评分":movie_scores if movie_scores else "",
        "语言":all_movie_language[0].strip() if all_movie_language else "",
        "导演":",".join(all_movie_director) if all_movie_director else "",
        "作者":",".join(all_movie_author) if all_movie_author else "",
        "主演":",".join(all_movie_actor) if all_movie_actor else "",
        "简介":all_movie_introduction[0].strip() if all_movie_introduction else "",
        "口号":all_movie_slogan[0].strip() if all_movie_slogan else ""

    }
    return movie_info

# 保存电影详情数据
def save_movies_info(all_movies_info):

    # csv文件保存
    with open("csv.data/movies.csv", "w", encoding="UTF-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "上映年份", "上映时间", "电影类型", "电影时长", "评分", "语言", "导演", "作者", "主演", "简介", "口号"])
        writer.writeheader()
        writer.writerows(all_movies_info)


# 主函数
def main():
    all_movies_info = []
    for page_num in range(1, 6):
       if page_num <= 1:
           # 获取网页高分榜单数据
           request = requests.get(TMDB_TOP_URL, timeout=60)
           # print(f"------>获取的源码：{request.text}")
       else:
           request = requests.post(TMDPB_follow_url, data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-12-01&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",timeout=60)
       print(f"发送请求，获取TMDB电影榜单{page_num}数据中~")

       # 解析数据，获取电影榜单列表
       doc = html.fromstring(request.text)
       div_list = doc.xpath( f"//*[@id='page_{page_num}']/div[1]/div/div")
       # 遍历电影榜单数据，获取电影详情
       for movie in div_list:
           movie_url = movie.xpath(".//a/@href")
           if movie_url:
               # 电影详情链接
               movie_detail_url = TMDB_BASE_URL + movie_url[0]
               print(f"------>电影详情链接：{movie_detail_url}")
               # 获取电影详情数据
               movie_detail = get_movie_detail(movie_detail_url)
               all_movies_info.append(movie_detail)


    # 电影详情数据到csv表格
    print("数据正在保存中~")
    save_movies_info(all_movies_info)
    print("数据保存完毕~")




if __name__ == '__main__':
    main()