def add_submission(contest_name, contest_user, user_points, submissions):
    submissions.setdefault(contest_name, {contest_user: user_points})
    if contest_name in submissions:
        if contest_user in submissions[contest_name]:
            submissions[contest_name][contest_user] = max(user_points, submissions[contest_name][contest_user])
        else:
            submissions[contest_name][contest_user] = user_points


def sort_submissions(submission_list):
    sorted_sub = submission_list.copy()
    for sort_users, submissions_by_user in submission_list.items():
            submission_list[sort_users] = {language_by_user: user_points for language_by_user, user_points in
                                           sorted(submissions_by_user.items(), key=lambda item: (-item[1], item[0]))}
    if sorted_sub == submission_list:
        return sorted_sub
    else:
        return submission_list


def best_rank(submission_list, points_list):
    for contest, submission in submission_list.items():
        for candidate, candidate_points in submission.items():
            points_list.setdefault(candidate, 0)
            points_list[candidate] += candidate_points
    return {candidate: candidate_points for candidate, candidate_points in
            sorted(points_list.items(), key=lambda item: (-item[1], item[0]))}


contest_data = input()
contests = {}
ranking = {}
position_number = 0
while contest_data != "no more time":
    user, contest, points = contest_data.split(" -> ")
    points = int(points)
    add_submission(contest, user, points, contests)
    contest_data = input()
sort_submissions(contests)
ranking = best_rank(contests, ranking)
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
