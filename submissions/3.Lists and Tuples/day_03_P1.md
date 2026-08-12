  Here are your **10 Lists and Tuples revision questions**. Answer them in any format — short explanations, code snippets, or bullet points. I'll check each one before we move to coding assignments.

---

### Easy (1–3)

**Q1.** What is the fundamental difference between a `list` and a `tuple` in Python? Mention at least two distinctions beyond just the syntax (parentheses vs brackets).

## ans: List in python is mutable sequencial data type and Tuple in python is immutable sequencial Data type.Mutable means we can add,remove or update the element inside(inplace) the list wheras immutable means inplace manupulation of element in tuple is not possible once the tuple is declaired it cannot be updated.List data type used for the applications where manupulation is required. wheareas the tuples are used to store data which doesnt required the manupulation. 

**Q2.** You have `items = [10, 20, 30, 40, 50]`. What are three different ways to access the value `50`? Write the exact code for each.

## ans: Through the positive indexing  items[4], Negativeindexing items[-1] and list poping items.pop().

**Q3.** What is the difference between `my_list.append([4, 5])` and `my_list.extend([4, 5])`? If `my_list` starts as `[1, 2, 3]`, what does it look like after each operation?

## ans: using my_list.append([4, 5]) the list is appended inside the main list and Through .extend all the elements of the extended list are added in the main list at the end.
ex: my_list.append([4, 5]) will be my_list = [1,2,3,[4,5]] and my_list.extend([4, 5]) will be my_list = [1,2,3,4,5]

---

### Medium (4–7)

**Q4.** What does `numbers[1:6:2]` mean when slicing a list? In plain English, describe what each of the three values (1, 6, 2) represents.
## ans:In this given example there are three values is included which are start index, end index and step index. 1 is the stating index which means the slicing start with this index and then 6 is the ending index and its not included and the 2 is the step index which means after the each index the index is incremented by 1 ex after index 1 index 2 is skipped and jumpped to index 3.

**Q5.** Explain the difference between `new_list = old_list` and `new_list = old_list.copy()`. If you modify `new_list` afterward, how does `old_list` behave in each case?

## ans: Here 'new_list = old_list' means we have created one more varible which is referncing the same object now both new and old list are pointing to same object. Whereas `new_list = old_list.copy()` means new_list created new object and which conatains copy of the main list. if we modify the new_list in first case then this affects the old_list also bcz both are referencing the same object but in second case the chnanges done are not affect the old_list.

**Q6.** Write a single line of Python (list comprehension) that takes `nums = [1, 2, 3, 4, 5, 6]` and produces a new list containing only the squares of even numbers.

## ans: nums_sqr = [x*x for x in nums]

**Q7.** What does the `*` operator do when unpacking a tuple or list? Give an example where `first, *middle, last = (10, 20, 30, 40, 50)` is useful.

## ans:When unpacking a tuple or list, the * operator (called the starred expression) captures all remaining elements that are not explicitly assigned to other variables and groups them into a new list. first = 10 middle =[20,30,40] last = 50.
---

### Hard (8–10)

**Q8.** Why is inserting an element at the beginning of a list (`my_list.insert(0, x)`) generally much slower than appending to the end (`my_list.append(x)`)? Explain in terms of how Python stores lists in memory.

## Inserting at the beginning of a list is much slower because Python lists are implemented as contiguous arrays of memory pointers. When you insert an item at index 0, Python cannot simply grow the array backward. It must keep the memory contiguous. To make room for the new element at the front:Python must move the existing element at index 0 to index 1.It must move index 1 to index 2, index 2 to index 3, and so on.If the list has \(N\) elements, Python has to perform \(N\) shift operations in memory.Time Complexity: \(O(N)\) (Linear time). As the list grows larger, the operation takes proportionally longer.

**Q9.** Tuples are immutable — but if you have `data = (1, [2, 3], 4)`, can you modify the inner list `[2, 3]` to become `[2, 3, 5]` without creating a new tuple? Explain why this is possible (or not) and what concept this demonstrates.

## Yes we can modify the same without creating new tuple. in python tuple is immutable which means the reference it holds cannot be chnaged once declaired but tuple doesnot care wheather the object pointed to by those references are mutable or immutable.This behavior demonstrates the concept of Shallow Immutability (or the difference between Object Identity vs. Object Value).

**Q10.** Under what condition can a tuple be used as a key in a dictionary, while a list cannot? If you have `points = {(1, 2): "A", (3, 4): "B"}`, why does this work, but `points = {[1, 2]: "A"}` raises a `TypeError`?

## A tuple can be used as a dictionary key only if all of its elements are completely hashable (immutable), whereas a list can never be used as a key because lists are inherently unhashable (mutable).Dictionary lookups in Python rely on a mechanism called a hash table. For a hash table to work efficiently and reliably, dictionary keys must be hashable. An object is hashable if it has a hash value that never changes during its entire lifetime.If you attempt to use a list as a key, Python immediately raises TypeError: unhashable type: 'list'.


---

**Reply with your answers to all 10, and I'll grade them.**