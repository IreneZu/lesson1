# Среднее время выполнения домашних заданий

homework_count = 12
hour_count = 1.5
name_of_course = 'Python'
time_for_work = hour_count / homework_count

str_course = 'Курс: ' + name_of_course
str_works = 'всего задач:'+ str(homework_count)
str_hours = 'затрачено часов:' + str(hour_count)
str_time = 'среднее время выполнения '+ str(time_for_work) + ' часа.'

print(str_course, str_works, str_hours, str_time, sep=', ')

