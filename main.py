from max_list_func import max_list_sum

num=int(input('请输参与计算整数的数目：'))
the_lists=input('请输入数据，每个数据间用" "隔开：')
the_lists=the_lists.split(' ')
the_lists=list(map(int,the_lists))
assert len(the_lists)==num ,'输入数据的总数与输入总数目不符'
print(max_list_sum(the_lists,num))