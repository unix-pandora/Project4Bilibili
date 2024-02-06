# 创建一个映射表，将需要替换的字符映射为空字符（''）
trans = str.maketrans(
    {
        "【": "",
        "】": "",
        "《": "",
        "》": "",
        "|": "",
        "｜": "",
        "）": "",
        "（": "",
        "(": "",
        ")": "",
        "{": "",
        "}": "",
        "?": "",
        "[": "",
        "]": "",
        ";": "",
        "#": "",
        "&": "",
        "*": "",
        "@": "",
        "!": "",
        "『": "",
        "』": "",
        "~": "",
        "%": "",
        "^": "",
        "_": "",
        "「": "",
        "」": "",
        "“": "",
        "”": "",
        " ": "",
        ",": "",
        "；": "",
    }
)
