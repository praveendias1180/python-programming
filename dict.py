from turtle import screensize


my_first_dict = dict()

scores = {'Saman': 70, 'Praveen': 100, 'Kamal': 20}
scores['Sunil'] = 35

scores.pop('Praveen')

print(scores)
print(list(scores.keys()))
print(list(scores.values()))
print(scores['Saman'])
print(scores.get('Praveen'))

for key in scores:
    print(key, scores[key])