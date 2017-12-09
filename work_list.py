def initTitle(some_arg=None):
    title_str=''
    if some_arg is None:
        title_str='Default title:'
    else:
        title_str=str(some_arg)
        hr_line=''
        for i in range(0,len(title_str)):
            hr_line+='-'
        print('%s\n%s\n%s'%(hr_line,title_str,hr_line))
def addTip(some_arg=None):
    tip_str=''
    if some_arg is None:
        tip_str='(Default tip)'
    else:
        tip_str='('+str(some_arg)+')'
        hr_line=''
        for i in range(0,len(tip_str)):
            hr_line+='-'
        print('%s\n%s'%(tip_str,hr_line))
def listEmpty(some_list):
    if len(some_list)>0:
        return False
    else:
        addTip('List is empty')
        return True
def showList(main_list):
    initTitle('Show list:')
    list_empty=listEmpty(main_list)
    if list_empty:
        pass
    else:
        for i in range(0,len(main_list)):
            item=main_list[i]
            if item['res']!='' and item['pos']!='':
                print('%s.Company name: %s\n\tCity: %s\n\tType: %s\n\tResponse:%s\n\tPositive:%s'%(
                    (i+1),
                    item['name'],
                    item['city'],
                    item['type'],
                    item['res'],
                    item['pos']
                ))
            else:
                print('%s.Company name: %s\n\tCity: %s\n\tType: %s'%(
                    (i+1),
                    item['name'],
                    item['city'],
                    item['type']
                ))
def addItem(main_list):
    initTitle('Add item:')
    addTip('Type new item name or press \'Enter\' to exit')
    new_item=dict(id='',name='',city='',type='',res='',pos='')
    item_len=len(new_item)
    item_ready=0
    exit_loop=False
    while not exit_loop:
        for key in new_item:
            if key=='id':
                new_item[key]=(len(main_list)+1)
                item_ready+=1
            elif key=='res' or key=='pos':
                item_ready+=1
            else:
                add_input=input('Type '+key+':')
                if add_input!='':
                    new_item[key]=add_input.strip()
                    item_ready+=1
                else:
                    addTip('Input '+key+' is empty!')
                    exit_loop=True
        if item_ready==item_len:
            main_list.append(new_item)
            initTitle('(>>>Item added<<<)')
            exit_loop=True
def editItem(main_list):
    initTitle('Edit item:')
    list_empty=listEmpty(main_list)
    if list_empty:
        pass
    else:
        addTip('Type item number or press \'Enter\' to exit')
        new_item=dict(id='',name='',city='',type='',res='',pos='')
        item_len=len(new_item)
        item_ready=0;
        exit_loop=False
        while not exit_loop:
            user_input=input('Type number:')
            if user_input!='':
                try:
                    search_num=int(user_input)
                    list_len=len(main_list)
                    if search_num>list_len or search_num==0:
                        addTip('Item not in list. List has '+str(list_len)+' items.')
                    else:
                        i=0
                        while i<list_len:
                            old_item=main_list[i]
                            if search_num==old_item['id']:
                                for key in new_item:
                                    if key=='id':
                                        new_item[key]=old_item[key]
                                        item_ready+=1
                                    else:
                                        key_type=''
                                        old_key=''
                                        if key=='res':
                                            key_type='response'
                                            old_key='response'
                                        elif key=='pos':
                                            key_type='positive'
                                            old_key='positive'
                                        else:
                                            key_type='new '+key
                                            old_key=key
                                        initTitle('Old item '+old_key+':\''+old_item[key]+'\'')
                                        addTip('Type \'>>>\' to leave old item.')
                                        new_key=input('Type '+key_type+':')
                                        if new_key!='':
                                            if len(new_key)==3 and new_key=='>>>':
                                                addTip('Item '+key+' not changed.')
                                                new_item[key]=old_item[key]
                                                item_ready+=1
                                            else:
                                                new_item[key]=new_key.strip()
                                                item_ready+=1
                                        else:
                                            addTip('Input '+key_type+' is empty!')
                                            exit_loop=True
                                break
                            else:
                                i+=1
                        if item_ready==item_len:
                            initTitle('(>>>Item edited<<<)')
                            old_item_index=main_list.index(old_item)
                            main_list.insert(old_item_index, new_item)
                            main_list.remove(old_item)
                            exit_loop=True
                except ValueError:
                    addTip('ERROR:Must be number!')
            else:
                addTip('Input number is empty!')
                exit_loop=True
def removeItem(main_list):
    initTitle('Remove item:')
    list_empty=listEmpty(main_list)
    if list_empty:
        pass
    else:
        addTip('Type item number or press \'Enter\' to exit')
        exit_loop=False
        while not exit_loop:
            user_input=input('Type number:')
            if user_input!='':
                try:
                    search_num=int(user_input)
                    list_len=len(main_list)
                    if search_num>list_len or search_num==0:
                        addTip('Item not in list. List has '+str(list_len)+' items.')
                    else:
                        i=0
                        while i<list_len:
                            item=main_list[i]
                            if item['id']!=(i+1):
                                item['id']=(i+1)
                            else:
                                pass
                            if search_num==item['id']:
                                main_list.remove(item)
                                list_len=len(main_list)
                                i=i
                                search_num=0
                                initTitle('(>>>Item removed<<<)')
                                exit_loop=True
                            else:
                                i+=1
                except ValueError:
                    addTip('ERROR:Must be number!')
            else:
                addTip('Input number is empty!')
                exit_loop=True
def exitApp(main_list):
    openList('w',main_list)
    initTitle('Exit app')
    exit()
def showOptions(options):
    initTitle('Options:')
    opt_i=0
    for key in options:
        opt=options[key]
        opt_i+=1
        if opt['name']=='Exit':
            print('%s.To %s type:\'%s\''%(opt_i,opt['name'],key))
        elif opt['name']=='List':
            print('%s.To show %s type:\'%s\''%(opt_i,opt['name'],key))
        else:
            print('%s.To %s item type:\'%s\''%(opt_i,opt['name'],key))
def mainLoop(options,main_list):
    user_input=''
    while user_input!='x':
        showOptions(options)
        user_input=input('Type option:')
        try:
            letter=user_input.strip().lower()
            opt=options[letter]['func']
            opt(main_list)
        except KeyError:
            addTip('ERROR:No option!')
            user_input=''
def openList(file_mode,append_obj=None):
    file_name='work_list.json'
    file_path=cwd+'\\'+file_name
    main_list=[]
    with open(file_path,file_mode) as file:
        if file_mode=='r':
            initTitle('File loaded')
            main_list=json_module.load(file)
        elif file_mode=='w':
            json_module.dump(append_obj,file)
            initTitle('File saved')
        else:
            initTitle('File created')
    return main_list
def listApp():
    initTitle('---Work list App---')
    options={
        'l':{'name':'List','func':showList},
        'a':{'name':'Add','func':addItem},
        'e':{'name':'Edit','func':editItem},
        'r':{'name':'Remove','func':removeItem},
        'x':{'name':'Exit','func':exitApp}
    }
    import os
    global json_module
    import json as json_module
    global cwd
    cwd=os.getcwd()
    try:
        main_list=openList('r')
    except FileNotFoundError:
        main_list=openList('a')
    mainLoop(options,main_list)
listApp()
