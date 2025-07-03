def get_num_words(text):
    return len(text.split())
def sort_on(items):
    return items["num"]
def get_letter_lib(text):
    words=text.lower().split()
    lib={}
    for word in words:
        for i in word:
            if i in lib:
                lib[i]+=1
            else:
                lib[i]=1
    return lib
def sort_dict_list(dict):
    new_list=[]
    for entry in dict:
        new_list.append({"char":entry,"num":dict[entry]})
    #print("new list",new_list)
    new_list.sort(reverse=True,key=sort_on)
    return new_list