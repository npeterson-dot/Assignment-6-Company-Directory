
class EmployeeNode:
    '''
    A class to represent an employee in the company directory.
    Each employee can have a left and right direct report.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A binary tree that manages the company reporting structure.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Check whether a team lead has been added.
        if self.root is None:
            print("Tree is empty. Add a team lead first.")
            return False

        # Start searching at the root.
        if current_node is None:
            current_node = self.root

        # Check whether the current employee is the manager.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                    return True
                else:
                    print(f"⚠️ {manager_name} already has a LEFT employee.")
                    return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                    return True
                else:
                    print(f"⚠️ {manager_name} already has a RIGHT employee.")
                    return False

            else:
                print("❌ Invalid side. Please enter left or right.")
                return False

        # Recursively search the left side of the tree.
        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        # Recursively search the right side of the tree.
        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        # Only display this message once after searching the whole tree.
        if current_node == self.root:
            print(f"❌ Manager {manager_name} was not found.")

        return False

    def print_tree(self, node=None, level=0):
        # Start at the team lead.
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("The company directory is empty.")
                    return
            else:
                return

        # Indent employees based on their level in the hierarchy.
        indent = "   " * level
        print(f"{indent}- {node.name}")

        # Recursively print the left and right employees.
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here
def test_company_tree():
    print("Testing the company directory:\n")

    tree = TeamTree()
    tree.root = EmployeeNode("Jordan")

    tree.insert("Jordan", "Riley", "left")
    tree.insert("Jordan", "Taylor", "right")
    tree.insert("Riley", "Morgan", "left")
    tree.insert("Riley", "Dana", "right")

    print("\nTest reporting structure:")
    tree.print_tree()

    print("\nTesting an occupied position:")
    tree.insert("Jordan", "Alex", "left")

    print("\nTesting a missing manager:")
    tree.insert("Unknown", "Alex", "right")

    print("\nTesting an invalid side:")
    tree.insert("Jordan", "Alex", "middle")


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


# Run the tests and then start the interactive menu.
if __name__ == "__main__":
    test_company_tree()
    company_directory()


"""
Design Memo - Assignment #6: Company Directory

For this assignment, I created a company directory using a binary tree
to organize employees based on who they report to. Each employee is
represented by a node that stores their name and has two possible
connections, one on the left and one on the right. The TeamTree class
manages the overall structure, starting with the team lead at the root.

Recursive insertion works by starting at the root and checking whether
the current employee matches the manager's name. If it matches, the
program checks whether the requested position is available and adds
the new employee. If it does not match, the function continues searching
through the left and right branches until it finds the correct manager.
This allows the program to search through different levels without
needing separate code for each level.

One challenge with this process was making sure the program could find
the correct manager without stopping too early. I also had to account
for situations where a manager already had someone assigned to a
position or when the manager's name did not exist. Using recursion and
return values helped organize these checks and prevent employees from
being placed incorrectly.

Trees can be especially useful in real-world systems where information
has a clear hierarchy. Company reporting structures, computer folders,
and website navigation are good examples. Unlike a regular list, a
tree shows the relationships between different levels of information.
Overall, this assignment helped me better understand how recursion
can make it easier to organize and manage hierarchical data.
"""
