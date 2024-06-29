import re
from collections import Counter


def extract_skills(description, skills):
    skills = [skill.lower() for skill in skills]

    skill_counts = Counter()

    for d in description:
        d = d.lower()

        for skill in skills:
            count = len(re.findall(r'\b' + re.escape(skill) + r'\b', d))
            skill_counts[skill] += count

    return dict(skill_counts)
