def is_balanced(source, caps):
    tags = []
    for c in source:
        if c in caps:
            tags.append(c)
    print("tags: ", tags)
    opening_tags = []
    dico_caps = {}
    for i in range(0, len(caps), 2):
        dico_caps[caps[i+1]] = caps[i]
    for t in tags:
        if t in dico_caps and dico_caps[t] == t and opening_tags and opening_tags[-1] == t:
            opening_tags.pop(-1)
        elif t in dico_caps.values():
            opening_tags.append(t)
        else:
            if opening_tags and dico_caps[t] == opening_tags[-1]:
                opening_tags.pop(-1)
            else:
                return False
    print("opening tags: ",opening_tags)
    return len(opening_tags) == 0


#https://www.codewars.com/kata/59590976838112bfea0000fa/train/python
