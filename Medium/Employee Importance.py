"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        s={}
        
        for employee in employees:
            s[employee.id]=employee
            
        stack=[id]
        value=0
        
        while stack:
            employee_id=stack.pop()
            employee=s[employee_id]
            value+=employee.importance
            stack.extend(employee.subordinates)
            
        return value