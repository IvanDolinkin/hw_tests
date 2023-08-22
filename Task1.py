from data import mentors, courses, durations, random_names, durations_test


def top_3_popular(mentors):
    all_names = []
    for group in mentors:
        for name in group:
            all_names.append(name.split()[0])

    unique_names = set(all_names)

    popular = []
    for name in unique_names:
        popular.append([name, all_names.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[:3]
    return (f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]}'
            f' раз(а)')


def sort_courses_by_duration(courses, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    result = []
    for k, v in durations_dict.items():
        for val in v:
            result.append(f'{courses_list[val]["title"]} - {k} месяцев')
    return result


def explore_relationship(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
        mcount_index.append([len(course["mentors"]), index])

    duration_index.sort()
    mcount_index.sort()

    indexes_d = []
    indexes_m = []

    for el in duration_index:
        indexes_d.append(el[1])

    for el in mcount_index:
        indexes_m.append(el[1])
    result = []
    [result.append(x) for x in [
        "Связь есть" if indexes_d == indexes_m else "Связи нет",
        "Порядок курсов по длительности: ",
        indexes_d,
        "Порядок курсов по количеству преподавателей: ",
        indexes_m]
     ]
    return result


if __name__ == '__main__':
    print(top_3_popular(mentors))
    print(*sort_courses_by_duration(courses, durations), sep='\n')
    print(*explore_relationship(courses, mentors, durations), sep='\n')
    print(top_3_popular(random_names))
    # print(top_3_popular(random_names_2))
    print(*explore_relationship(courses, mentors, durations_test), sep='\n')
    print(''.join([x[0] for x in sort_courses_by_duration(courses, durations)]))
