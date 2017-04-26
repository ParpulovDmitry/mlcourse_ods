import argparse
import tqdm
import codecs
import re

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="Path to input file")
parser.add_argument("-o", "--output", type=str, help="Path to output file")


args = parser.parse_args()
in_file = args.input
out_file = args.output

search_tags = "(?:^| )(?:javascript|java|python|ruby|php|c\+\+|c\#|go|scala|swift)(?:$| )"
map_dict = {'javascript': '1', 'java': '2', 'python': '3', 'ruby': '4', 'php': '5', 
            'c++': '6', 'c#': '7', 'go': '8', 'scala': '9', 'swift': '10'}

with codecs.open(out_file, 'w', encoding='utf-8') as f_out:
    with codecs.open(in_file, 'r', encoding='utf-8') as f_in:
        for i,line in enumerate(f_in):
            if i % 1000000 == 0:
                print i

            if not "\t" in line or len(re.findall(r"\t", line)) > 1:
                continue
            
            body, tags = line.split("\t")
            
            if len(re.findall(search_tags, tags)) == 1:
                tag = re.findall(search_tags, tags)[0].strip()
                body = re.sub('(?:\?|\|)', '', body)
                new_line = map_dict[tag] + " | " + body.strip() + "\n"
                f_out.write(new_line)

