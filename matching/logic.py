from itertools import combinations
from accounts.models import Profile

# --------------------------
# Configuration
# --------------------------
SKILL_WEIGHT = 2.0
INTEREST_WEIGHT = 1.5
BRANCH_DIVERSITY_WEIGHT = 1.0
YEAR_WEIGHT = 0.5
MAX_TEAM_SIZE = 4


# --------------------------
# Fetch student data
# --------------------------
def get_student_data():
    students = []

    for profile in Profile.objects.all():
        students.append({
            "id": profile.user.id,
            "name": profile.name,
            "skills": profile.skills_list(),
            "interests": profile.interest_list(),
            "year": profile.year,
            "branch": profile.branch,
            "gender": profile.gender,
            "user_id": profile.user.id,
        })

    return students


# --------------------------
# Compatibility Score
# --------------------------
def compatibility_score(student1, student2):

    score = 0

    # Skills
    common_skills = set(student1["skills"]) & set(student2["skills"])
    score += len(common_skills) * SKILL_WEIGHT

    # Interests
    common_interests = set(student1["interests"]) & set(student2["interests"])
    score += len(common_interests) * INTEREST_WEIGHT

    # Branch diversity
    if student1["branch"] != student2["branch"]:
        score += BRANCH_DIVERSITY_WEIGHT

    # Same / nearby year
    try:
        diff = abs(int(student1["year"]) - int(student2["year"]))

        if diff == 0:
            score += YEAR_WEIGHT

        elif diff == 1:
            score += YEAR_WEIGHT / 2

    except:
        pass

    return round(score, 2)


# --------------------------
# Weighted Graph
# --------------------------
def build_weighted_graph(students, threshold=0):

    graph = {s["id"]: [] for s in students}
    edges = []

    for s1, s2 in combinations(students, 2):

        weight = compatibility_score(s1, s2)

        if weight > threshold:

            graph[s1["id"]].append((s2["id"], weight))
            graph[s2["id"]].append((s1["id"], weight))

            edges.append((s1["id"], s2["id"], weight))

    edges.sort(key=lambda x: x[2], reverse=True)

    return graph, edges


# --------------------------
# Greedy Team Formation
# --------------------------
def form_teams(students, max_team_size=MAX_TEAM_SIZE):

    if not students:
        return {}

    student_map = {s["id"]: s for s in students}

    assigned = set()

    teams = {}

    team_no = 1

    for student in students:

        if student["id"] in assigned:
            continue

        team_ids = [student["id"]]
        assigned.add(student["id"])

        while len(team_ids) < max_team_size:

            best_student = None
            best_score = -1

            for candidate in students:

                if candidate["id"] in assigned:
                    continue

                avg = 0

                for member in team_ids:
                    avg += compatibility_score(
                        student_map[member],
                        candidate
                    )

                avg /= len(team_ids)

                if avg > best_score:
                    best_score = avg
                    best_student = candidate["id"]

            if best_student is None:
                break

            assigned.add(best_student)
            team_ids.append(best_student)

        teams[team_no] = [student_map[i] for i in team_ids]

        team_no += 1

    return teams


# --------------------------
# Recommendations
# --------------------------
def recommend_partners(student_id, students, top_n=5):

    target = next(s for s in students if s["id"] == student_id)

    scores = []

    for student in students:

        if student["id"] == student_id:
            continue

        scores.append(
            (
                student["id"],
                compatibility_score(target, student)
            )
        )

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_n]


# --------------------------
# Testing
# --------------------------
if __name__ == "__main__":

    students = get_student_data()

    print(form_teams(students))

    if students:
        print(recommend_partners(students[0]["id"], students))