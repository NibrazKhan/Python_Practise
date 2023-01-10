# create a tuple:
given_tuple=('banana','mango','apple')
#converting tuple to list:
to_list=list(given_tuple)
# updating the list:
to_list[1]="kiwi"
#Converting again to list.
new_tuple=tuple(to_list)
print(new_tuple)
