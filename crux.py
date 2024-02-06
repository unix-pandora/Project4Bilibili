import sys
import getopt
import pivot


def main(argv):
    pattern = ""

    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["help", "pattern="])
    except getopt.GetoptError:
        print("Error: crux.py -p <pattern>")
        print("   or: crux.py --pattern=<pattern>")
        print("   or: -h <help>")
        print("   or: --help <help>")
        sys.exit(2)

    if len(opts) != 1:
        print("   crux.py -h <help>")
        print("   crux.py --help <help>")
        print("   crux.py -p <pattern>")
        print("   crux.py --pattern=<pattern>")
        print("   0:silent  1:audible")
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("   crux.py -p <pattern>")
            print("   or: crux.py --pattern=<pattern>")
            print("   0:silent    1:audible")
            sys.exit()
        elif opt in ("-p", "--pattern"):
            pattern = arg

    print("pattern is：", pattern)
    # 打印 返回值args列表，即其中的元素是那些不含'-'或'--'的参数。
    for i in range(0, len(args)):
        print("parameter %s is：%s" % (i + 1, args[i]))

    if pattern == "1":
        pivot.process_audible()
    elif pattern == "0":
        pivot.process_silent()
    else:
        print("Invaild option value:  0:silent    1:audible")


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])
