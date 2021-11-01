#  Unique Email Addresses

def convert(email):
    name, domain = email.split('@')
    if '+' in name:
        name = name[:name.index('+')]
    name = "".join(name.split("."))
    return "".join([name, '@', domain])


def unique_email_addresses(emails):
    unique_email = set()
    for email in emails:
        unique_email.add(convert(email))
    return len(unique_email), unique_email



emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

print(unique_email_addresses(emails))



# Find and Replace Pattern

def checking(word, pattern):
    if len(set(list(word))) != len(set(list(pattern))):
        return False
    real_dict = {}
    for index, char in enumerate(word):
        if char in real_dict:
            if real_dict[char] != pattern[index]:
                return False
        else:
            real_dict[char]=pattern[index]
    return word


def find_and_eplace_pattern(words, pattern):
    possible_replace_words = []
    for word in words:
        result = checking(word, pattern)
        if result:
            possible_replace_words.append(word)
    return possible_replace_words


# words = ["abc","deq","mee","aqq","dkd","ccc"]
# pattern = "abb"
words = ["a", "b", "c", "d"]
pattern = "a"
find_and_eplace_pattern(words, pattern) 




#  Finding the Users Active Minutes

def finding_the_users_active_minutes(logs, k):
        _dict = {}
        for i in range(len(logs)):
            if logs[i][0] in _dict:
                _dict[logs[i][0]] += [logs[i][1]]
            else:
                _dict[logs[i][0]] = [logs[i][1]]
        
        acc = [0 for _ in range(k)]
        for key in _dict:
            acc[len(set(_dict[key]))-1] += 1
        return acc



logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]; k = 5
# logs = [[1,1],[2,2],[2,3]]; k = 4
finding_the_users_active_minutes(logs, k)



# Jewels and Stones

def jewels_and_stones(jewels, stones):
    return sum([char in jewels for char in stones])

# jewels = "aA"; stones = "aAAbbbb"
jewels = "z"; stones = "ZZ"
jewels_and_stones(jewels, stones)


# Beautiful binary string

def beautiful_binary_string(acc):
    return acc.count("010")

beautiful_binary_string("01010101")


# String power

def string_power(s, k):
    if k < 0:
        if s[:abs(k)] * abs(k) == s:
            return s[:abs(k)]
        else:
            return "undefined"
    else:
        return s*k
    
string_power("xyzxyz", -3)

