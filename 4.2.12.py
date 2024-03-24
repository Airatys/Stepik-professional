import csv

with open('student_counts.csv', encoding='utf-8') as file_1, open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_2:
    dat = csv.DictReader(file_1, delimiter=',')
    commit = dat.fieldnames
    commit = [commit[0]] + sorted(commit[1:], key=lambda x: (len(x), x))
    wet = csv.DictWriter(file_2, fieldnames=commit, delimiter=',')
    wet.writeheader()
    for i in dat:
        wet.writerow(i)




