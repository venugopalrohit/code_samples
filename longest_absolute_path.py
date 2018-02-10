# Google interview question
# https://discuss.leetcode.com/topic/31565/the-longest-absolute-path-in-file-system
#

def get_path_from_stack(input_stack):
    complete_path = ""
    for dir_name in input_stack:
        complete_path += dir_name

    return complete_path


def find_longest_path(input_string):

    max_length = 0
    max_path = ""
    stack_total_length = 0
    prev_depth = -1
    dir_stack = []

    list_of_directories = input_string.split("\n")
    #print(list_of_directories)

    for directory in list_of_directories:
        directory_name = directory.lstrip("\t")
        current_depth =  len(directory) - len(directory_name)

        while(current_depth <= prev_depth):
            stack_total_length -= len(dir_stack.pop())
            prev_depth -= 1

        #Check if directory name is actually file name
        if("." in directory_name):
            # Calculate total length of path and check with max seen so far
            total_length = len(directory_name) + stack_total_length
            if(total_length >= max_length):
                max_length = total_length;
                max_path = get_path_from_stack(dir_stack) + directory_name

        # This is a directory, so push it onto the directory stack
        else:
            # Calculating total length, including the path-directory seperator
            stack_total_length += len(directory_name + "\\")
            dir_stack.append((directory_name + "\\"))
            prev_depth = current_depth

    return(max_path)



input_string = "dir\n\tsubdir\n\t\tsubdir\n\t\t\tsubdir\n\t\t\t\tfile.txt\n\tsubdir1\n\t\tsubdirdir1\n\t\t\tfile1.txt"
input_array = ["dir", "subdir1", "subdirdir1", "file1.txt"]
print(find_longest_path(input_string))

