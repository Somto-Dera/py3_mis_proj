punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(string_param):
    
    #punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in punctuation_chars:
        string_param = string_param.replace(char, "")

    return string_param
            
def get_neg(string_param):
    neg_count = 0
    string_param = strip_punctuation(string_param)
    string_param = string_param.lower()
    string_param = string_param.split()
    for char in negative_words:
        if char in string_param:
            neg_count+=1
        
    return neg_count


def get_pos(string_param):
    pos_count = 0
    string_param = strip_punctuation(string_param)
    string_param = string_param.lower()
    string_param = string_param.split()
    for char in positive_words:
        if char in string_param:
            pos_count+=1
        
    return pos_count


def get_net_score(tweet_txt):
    
    pos_count_lst = []
    neg_count_lst = []
    score_lst = []
    for char in tweet_txt:
        pos_count_lst.append(get_pos(char))
        neg_count_lst.append(get_neg(char))
        score_lst.append(get_pos(char) - get_neg(char))
    
    
    
    return pos_count_lst, neg_count_lst,score_lst

##################################################################


fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)

tweet_text = []
retweet_count = []
reply_count = []
positive_count_lst = []
negative_count_lst = []
net_score_lst = []
print ("done!")

for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[0] != "NA" and vals[1] != "NA" and vals[2] != "NA":
        #print("{}: {}; {}".format(vals[0], vals[1], vals[2]))
        tweet_text.append(vals[0])
        retweet_count.append(vals[1])
        reply_count.append(vals[2])

##################################################################

positive_count_lst, negative_count_lst, net_score_lst = get_net_score(tweet_text)
print (tweet_text)
print (retweet_count)
print (reply_count)
print(positive_count_lst)
print(negative_count_lst)
print(len(positive_count_lst))
print(net_score_lst)

##################################################################


outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for idx in range(0, len(positive_count_lst)):
    row_string = '{}, {}, {}, {}, {}'.format(retweet_count[idx], reply_count[idx], positive_count_lst[idx], negative_count_lst[idx], net_score_lst[idx])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
