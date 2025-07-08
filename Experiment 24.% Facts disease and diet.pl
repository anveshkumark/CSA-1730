% Facts: disease and diet
diet(diabetes, 'Eat vegetables, whole grains, and low sugar foods').
diet(hypertension, 'Eat fruits, vegetables, and low salt foods').
diet(obesity, 'Eat low-calorie foods and high-fiber vegetables').
diet(anemia, 'Eat iron-rich foods like spinach and red meat').
diet(cholesterol, 'Eat oats, nuts, and avoid fried foods').

% Rule: suggest diet
suggest_diet(Disease, Diet) :- diet(Disease, Diet).
