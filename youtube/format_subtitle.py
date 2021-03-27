import argparse

parser = argparse.ArgumentParser(description="crawlYoutube command flags")

parser.add_argument("--file", "-f", type=str, help="file name to convert type")
parser.add_argument("--save_dir", "-s", type=str,
                    help="Directory to save file")

args = parser.parse_args()

line_array = []

def process_array_of_line(array,time_begin,time_end):
    # Split first element of array and remove  "<>" 
    temp = array[0]
    temp = temp.replace('>','')
    temp = temp.split('<')
    # print(temp)
    array.pop(0)
    new_array = []
    for x in array:
        x = x.replace('>','')
        x = x.replace('<','')
        new_array.append(x)
        
    new_array.insert(0,temp[1])
    new_array.insert(0,temp[0])
    new_array.insert(0,time_begin)
    new_array.remove('\n')
    new_array.append(time_end)

    return new_array


def process_main_line(line,line_array,time_begin,time_end):
    # When we get a line that doesn't have specific time begin
    # time end for each word (just have for the entire frame script)
    if "<c>" not in line:
        temp_array = []
        word_dict = {}
        word_dict['text'] =  line
        word_dict['start'] = time_begin
        word_dict['end'] = time_end
        temp_array.append(word_dict)
        line_array.append(temp_array)
        return
                
    # Else we have time begin time end for individual word
    line_split = line.split('<c> ')

    new_line_split = []
    for x in line_split:
        x = x.split('</c>')
        new_line_split = new_line_split + x

    line_split = process_array_of_line(new_line_split,time_begin,time_end)

    temp_array = []
    for x in range(len(line_split)):
        if x % 2 == 1:
            word_dict = {}
            word_dict['text'] = line_split[x]
            word_dict['start'] = line_split[x-1]
            word_dict['end'] = line_split[x+1]
            temp_array.append(word_dict)
    line_array.append(temp_array)
# './result/csty.vtt'
num_lines = sum(1 for line in open(args.file)) + 1
f = open(args.file)
# Remove 3 first line 
print(f.readline())
print(f.readline())
print(f.readline())

# Remove blank line
f.readline()

# Read block 1 (contain 5 lines)
# Block 1
line1 = f.readline()
f.readline()
line2 = f.readline()
f.readline()
line3 = f.readline()

line1_split = line1.split(' ')
line3_split = line3.split(' ')

time_begin = line1_split[0]
time_end = line3_split[0]

process_main_line(line2,line_array,time_begin,time_end)
print(line_array)

# End block 1
num_block = (num_lines - 9)/8
# Read block 2 - end (each block contain 9 lines)
for x in range(int(num_block)):
    time_begin = time_end

    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    main_line = f.readline()
    print(main_line)
    f.readline()

    line3 = f.readline()
    line3_split = line3.split(' ')
    time_end = line3_split[0]
    
    process_main_line(main_line,line_array,time_begin,time_end)
    # if x == 508:
    #     break

print(len(line_array))
# print(line_array)
fwrite = open(args.save_dir,'a')
fwrite.write(str(line_array))
fwrite.close()
f.close()