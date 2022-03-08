def add_submission(contest_name, contest_user, user_points, submissions, max_points):
    submissions.setdefault(contest_name, {contest_user: user_points})
    max_points.setdefault(contest_user, 0)
    if contest_name in submissions:
        if contest_user in submissions[contest_name]:
            submissions[contest_name][contest_user] = max(user_points, submissions[contest_name][contest_user])
            max_points[contest_user] += user_points
        else:
            submissions[contest_name][contest_user] = user_points
            max_points[contest_user] += user_points


def sort_submissions(submission_list):
    for sort_users, submissions_by_user in submission_list.items():
        submission_list[sort_users] = {language_by_user: user_points for language_by_user, user_points in
                                       sorted(submissions_by_user.items(), key=lambda item: (-item[1], item[0]))}


contest_data = input()
contests = {}
ranking = {}
position_number = 0
while contest_data != "no more time":
    user, contest, points = contest_data.split(" -> ")
    points = int(points)
    add_submission(contest, user, points, contests, ranking)
    contest_data = input()
sort_submissions(contests)
ranking = {user: points for user, points in sorted(ranking.items(), key=lambda item: -item[1])}
for contest, users in contests.items():
    print(f"{contest}: {len(users)} participants")
    position_number = 1
    for user, points in users.items():
        print(f"{position_number}. {user} <::> {points}")
        position_number += 1
print("Individual standings:")
position_number = 1
for user, points in ranking.items():
    print(f"{position_number}. {user} -> {points}")
    position_number += 1
