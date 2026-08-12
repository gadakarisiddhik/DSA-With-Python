"""
O(n), when Data increase cheaking process will br increase
"""
def find_paper(papers,name):
    for paper in papers:
        if paper == name:
            return True
    return False

paper_names = ["Pooja","Quahira","Rushikesh","Siddik","Tipu","Umar","Ved","Karan"]
search_name  = "Karan"

result = find_paper(paper_names , search_name)
if result:
    print("Paper Found")
else:
    print("Paper Not Found")
