import os
import sys

def get_unique_filename_with_path(dst):

    if os.path.exists(dst):
        i = 0
        o_dst = dst
        while os.path.exists(dst):
            file_name = os.path.splitext(os.path.basename(o_dst))
            #print(file_name)
            new_file_name = file_name[0] + f"_{i}" + file_name[1]
            #print(new_file_name)
            dst = os.path.join(os.path.dirname(o_dst), new_file_name)
            #print(dst)
            i+=1
            
    return dst


#def main():
#    ufn = get_unique_filename_with_path(sys.argv[1])
#    print(ufn)



#if __name__=="__main__":
#    main()