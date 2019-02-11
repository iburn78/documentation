from konlpy.tag import Twitter # Twitter starts with capital T, so it is a class
twitter = Twitter()
maillist = twitter.pos("고구려의 영역은 어디까지일까", norm=True, stem=True)
print(maillist)

print(twitter.morphs(u' ')) 
# u' ' means string is unicode, but no longer used in Python3 as it is automatic

print(twitter.morphs(' 정부와 기업이 함께 근로자의 휴가비를 지원 ')) # slices words into each word
print(twitter.nouns('직장 내 자유로운 휴가 분위기를 조성하고 일과 휴식이 균형을 이루는 근무 여건을 만들기 위해 지난해부터 시행한 사업이다. ')) # extracts nouns
print(twitter.pos('이것도 되나욬ㅋㅋㅋ')) # each word and its category
print(twitter.pos('이것도 되나욬ㅋㅋㅋ', norm=True)) # norm option converts to nomral words
print(twitter.pos('이것도 되나욬ㅋㅋㅋ', norm=True, stem=True)) # stem option converts words to root words
# Last statement is most frequently used
