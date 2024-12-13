class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stulen = len(students)
        sanlen = len(sandwiches)
        count = 0
        attempt = 0
        l = 0
        r = 0

        while count < stulen:
            if(students[l] == -1):
                l = (l + 1) % stulen
                continue

            if students[l] == sandwiches[r]:
                students[l] = -1
                l = (l + 1) % stulen
                r += 1
                attempt  = 0
                count += 1
            else:
                l = (l + 1) % stulen
            attempt += 1
            if attempt == stulen:
                break
        
        return stulen - count 


import queue
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        Q = queue.Queue()
        stulen = len(students)
        sandlen = len(sandwiches)  
        attempt = 0
        r = 0
        count = 0
        l = 0
        for stu in students:
            Q.put(stu)

        while not Q.empty():
            current_student = Q.get()

            if current_student == sandwiches[r]:
                r += 1
                count += 1
                attempt = 0
            else:
                Q.put(current_student)
                attempt += 1

       
            if(attempt == stulen):
                 break
        return stulen - count

        