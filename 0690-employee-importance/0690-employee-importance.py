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
        # Step 1: Create a dictionary to store importance values
        importance_dict = {emp.id: emp for emp in employees}

        # Step 2: Initialize total importance
        totalImportance = 0

        # Step 3: DFS function
        def dfs(employee_id):
            nonlocal totalImportance
            # Add importance value of the current employee
            totalImportance += importance_dict[employee_id].importance
            # Recursively call DFS for direct subordinates
            for subordinate_id in importance_dict[employee_id].subordinates:
                dfs(subordinate_id)


        # Step 4: Start DFS traversal
        dfs(id)

        # Step 5: Return result
        return totalImportance
