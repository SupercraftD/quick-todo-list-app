todo=[]

def main():
    prompt()

def prompt():
    global todo
    print('Tasks:')
    if len(todo)==0:
        print('No tasks yet')
    else:
        for i in todo:
            print(i['name'],i['priority'])
    print()
    print('1: create new task\n2: mark task as done')
    c=input('command: ')
    if c=='1':
        name=input('name: ')
        priority=input('priority: ')
        if not priority.isnumeric():
            while priority.isnumeric():
                priority=input('(number) priority: ')
        todo.append({
            'name':name,
            'priority':int(priority)
        })
    elif c=='2':
        name=input('name: ')
        exists=False
        ic=0
        for v,i in enumerate(todo):
            if i['name']==name:
                exists=True
                ic=v
        if not exists:
            while not exists:
                name=input('(valid) name: ')
                for v,i in enumerate(todo):
                    if i['name']==name:
                        exists=True
                        ic=v
        del todo[ic]

    todo=list(sorted(todo,key=lambda e:e['priority']))
    prompt()







if __name__ == '__main__':
    main()