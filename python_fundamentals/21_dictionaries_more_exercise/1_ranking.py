def add_submission(password, contest, contest_user, user_points, password_list, submission_list):
    if contest in password_list:
        if password_list[contest] == password:
            submission_list.setdefault(contest_user, {contest: user_points})
            if username in submission_list:
                if contest in submission_list[contest_user]:
                    submission_list[contest_user][contest] = max(user_points, submission_list[contest_user][contest])
                else:
                    submission_list[contest_user][contest] = user_points


def best_candidate(submission_list, points_list):
    for user, submission in submission_list.items():
        for candidate_language, candidate_points in submission.items():
            points_list.setdefault(user, 0)
            points_list[user] += candidate_points
    return {user: candidate_points for user, candidate_points in sorted(points_list.items(),
                                                                        key=lambda item: item[1], reverse=True)}


def sort_submissions(submission_list):
    for sort_users, submissions_by_user in submission_list.items():
        submission_list[sort_users] = {language_by_user: user_points for language_by_user, user_points in
                                       sorted(submissions_by_user.items(), key=lambda item: item[1], reverse=True)}
    return {sort_users: submissions_by_user for sort_users, submissions_by_user in
            sorted(submission_list.items(), key=lambda item: item[0])}


password_input = input()
contest_passwords = {}
contest_submissions = {}
points_total = {}
while password_input != "end of contests":
    contest_name, contest_password = password_input.split(":")
    contest_passwords[contest_name] = contest_password
    password_input = input()

submission_input = input()
while submission_input != "end of submissions":
    contest_by_user, password_by_user, username, points = submission_input.split("=>")
    points = int(points)
    add_submission(password_by_user, contest_by_user, username, points, contest_passwords, contest_submissions)
    submission_input = input()

points_total = best_candidate(contest_submissions, points_total)
contest_submissions = sort_submissions(contest_submissions)

print(f"Best candidate is {list(points_total.keys())[0]} with total {list(points_total.values())[0]} points.")
print("Ranking:")
for users, submissions in contest_submissions.items():
    print(users)
    for language in submissions:
        print(f"#  {language} -> {submissions[language]}")
