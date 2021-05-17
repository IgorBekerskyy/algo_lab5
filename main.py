from read import read, write



def lps_list (pattern, length_of_pattern, lps):
    length = 0
    i = 1
    while i < length_of_pattern:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1




def search_substring_in_string(pattern, string):
    length_of_pattern = len(pattern)
    txt_length = len(string)
    lps = [0] * length_of_pattern
    j = 0
    final_result = []
    lps_list(pattern, length_of_pattern, lps)
    i = 0
    while i < txt_length:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == length_of_pattern:
            final_result.append( str(i - j) + "-" + str(i - j + length_of_pattern - 1) )
            j = lps[j - 1]
        elif pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return final_result



if __name__ == '__main__':
    res = read("file.in")
    string = res[0]
    pattern = res[1]
    write(search_substring_in_string(pattern, string), "final")