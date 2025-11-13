list3=[1,2,3,4,1,2]
count=Counter(list3)
duplicate_item = [item for item,count in count.items() if count > 1]
duplicate_with_count ={item:count for item,count in count.items() if count > 1}
print(duplicate_item) #[1, 2]
print(duplicate_with_count) #{1: 2, 2: 2}