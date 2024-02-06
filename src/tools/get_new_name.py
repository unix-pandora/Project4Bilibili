import consultation
import matching
import dispose_json
import assemble_name


def build_new_name(dir_path, pattern):
    files_sets = consultation.traverse_files(dir_path)
    reciprocate = matching.find_by_pattern(files_sets, pattern)

    mine_list = list(reciprocate)
    print("\n", "List: ", str(mine_list))

    json_data = dispose_json.read_json_file(mine_list[0])
    video_name = assemble_name.assemble(json_data)

    return video_name
