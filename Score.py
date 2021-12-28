

def add_score(scores_file,new_score):
    with open(scores_file, 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        print ('current file data',data)
        if len(data)==0 :
            data=['0']
        print ('this is the existing score',data)
        total_score=int(data[0])
        new_total_score=total_score+new_score
        print ('new total score is ', new_total_score)
    with open(scores_file, 'w') as file:
        rc= file.write(str(new_total_score))
        print (rc)


def reset_score(scores_file):
    with open(scores_file, 'w') as file:
        rc=file.truncate()
        return rc



def get_score(scores_file):
    while 1==1:
        try:
            with open(scores_file, 'r') as file:
                return file.readlines()[0]
        except FileNotFoundError:
            reset_score(scores_file)
        else:
            return exception