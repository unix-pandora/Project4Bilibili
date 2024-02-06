import public_constant as pubcon


def assemble(json_data):
    avid = json_data["avid"]
    title = json_data["title"]
    page = json_data["page_data"]["page"]

    print("avid:", str(avid), " title:", str(title), " page:", str(page))

    video_name = str(avid) + "-" + title + "-" + str(page) + ".mp4"
    # 使用translate方法替换字符
    video_name = video_name.translate(pubcon.trans)

    print("assemble video name: ", video_name)
    return video_name
