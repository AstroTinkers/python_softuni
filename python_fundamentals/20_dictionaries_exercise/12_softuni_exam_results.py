command = input()
judge_collection = {}
submissions = {}
ban_list = []
while command != "exam finished":
    if "banned" in command:
        ban_list.append(command.split("-")[0])
    else:
        username, language, points = command.split("-")
        points = int(points)
        if language in judge_collection:
            if username in judge_collection[language]:
                judge_collection[language][username] = max(points, judge_collection[language][username])
            else:
                judge_collection[language][username] = points
        else:
            judge_collection.setdefault(language, {username: points})
        submissions.setdefault(language, 0)
        submissions[language] += 1
    command = input()
print("Results:")
for results in judge_collection.values():
    for student, score in results.items():
        if student not in ban_list:
            print(f"{student} | {score}")
print("Submissions:")
for language, submission in submissions.items():
    print(f"{language} - {submissions[language]}")
