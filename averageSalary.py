import math
class Solution: 
    def averageSalary(self, salary: list[int]) -> float:
        # given an array of unique integers, salary, 
        # where salary[i] is the salary of the ith employee

        # return the avg salary of employees excluding the minimum and maximum salary
        max_sal = max(salary)
        min_sal = min(salary)
        
        # remove the min and max
        salary.pop(salary.index(max_sal))
        salary.pop(salary.index(min_sal))
        sal_counter = 0.0

        for i in salary:
            sal_counter += i
        return sal_counter/len(salary)


if __name__ == '__main__':
    salary = [400,200,300,100]
    test = Solution()
    print(test.averageSalary(salary=salary))