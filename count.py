import os

def countLOCInFolder(dir = './'):
    allcount = 0
    emptycount = 0
    commentcount = 0
    codecount = 0
    errorcount = 0

    for file in os.listdir(dir):
        if file.startswith('.'):
            continue
        
        if not os.path.isfile(dir + file):
            (allcount_rec, emptycount_rec, commentcount_rec, codecount_rec, errorcount_rec) = countLOCInFolder(dir + file + '/')
            allcount += allcount_rec
            emptycount += emptycount_rec
            commentcount += commentcount_rec
            codecount += codecount_rec
            errorcount += errorcount_rec
        else:
            try:
                with open(dir + file, 'r') as f:
                    for line in f.read().split('\n'):
                        allcount += 1
                        if (line.strip() == ''):
                            emptycount += 1
                        elif (line.strip().startswith('#')):
                            commentcount += 1
                        else:
                            codecount += 1
            except:
                errorcount =+ 1

    return (allcount, emptycount, commentcount, codecount, errorcount)


(allcount, emptycount, commentcount, codecount, errorcount) = countLOCInFolder()

print(f'All lines: {allcount}')
print(f'Empty lines: {emptycount}')
print(f'Comment lines: {commentcount}')
print(f'Comment rate: {format(float(commentcount/allcount),".4f")}')
print(f'Code lines: {codecount}')
print(f'Files skipped: {errorcount}')