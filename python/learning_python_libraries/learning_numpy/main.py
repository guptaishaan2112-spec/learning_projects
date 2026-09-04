import numpy as np
stu=np.random.randint(0,100,size=(50,5))
avg_scores=np.mean(stu,axis=1)
print(stu)
print(f'avg marks of each student: {avg_scores}')
print('best student marks:',np.max(avg_scores))
print('worst student marks:',np.min(avg_scores))
print('subject wise avg marks:',np.mean(stu,axis=0))
print('subject wise best marks:',np.max(stu,axis=0))
print('students who failed in at least one subject:',np.sum(np.any(stu<40,axis=1)))
#since true=1 and false =0, we can sum the boolean array to get the count of students who failed in at least one subject.
'''stu = np.array([
    [50, 60, 30, 70, 80],
    [55, 65, 75, 85, 95],
    [20, 40, 50, 60, 70]
])

Then:

stu < 40

gives:

[[False False  True False False]
 [False False False False False]
 [ True False False False False]]
2. np.any(stu < 40, axis=1)

Checks each row:

[ True False  True]

Meaning:

Student 1 failed in at least one subject → True
Student 2 didn't fail any subject → False
Student 3 failed in at least one subject → True
3. np.sum(...)
np.sum([True, False, True])

Since:

True  = 1
False = 0

Result:

2
'''